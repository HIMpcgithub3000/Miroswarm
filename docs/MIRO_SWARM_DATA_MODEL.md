# MIRO SWARM — Data Model & Persistence Specification
**Project:** Miro Swarm (Project 3 Capstone)  
**Document ID:** D04 (`MIRO_SWARM_DATA_MODEL.md`)  
**Version:** 1.0  
**Date:** November 9, 2026  

---

## 1. Storage Architecture

Miro Swarm uses an embedded, high-performance relational database (**SQLite 3**) located at:
`data/miro_swarm.db` (with Write-Ahead Logging `WAL` mode enabled for concurrent worker queries).

---

## 2. Relational Schemas

```sql
-- 1. Projects & Decision Intake
CREATE TABLE IF NOT EXISTS projects (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    domain TEXT NOT NULL,
    decision_question TEXT NOT NULL,
    baseline_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Source Documents & File Registry
CREATE TABLE IF NOT EXISTS source_documents (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES projects(id),
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    sha256 TEXT NOT NULL,
    status TEXT NOT NULL, -- 'uploaded', 'processed', 'failed'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Digital-Twin Graph Snapshots (Versioned)
CREATE TABLE IF NOT EXISTS graph_snapshots (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES projects(id),
    version INTEGER NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Digital-Twin Entity Nodes (9 Healthcare Entity Types)
CREATE TABLE IF NOT EXISTS graph_nodes (
    id TEXT PRIMARY KEY,
    snapshot_id TEXT NOT NULL REFERENCES graph_snapshots(id),
    entity_type TEXT NOT NULL, -- 'Hospital', 'Procedure', 'BillItem', 'TPA', 'Patient', 'Doctor', 'Regulator', 'PriceBenchmark', 'CommunityBowl'
    name TEXT NOT NULL,
    properties_json TEXT NOT NULL,
    source_document_id TEXT REFERENCES source_documents(id),
    source_chunk_index INTEGER,
    confidence_score REAL DEFAULT 1.0,
    human_approved BOOLEAN DEFAULT 1
);

-- 5. Digital-Twin Relational Edges (8 Directed Relationship Types)
CREATE TABLE IF NOT EXISTS graph_edges (
    id TEXT PRIMARY KEY,
    snapshot_id TEXT NOT NULL REFERENCES graph_snapshots(id),
    source_node_id TEXT NOT NULL REFERENCES graph_nodes(id),
    target_node_id TEXT NOT NULL REFERENCES graph_nodes(id),
    relationship_type TEXT NOT NULL, -- 'OFFERS', 'APPLIES', 'UNDERGOES', 'ADJUDICATES', 'CONSTRAINS', 'REQUIRES', 'FILES', 'CONTESTS'
    properties_json TEXT NOT NULL,
    provenance_reference TEXT
);

-- 6. Experiments
CREATE TABLE IF NOT EXISTS experiments (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES projects(id),
    graph_snapshot_id TEXT NOT NULL REFERENCES graph_snapshots(id),
    name TEXT NOT NULL,
    rounds INTEGER NOT NULL DEFAULT 5,
    agent_count INTEGER NOT NULL DEFAULT 10,
    status TEXT NOT NULL, -- 'created', 'running', 'completed', 'failed'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 7. Simulation Worlds (Isolated Alternative Futures)
CREATE TABLE IF NOT EXISTS worlds (
    id TEXT PRIMARY KEY,
    experiment_id TEXT NOT NULL REFERENCES experiments(id),
    world_key TEXT NOT NULL, -- 'world_a', 'world_b', 'world_c', 'world_d'
    name TEXT NOT NULL,
    intervention_type TEXT NOT NULL, -- 'baseline', 'price_cap', 'unbundling_ban', 'chaos_boycott'
    parameters_json TEXT NOT NULL,
    status TEXT NOT NULL -- 'pending', 'active', 'completed', 'failed'
);

-- 8. Synthetic Agents
CREATE TABLE IF NOT EXISTS agents (
    id TEXT PRIMARY KEY,
    experiment_id TEXT NOT NULL REFERENCES experiments(id),
    role TEXT NOT NULL, -- 'Hospital_CFO', 'Patient_Advocate', 'Treating_Doctor', 'TPA_Auditor', 'Regulator'
    persona_prompt TEXT NOT NULL,
    risk_tolerance REAL,
    financial_sensitivity REAL
);

-- 9. World-Scoped Agent Memory (Strict Isolation: NO Leakage)
CREATE TABLE IF NOT EXISTS world_agent_memories (
    id TEXT PRIMARY KEY,
    world_id TEXT NOT NULL REFERENCES worlds(id),
    agent_id TEXT NOT NULL REFERENCES agents(id),
    round_index INTEGER NOT NULL,
    memory_type TEXT NOT NULL, -- 'observation', 'action', 'reflection'
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 10. Immutable Simulation Event Log
CREATE TABLE IF NOT EXISTS simulation_events (
    id TEXT PRIMARY KEY,
    world_id TEXT NOT NULL REFERENCES worlds(id),
    round_index INTEGER NOT NULL,
    agent_id TEXT NOT NULL REFERENCES agents(id),
    action_type TEXT NOT NULL, -- 'POST', 'DISPUTE', 'DENY', 'ACCEPT', 'BOYCOTT'
    action_payload_json TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 11. Adversarial Debate Transcripts
CREATE TABLE IF NOT EXISTS adversarial_debates (
    id TEXT PRIMARY KEY,
    experiment_id TEXT NOT NULL REFERENCES experiments(id),
    round_index INTEGER NOT NULL,
    speaker_role TEXT NOT NULL, -- 'proposition', 'opposition', 'adjudicator'
    argument_text TEXT NOT NULL,
    evidence_citation TEXT,
    assumptions_stated TEXT
);

-- 12. Experiment Metrics
CREATE TABLE IF NOT EXISTS experiment_metrics (
    id TEXT PRIMARY KEY,
    experiment_id TEXT NOT NULL REFERENCES experiments(id),
    world_id TEXT REFERENCES worlds(id),
    category TEXT NOT NULL, -- 'agent_behavior', 'business_outcome', 'reliability'
    metric_name TEXT NOT NULL,
    metric_value REAL NOT NULL,
    unit TEXT,
    formula_reference TEXT
);

-- 13. Ground-Truth Benchmarks & Evaluations
CREATE TABLE IF NOT EXISTS benchmark_evaluations (
    id TEXT PRIMARY KEY,
    experiment_id TEXT NOT NULL REFERENCES experiments(id),
    dataset_name TEXT NOT NULL,
    target_metric TEXT NOT NULL,
    simulated_value REAL NOT NULL,
    benchmark_value REAL NOT NULL,
    error_mae REAL NOT NULL,
    error_delta_percent REAL NOT NULL,
    verdict TEXT NOT NULL,
    evaluated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 3. Provenance & Snapshot Invariance Principle

1. **Snapshot Pinning:** Once an experiment is executed against `graph_snapshot_id`, editing nodes or edges in subsequent snapshots never alters the historical experiment data.
2. **Provenance Traceability:** Every node and edge in `graph_nodes` and `graph_edges` links directly to a `source_document_id` and a `source_chunk_index`, enabling zero-hallucination audits.
3. **World Memory Isolation:** The composite index on `(world_id, agent_id, round_index)` guarantees that queries for an agent's memory are scoped exclusively to their designated simulation world.
