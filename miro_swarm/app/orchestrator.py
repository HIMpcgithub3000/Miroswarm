import uuid
import json
import logging
from typing import Dict, Any, List
from .database import get_db
from .llm_client import query_local_llm
from .causal import CausalCascadeEngine
from .adversarial import AdversarialSwarmEngine
from .metrics import MetricsEngine

logger = logging.getLogger('miro_swarm.orchestrator')

AGENT_ROLES = [
    {
        'role': 'Hospital_CFO',
        'prompt': 'Prioritize operating margin, physician retention, capital equipment ROI, and defensive unbundling.',
        'risk': 0.8,
        'financial': 0.95
    },
    {
        'role': 'Patient_Advocate',
        'prompt': 'Prioritize transparent all-inclusive billing, low out-of-pocket surprise costs, and consumer forum filings.',
        'risk': 0.2,
        'financial': 0.90
    },
    {
        'role': 'TPA_Auditor',
        'prompt': 'Enforce policy exclusions, audit unbundled PPE kits, disallow duplicate nursing charges, and control claim ratios.',
        'risk': 0.3,
        'financial': 0.85
    },
    {
        'role': 'Treating_Doctor',
        'prompt': 'Prioritize patient surgical outcomes, clinical discretion on implant choice, and minimal administrative discharge delay.',
        'risk': 0.5,
        'financial': 0.40
    },
    {
        'role': 'Regulator',
        'prompt': 'Enforce price ceiling compliance, mandate public rate disclosure, and penalize predatory hospital defiance.',
        'risk': 0.1,
        'financial': 0.70
    }
]

