import unittest
import json
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import get_db
from app.digital_twin import DigitalTwinManager
from app.orchestrator import MultiWorldOrchestrator
from app.causal import CausalCascadeEngine
from app.chaos import ChaosEngineeringEngine
from app.metrics import MetricsEngine
from app.evaluation import BenchmarkEvaluationEngine
from app.adversarial import AdversarialSwarmEngine

class TestMiroSwarmE2E(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a test project
        import uuid
        cls.project_id = f"test-proj-{uuid.uuid4().hex[:6]}"
        with get_db() as db:
            db.execute(
                "INSERT INTO projects (id, name, domain, decision_question) VALUES (?, ?, ?, ?)",
                (cls.project_id, "E2E Test Healthcare Decision", "healthcare_pricing", "Should procedure caps be enforced?")
            )
        cls.snap_id = DigitalTwinManager.create_snapshot(cls.project_id, 1, "E2E Snapshot")

    def test_01_digital_twin_nodes_and_edges(self):
        hosp = DigitalTwinManager.add_node(self.snap_id, 'Hospital', 'Test Hospital', {'tier': 'corporate'})
        proc = DigitalTwinManager.add_node(self.snap_id, 'Procedure', 'Knee Arthroplasty', {'cost': 250000})
        edge = DigitalTwinManager.add_edge(self.snap_id, hosp, proc, 'OFFERS', {'rate': 250000}, 'Audit 2024')
        
        graph = DigitalTwinManager.get_snapshot_graph(self.snap_id)
        self.assertGreaterEqual(graph['nodeCount'], 2)
        self.assertGreaterEqual(graph['edgeCount'], 1)
        self.assertTrue(any(n['name'] == 'Test Hospital' for n in graph['nodes']))

    def test_02_multi_world_simulation_and_memory_isolation(self):
        exp_id = f"test-exp-{self.project_id}"
        with get_db() as db:
            db.execute(
                "INSERT INTO experiments (id, project_id, graph_snapshot_id, name, rounds, agent_count, status) VALUES (?, ?, ?, ?, 2, 3, 'configured')",
                (exp_id, self.project_id, self.snap_id, "E2E Experiment")
            )
        agents = MultiWorldOrchestrator.spawn_agents_for_experiment(exp_id, count=3)
        worlds = MultiWorldOrchestrator.initialize_worlds_for_experiment(exp_id)
        self.assertEqual(len(worlds), 4)

        # Run simulation
        result = MultiWorldOrchestrator.run_simulation(exp_id, rounds=2)
        self.assertEqual(result['status'], 'completed')
        self.assertGreater(result['totalEventsPersisted'], 0)

        # TEST STRICT WORLD MEMORY ISOLATION
        world_a_id = next(w['id'] for w in worlds if w['key'] == 'world_a')
        world_b_id = next(w['id'] for w in worlds if w['key'] == 'world_b')
        with get_db() as db:
            mem_a = db.execute("SELECT * FROM world_agent_memories WHERE world_id = ?", (world_a_id,)).fetchall()
            mem_b = db.execute("SELECT * FROM world_agent_memories WHERE world_id = ?", (world_b_id,)).fetchall()
            
            # Verify non-empty
            self.assertGreater(len(mem_a), 0)
            self.assertGreater(len(mem_b), 0)

            # Ensure zero cross-world memory ID overlap
            ids_a = set(m['id'] for m in mem_a)
            ids_b = set(m['id'] for m in mem_b)
            self.assertEqual(len(ids_a.intersection(ids_b)), 0)

    def test_03_adversarial_debate(self):
        exp_id = f"test-exp-{self.project_id}"
        turns = AdversarialSwarmEngine.run_debate_round(exp_id, "Mandatory surgery package price caps")
        self.assertEqual(len(turns), 3)
        roles = [t['role'] for t in turns]
        self.assertIn('proposition', roles)
        self.assertIn('opposition', roles)
        self.assertIn('adjudicator', roles)

    def test_04_chaos_engineering_disruption(self):
        exp_id = f"test-exp-{self.project_id}"
        with get_db() as db:
            world = db.execute("SELECT id FROM worlds WHERE experiment_id = ? LIMIT 1", (exp_id,)).fetchone()
        disruption = ChaosEngineeringEngine.inject_disruption(world['id'], 'tpa_preauth_blackout')
        self.assertEqual(disruption['severity'], 'High')
        self.assertEqual(disruption['status'], 'applied_to_world_only')

    def test_05_metrics_and_benchmark_evaluation(self):
        exp_id = f"test-exp-{self.project_id}"
        metrics = MetricsEngine.calculate_experiment_metrics(exp_id)
        self.assertIn('agentBehavior', metrics)
        self.assertGreater(metrics['agentBehavior']['participationRate']['value'], 0)

        # Evaluate against ground truth
        eval_res = BenchmarkEvaluationEngine.evaluate_experiment(exp_id, 'ahpi_2024_knee_pricing', 345000.0)
        self.assertEqual(eval_res['calibrationVerdict'], 'CALIBRATED_WITHIN_TOLERANCE')
        self.assertAlmostEqual(eval_res['percentageDelta'], 1.47, places=1)

if __name__ == '__main__':
    unittest.main()
