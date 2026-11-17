# MIRO SWARM — REST API Contracts & Endpoint Specifications
**Project:** Miro Swarm (Project 3 Capstone)  
**Document ID:** D03 (`MIRO_SWARM_API_CONTRACTS.md`)  
**Version:** 1.0  
**Date:** November 9, 2026  

---

## 1. Overview & Protocol Guidelines

All endpoints are hosted by **Miro Swarm Lab** (Port 3001) under the `/api` route prefix. All payloads and responses enforce strict JSON formatting (`application/json`) with standard HTTP status codes:
* `200 OK`: Successful retrieval / processing.
* `201 Created`: Resource successfully created.
* `400 Bad Request`: Validation failure or malformed payload.
* `404 Not Found`: Resource ID does not exist.
* `500 Internal Error`: Worker crash or model generation error.

---

## 2. Endpoint Specifications

### 2.1 Project & Idea Intake
#### `POST /api/projects`
Creates a new decision project from natural-language idea.
* **Request:**
  ```json
  {
    "name": "Mandatory Procedure Price Capping",
    "domain": "healthcare_pricing",
    "decisionQuestion": "What happens if hospitals are required to cap surgery packages?",
    "baselineDescription": "Unregulated hospital billing with 450% consumable markup."
  }
  ```
* **Response (201 Created):**
  ```json
  {
    "projectId": "proj-901",
    "name": "Mandatory Procedure Price Capping",
    "status": "intake_approved",
    "createdAt": "2026-11-09T00:00:00Z"
  }
  ```

#### `GET /api/projects/{id}`
Retrieves project details, active experiments, and linked digital-twin version.

---

### 2.2 Ingestion & Digital Twin Graph
#### `POST /api/projects/{id}/documents`
Uploads raw documents (PDF, Markdown, CSV) to project storage.
* **Request:** `multipart/form-data` with `file` payload.
* **Response (201 Created):**
  ```json
  {
    "documentId": "doc-01",
    "fileName": "AHPI_Knee_Replacement_Benchmark_2024.pdf",
    "fileSize": 451200,
    "sha256": "8f4b23...",
    "status": "uploaded"
  }
  ```

#### `POST /api/projects/{id}/ingestion`
Triggers entity/relationship extraction via local model into the digital-twin graph.
* **Request:** `{"documentId": "doc-01"}`
* **Response (200 OK):**
  ```json
  {
    "graphVersion": 1,
    "extractedNodes": 9,
    "extractedEdges": 8,
    "status": "ready_for_review"
  }
  ```

#### `GET /api/projects/{id}/graph`
Retrieves current persisted graph snapshot with nodes, edges, and provenance metadata.

---

### 2.3 Experiment & Multi-World Simulation
#### `POST /api/projects/{id}/experiments`
Configures a controlled simulation experiment with baseline and intervention scenarios.
* **Request:**
  ```json
  {
    "name": "Price Cap Resilience Test",
    "graphVersion": 1,
    "scenarios": [
      { "worldKey": "world_a", "name": "Status Quo", "interventionType": "baseline" },
      { "worldKey": "world_b", "name": "Strict Package Caps", "interventionType": "price_cap" },
      { "worldKey": "world_c", "name": "Consumables De-escalation", "interventionType": "unbundling_ban" },
      { "worldKey": "world_d", "name": "Provider Defiance Shock", "interventionType": "chaos_boycott" }
    ],
    "rounds": 5,
    "agentCount": 20
  }
  ```
* **Response (201 Created):**
  ```json
  {
    "experimentId": "exp-501",
    "worlds": ["wld-1", "wld-2", "wld-3", "wld-4"],
    "status": "configured"
  }
  ```

#### `POST /api/experiments/{id}/run`
Triggers execution of the isolated worlds using local model workers.
* **Response (200 OK):** `{"experimentId": "exp-501", "status": "running"}`

#### `GET /api/experiments/{id}`
Returns current execution progress, completed rounds, and active status per world.

#### `GET /api/worlds/{id}/events`
Returns raw, immutable simulation action log for a specific world.

---

### 2.4 Adversarial Debate & Causal Impact
#### `GET /api/experiments/{id}/adversarial-debate`
Retrieves the structured 3-role dialectic transcript (Proposition, Opposition, Adjudicator) grounded in graph evidence.

#### `GET /api/experiments/{id}/causal-cascade`
Retrieves the mathematical DAG calculating variable propagation paths (e.g., consumable cap $\rightarrow$ hospital margin compression $\rightarrow$ diagnostic unbundling).

---

### 2.5 Metrics & Closed-Loop Evaluation
#### `GET /api/experiments/{id}/metrics`
Returns calculated metrics across three separate categories:
1. **Agent Behavior Metrics:** `participationRate`, `evidenceSupportRate`, `contradictionRate`, `polarizationIndex`, `consensusScore`.
2. **Business Outcome Metrics:** `oopVariance`, `tpaDeductionRate`, `hospitalSolvencyRisk`.
3. **Reliability Metrics:** `missingDataWarnings`, `predictionVarianceAcrossWorlds`.

#### `POST /api/experiments/{id}/evaluate`
Evaluates simulated predictions against held-out ground truth datasets (AHPI, IRDAI, CGHS).
* **Request:** `{"datasetKey": "ahpi_2024_knee_pricing"}`
* **Response (200 OK):**
  ```json
  {
    "evaluationId": "eval-101",
    "dataset": "AHPI 2024 Knee Cost Benchmark",
    "metrics": {
      "mae": 5000,
      "rmse": 6200,
      "percentageDelta": 1.47
    },
    "verdict": "within_tolerance_5pct"
  }
  ```

#### `GET /api/experiments/{id}/report`
Exports the complete, reproducible markdown experiment report with assumptions, evidence citations, and limitations.