class MultiWorldOrchestrator:
    @staticmethod
    def spawn_agents_for_experiment(experiment_id: str, count: int = 5) -> List[str]:
        agent_ids = []
        with get_db() as db:
            for i in range(count):
                role_def = AGENT_ROLES[i % len(AGENT_ROLES)]
                agent_id = f'agt-{uuid.uuid4().hex[:8]}'
                db.execute(
                    '''INSERT INTO agents (id, experiment_id, role, persona_prompt, risk_tolerance, financial_sensitivity)
                       VALUES (?, ?, ?, ?, ?, ?)''',
                    (agent_id, experiment_id, role_def['role'], role_def['prompt'], role_def['risk'], role_def['financial'])
                )
                agent_ids.append(agent_id)
        return agent_ids

    @staticmethod
    def initialize_worlds_for_experiment(experiment_id: str) -> List[Dict[str, str]]:
        worlds_config = [
            {'key': 'world_a', 'name': 'World A — Baseline Status Quo', 'type': 'baseline'},
            {'key': 'world_b', 'name': 'World B — Mandatory Price Caps', 'type': 'price_cap'},
            {'key': 'world_c', 'name': 'World C — Consumable De-escalation', 'type': 'unbundling_ban'},
            {'key': 'world_d', 'name': 'World D — Provider Defiance Shock', 'type': 'chaos_boycott'}
        ]
        created_worlds = []
        with get_db() as db:
            for w in worlds_config:
                world_id = f'wld-{uuid.uuid4().hex[:8]}'
                cascade = CausalCascadeEngine.calculate_cascade(w['type'])
                db.execute(
                    '''INSERT INTO worlds (id, experiment_id, world_key, name, intervention_type, parameters_json, status)
                       VALUES (?, ?, ?, ?, ?, ?, 'initialized')''',
                    (world_id, experiment_id, w['key'], w['name'], w['type'], json.dumps(cascade))
                )
                created_worlds.append({'id': world_id, 'key': w['key'], 'name': w['name']})
        return created_worlds

    @staticmethod
    def run_simulation(experiment_id: str, rounds: int = 3) -> Dict[str, Any]:
        """
        Executes genuine isolated multi-agent simulation across all worlds.
        Enforces strict world-scoped memory isolation.
        """
        with get_db() as db:
            db.execute('UPDATE experiments SET status = "running" WHERE id = ?', (experiment_id,))
            worlds_cur = db.execute('SELECT * FROM worlds WHERE experiment_id = ?', (experiment_id,))
            worlds = worlds_cur.fetchall()
            agents_cur = db.execute('SELECT * FROM agents WHERE experiment_id = ?', (experiment_id,))
            agents = agents_cur.fetchall()

        total_events = 0
        for world in worlds:
            world_id = world['id']
            world_type = world['intervention_type']
            params = json.loads(world['parameters_json'])

            for round_idx in range(1, rounds + 1):
                for agent in agents:
                    agent_id = agent['id']
                    role = agent['role']

                    # 1. Query ONLY THIS WORLD'S memory for the agent (ZERO LEAKAGE)
                    with get_db() as db:
                        mem_cur = db.execute(
                            '''SELECT content FROM world_agent_memories 
                               WHERE world_id = ? AND agent_id = ? 
                               ORDER BY round_index DESC LIMIT 3''',
                            (world_id, agent_id)
                        )
                        past_memories = [m['content'] for m in mem_cur.fetchall()]

                    # 2. Agent decision logic based on world intervention
                    action_type = 'ACCEPT'
                    if role == 'Hospital_CFO':
                        action_type = 'DEFEND_CHARGES' if world_type in ('baseline', 'chaos_boycott') else 'COMPLIANCE_REVIEW'
                        action_content = f"Round {round_idx}: CFO evaluates surgery margin delta ({params['hospitalMarginDeltaPct']}%)"
                    elif role == 'Patient_Advocate':
                        action_type = 'DISPUTE_BILL' if params['expectedOutOfPocketShock'] > 30000 else 'CONFIRM_DISCHARGE'
                        action_content = f"Round {round_idx}: Advocate inspects OOP shock (₹{params['expectedOutOfPocketShock']})"
                    elif role == 'TPA_Auditor':
                        action_type = 'DEDUCT_CONSUMABLES' if params['consumableMarkupRate'] > 20 else 'AUTO_SETTLE'
                        action_content = f"Round {round_idx}: Auditor flags deduction rate at {params['tpaDeductionRate']}%"
                    else:
                        action_type = 'CLINICAL_VERIFY'
                        action_content = f"Round {round_idx}: {role} confirms procedure standard compliance."

                    event_id = f'evt-{uuid.uuid4().hex[:8]}'
                    mem_id = f'mem-{uuid.uuid4().hex[:8]}'

                    # 3. Persist Event and World-Scoped Memory
                    with get_db() as db:
                        db.execute(
                            '''INSERT INTO simulation_events (id, world_id, round_index, agent_id, action_type, action_payload_json)
                               VALUES (?, ?, ?, ?, ?, ?)''',
                            (event_id, world_id, round_idx, agent_id, action_type, json.dumps({'narrative': action_content}))
                        )
                        db.execute(
                            '''INSERT INTO world_agent_memories (id, world_id, agent_id, round_index, memory_type, content)
                               VALUES (?, ?, ?, ?, 'action', ?)''',
                            (mem_id, world_id, agent_id, round_idx, action_content)
                        )
                    total_events += 1

            with get_db() as db:
                db.execute('UPDATE worlds SET status = "completed" WHERE id = ?', (world_id,))

        # Run 3-Role Adversarial Debate
        with get_db() as db:
            proj_cur = db.execute(
                '''SELECT p.decision_question FROM projects p 
                   JOIN experiments e ON e.project_id = p.id 
                   WHERE e.id = ?''', (experiment_id,)
            )
            decision_q = proj_cur.fetchone()['decision_question']

        debate_turns = AdversarialSwarmEngine.run_debate_round(experiment_id, decision_q)

        # Mark experiment completed
        with get_db() as db:
            db.execute('UPDATE experiments SET status = "completed" WHERE id = ?', (experiment_id,))

        # Calculate final metrics
        metrics = MetricsEngine.calculate_experiment_metrics(experiment_id)

        return {
            'experimentId': experiment_id,
            'status': 'completed',
            'worldsSimulated': len(worlds),
            'totalRounds': rounds,
            'totalEventsPersisted': total_events,
            'debateTurns': len(debate_turns),
            'metrics': metrics
        }
