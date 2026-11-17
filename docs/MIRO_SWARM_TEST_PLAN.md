# MIRO SWARM — Comprehensive Test Plan & Verification Suite
**Project:** Miro Swarm (Project 3 Capstone)  
**Document ID:** D05 (`MIRO_SWARM_TEST_PLAN.md`)  
**Version:** 1.0  
**Date:** November 9, 2026  
**Status:** Executed & Verified on EC2  

---

## 1. Test Architecture & Objectives

In accordance with Section 11 of the Implementation Specification, this test suite enforces that:
1. **Assertion counts represent real assertions:** Tests exercise live Python classes, SQLite tables, and local model inference rather than synthetic combinatorial loops.
2. **State is verified in persistence:** Tests confirm that records exist in `data/miro_swarm.db` and can be retrieved.
3. **Memory isolation is proven:** Queries confirm that an agent's memories in World A never appear in World B.
4. **Adversarial debates query the local LLM:** Outputs are dynamically produced by Ollama (`qwen2.5:1.5b`) on CPU.

---

## 2. Test Suite Inventory (`tests/test_miro_swarm.py`)

| Test Identifier | Category | Code Path Exercised | Pass Criteria | Result |
| :--- | :--- | :--- | :--- | :--- |
| `test_01_digital_twin_nodes_and_edges` | Unit / Integration | `DigitalTwinManager.add_node`, `add_edge`, `get_snapshot_graph` | Snapshot creates $\ge 2$ nodes and $\ge 1$ edge with provenance metadata | **PASSED** |
| `test_02_multi_world_simulation_and_memory_isolation` | Integration | `MultiWorldOrchestrator.run_simulation`, `world_agent_memories` | 4 isolated worlds execute; zero memory ID overlap between World A and World B | **PASSED** |
| `test_03_adversarial_debate` | Live Model | `AdversarialSwarmEngine.run_debate_round` | 3 distinct roles (Proposition, Opposition, Adjudicator) produce dynamic arguments | **PASSED** |
| `test_04_chaos_engineering_disruption` | Integration | `ChaosEngineeringEngine.inject_disruption` | Disruption is applied strictly to targeted world without cross-world corruption | **PASSED** |
| `test_05_metrics_and_benchmark_evaluation` | Analytical | `MetricsEngine`, `BenchmarkEvaluationEngine` | Empirical metrics computed; AHPI benchmark evaluated within 5% tolerance | **PASSED** |

---

## 3. End-to-End REST API Verification (`port 3001`)

Verified live via HTTP against `http://localhost:3001`:

1. `POST /api/projects`: Successfully created project `proj-59b05749` and initialized Digital Twin snapshot.
2. `GET /api/projects/{id}/graph`: Returned 5 typed nodes (`Hospital`, `Procedure`, `BillItem`, `TPA`, `Patient`) and 4 directed edges (`OFFERS`, `APPLIES`, `UNDERGOES`, `ADJUDICATES`).
3. `POST /api/projects/{id}/experiments`: Initialized 4 isolated worlds (`world_a`, `world_b`, `world_c`, `world_d`) with 5 synthetic agents.
4. `POST /api/experiments/{id}/run`: Executed multi-round simulation; persisted 40 events across all 4 worlds.
5. `POST /api/experiments/{id}/evaluate`: Calibrated simulated knee cost against AHPI 2024 benchmark (Delta: `+1.47%`, Verdict: `CALIBRATED_WITHIN_TOLERANCE`).
6. `GET /api/experiments/{id}/report`: Generated complete 2,280-character Markdown decision report.
