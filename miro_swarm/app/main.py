import os
import uuid
import json
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .database import get_db
from .digital_twin import DigitalTwinManager
from .orchestrator import MultiWorldOrchestrator
from .causal import CausalCascadeEngine
from .chaos import ChaosEngineeringEngine
from .metrics import MetricsEngine
from .evaluation import BenchmarkEvaluationEngine

app = FastAPI(title="Miro Swarm Lab Decision Platform", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------- Models -----------------
class ProjectCreate(BaseModel):
    name: str
    domain: str
    decisionQuestion: str
    baselineDescription: Optional[str] = ""

class ExperimentCreate(BaseModel):
    name: str
    rounds: Optional[int] = 3
    agentCount: Optional[int] = 5

class DisruptionCreate(BaseModel):
    templateKey: str
    customParams: Optional[Dict[str, Any]] = None

class EvaluateRequest(BaseModel):
    datasetKey: str
    simulatedValue: float

# ----------------- Endpoints -----------------
@app.get("/health")
def health():
    return {"status": "ok", "service": "Miro Swarm Lab Platform", "port": 3001}

@app.post("/api/projects", status_code=201)
def create_project(req: ProjectCreate):
    proj_id = f"proj-{uuid.uuid4().hex[:8]}"
    with get_db() as db:
        db.execute(
            '''INSERT INTO projects (id, name, domain, decision_question, baseline_description)
               VALUES (?, ?, ?, ?, ?)''',
            (proj_id, req.name, req.domain, req.decisionQuestion, req.baselineDescription)
        )
    # Automatically initialize Snapshot 1
    snap_id = DigitalTwinManager.create_snapshot(proj_id, 1, "Initial Digital Twin Snapshot")
    
    # Pre-seed default healthcare digital-twin nodes for demonstrator
    hosp_id = DigitalTwinManager.add_node(snap_id, 'Hospital', 'Apollo Multi-Specialty Hospital', {'city': 'Delhi-NCR', 'nabhAccredited': True})
    proc_id = DigitalTwinManager.add_node(snap_id, 'Procedure', 'Coronary Angioplasty (PTCA)', {'category': 'Cardiology', 'baseCostINR': 210000})
    item_id = DigitalTwinManager.add_node(snap_id, 'BillItem', 'Sterile Surgical PPE & Gowns', {'category': 'Consumables', 'medianMarkup': '450%'})
    tpa_id = DigitalTwinManager.add_node(snap_id, 'TPA', 'MediAssist TPA', {'claimSettlementRate': '76%'})
    pat_id = DigitalTwinManager.add_node(snap_id, 'Patient', 'Middle-Class Inpatient Cohort', {'financialSensitivity': 'High'})
    
    DigitalTwinManager.add_edge(snap_id, hosp_id, proc_id, 'OFFERS', {'baseCost': 210000}, 'Hospital rate card 2024')
    DigitalTwinManager.add_edge(snap_id, hosp_id, item_id, 'APPLIES', {'markupMultiplier': 4.5}, 'Discharge audit #DEL-4491')
    DigitalTwinManager.add_edge(snap_id, pat_id, proc_id, 'UNDERGOES', {'volumeWeight': 0.45}, 'Elective cardiology cohort')
    DigitalTwinManager.add_edge(snap_id, tpa_id, item_id, 'ADJUDICATES', {'deductionRatio': 0.24}, 'IRDAI non-payable list')

    return {"projectId": proj_id, "snapshotId": snap_id, "status": "created"}

@app.get("/api/projects/{id}")
def get_project(id: str):
    with get_db() as db:
        cur = db.execute("SELECT * FROM projects WHERE id = ?", (id,))
        proj = cur.fetchone()
        if not proj:
            raise HTTPException(status_code=404, detail="Project not found")
        snaps = db.execute("SELECT * FROM graph_snapshots WHERE project_id = ?", (id,)).fetchall()
        exps = db.execute("SELECT * FROM experiments WHERE project_id = ?", (id,)).fetchall()

    return {
        "project": dict(proj),
        "snapshots": [dict(s) for s in snaps],
        "experiments": [dict(e) for e in exps]
    }

@app.get("/api/projects/{id}/graph")
def get_project_graph(id: str):
    with get_db() as db:
        cur = db.execute("SELECT id FROM graph_snapshots WHERE project_id = ? AND is_active = 1", (id,))
        snap = cur.fetchone()
        if not snap:
            raise HTTPException(status_code=404, detail="No active graph snapshot found for project")
        snap_id = snap['id']

    return DigitalTwinManager.get_snapshot_graph(snap_id)

@app.post("/api/projects/{id}/experiments", status_code=201)
def create_experiment(id: str, req: ExperimentCreate):
    exp_id = f"exp-{uuid.uuid4().hex[:8]}"
    with get_db() as db:
        snap_cur = db.execute("SELECT id FROM graph_snapshots WHERE project_id = ? AND is_active = 1", (id,))
        snap = snap_cur.fetchone()
        if not snap:
            raise HTTPException(status_code=400, detail="Project lacks an active graph snapshot")
        snap_id = snap['id']

        db.execute(
            '''INSERT INTO experiments (id, project_id, graph_snapshot_id, name, rounds, agent_count, status)
               VALUES (?, ?, ?, ?, ?, ?, 'configured')''',
            (exp_id, id, snap_id, req.name, req.rounds, req.agentCount)
        )

    # Spawn agents & initialize worlds
    MultiWorldOrchestrator.spawn_agents_for_experiment(exp_id, req.agentCount)
    worlds = MultiWorldOrchestrator.initialize_worlds_for_experiment(exp_id)

    return {"experimentId": exp_id, "worlds": worlds, "status": "configured"}

@app.post("/api/experiments/{id}/run")
def run_experiment(id: str):
    with get_db() as db:
        cur = db.execute("SELECT rounds FROM experiments WHERE id = ?", (id,))
        exp = cur.fetchone()
        if not exp:
            raise HTTPException(status_code=404, detail="Experiment not found")
        rounds = exp['rounds']

    res = MultiWorldOrchestrator.run_simulation(id, rounds)
    return res

@app.get("/api/experiments/{id}")
def get_experiment_status(id: str):
    with get_db() as db:
        exp_cur = db.execute("SELECT * FROM experiments WHERE id = ?", (id,))
        exp = exp_cur.fetchone()
        if not exp:
            raise HTTPException(status_code=404, detail="Experiment not found")
        worlds_cur = db.execute("SELECT * FROM worlds WHERE experiment_id = ?", (id,))
        worlds = [dict(w) for w in worlds_cur.fetchall()]

    return {"experiment": dict(exp), "worlds": worlds}

@app.get("/api/worlds/{id}/events")
def get_world_events(id: str):
    with get_db() as db:
        cur = db.execute("SELECT * FROM simulation_events WHERE world_id = ? ORDER BY round_index ASC, created_at ASC", (id,))
        events = [dict(e) for e in cur.fetchall()]
    return {"worldId": id, "eventCount": len(events), "events": events}

@app.post("/api/worlds/{id}/disrupt")
def inject_world_disruption(id: str, req: DisruptionCreate):
    return ChaosEngineeringEngine.inject_disruption(id, req.templateKey, req.customParams)

@app.get("/api/experiments/{id}/metrics")
def get_experiment_metrics(id: str):
    return MetricsEngine.calculate_experiment_metrics(id)

@app.post("/api/experiments/{id}/evaluate")
def evaluate_experiment(id: str, req: EvaluateRequest):
    return BenchmarkEvaluationEngine.evaluate_experiment(id, req.datasetKey, req.simulatedValue)

@app.get("/api/experiments/{id}/report")
def export_experiment_report(id: str):
    with get_db() as db:
        exp_cur = db.execute("SELECT * FROM experiments WHERE id = ?", (id,))
        exp = exp_cur.fetchone()
        if not exp:
            raise HTTPException(status_code=404, detail="Experiment not found")
        proj_cur = db.execute("SELECT * FROM projects WHERE id = ?", (exp['project_id'],))
        proj = proj_cur.fetchone()
        debates_cur = db.execute("SELECT * FROM adversarial_debates WHERE experiment_id = ?", (id,))
        debates = debates_cur.fetchall()
        evals_cur = db.execute("SELECT * FROM benchmark_evaluations WHERE experiment_id = ?", (id,))
        evals = evals_cur.fetchall()

    metrics = MetricsEngine.calculate_experiment_metrics(id)

    report_md = f"""# MIRO SWARM EXPERIMENT REPORT: {exp['name']}
**Project ID:** {proj['id']}  
**Domain:** {proj['domain']}  
**Decision Question:** {proj['decision_question']}  
**Status:** {exp['status']}  

---

## 1. Executive Summary & Recommendation
The multi-world simulation executed across 4 isolated futures testing procedural price caps against the baseline unregulated healthcare market.

## 2. Adversarial Swarm Dialectic
"""
    for d in debates:
        report_md += f"- **[{d['speaker_role'].upper()}] {d['speaker_role']}**: {d['argument_text']}\n  *Evidence*: {d['evidence_citation']}\n\n"

    report_md += f"""
## 3. Key Quantitative Metrics
- **Participation Rate:** {metrics['agentBehavior']['participationRate']['value']}
- **Evidence Support Rate:** {metrics['agentBehavior']['evidenceSupportRate']['value']}
- **Contradiction Rate:** {metrics['agentBehavior']['contradictionRate']['value']}
- **Consensus Score:** {metrics['agentBehavior']['consensusScore']['value']}

## 4. Ground-Truth Benchmark Evaluations
"""
    for ev in evals:
        report_md += f"- **Dataset**: {ev['dataset_name']} | **MAE**: ₹{ev['error_mae']} | **Delta**: {ev['error_delta_percent']}% ({ev['verdict']})\n"

    return {"experimentId": id, "reportMarkdown": report_md}
