# MIRO SWARM — System Architecture & Component Specification
**Project:** Miro Swarm (Project 3 Capstone)  
**Document ID:** D02 (`MIRO_SWARM_ARCHITECTURE.md`)  
**Version:** 1.0  
**Date:** November 9, 2026  

---

## 1. High-Level Architecture Topology

Miro Swarm establishes strict, verifiable architectural boundaries across three independent services:

```mermaid
flowchart TB
    subgraph HEALTHDOOR["1. HEALTHDOOR — Healthcare Product (Port 3000)"]
        H1["Patient Billing Breakdown (7 Categories)"]
        H2["Hidden Charge Detection Engine"]
        H3["Hospital Transparency Ratings (A–F)"]
        H4["Community Bowls & Dispute Scripts"]
        H1 --> H2 --> H3 --> H4
    end

    subgraph SWARM_LAB["2. MIRO SWARM LAB — Decision Intelligence Platform (Port 3001)"]
        C1["Component 1: Idea Intake & Experiment Manager"]
        C2["Component 2: Enterprise Digital Twin (Versioned Graph)"]
        C3["Component 3: Agent Factory & World-Scoped Memory"]
        C4["Component 4: Multi-World Simulation Orchestrator"]
        C5["Component 5: Adversarial Swarm Engine (3-Way Debate)"]
        C6["Component 6: Causal & Counterfactual Engine"]
        C7["Component 7: Business Chaos Engineering Engine"]
        C8["Component 8: Uncertainty & AI Metrics Engine"]
        C9["Component 9: Closed-Loop Outcome Evaluation"]
        C10["Component 10: Reports & Decision Dashboard"]

        C1 --> C2 --> C3 --> C4
        C4 --> C5
        C4 --> C6
        C4 --> C7
        C5 & C6 & C7 --> C8 --> C9 --> C10
    end

    subgraph UPSTREAM_ENGINE["3. MIROFISH — Upstream Multi-Agent Runtime (Port 5001 / 5173)"]
        M1["Document Processing & Chunking"]
        M2["D3 Graph Extraction Foundation"]
        M3["OASIS Turn-Based Social Feed Sandbox"]
        M4["ReACT Agent Synthesis"]
        M1 --> M2 --> M3 --> M4
    end

    subgraph LOCAL_INFERENCE["4. LOCAL INFERENCE ENGINE (Port 11434)"]
        LLM["Ollama / llama.cpp (qwen2.5:1.5b-instruct on CPU)"]
    end

    H3 -. Optional Anonymized Scenario Export .-> C1
    SWARM_LAB <-->|Typed REST Adapter| UPSTREAM_ENGINE
    SWARM_LAB & UPSTREAM_ENGINE <-->|HTTP JSON / Private Localhost| LOCAL_INFERENCE
```

---

## 2. Architectural Boundary Rules

1. **Independent Operation Rule:**
   * **Healthdoor** operates independently on port `3000`. Its core patient-facing tools (bill audits, transparency scorecards) never depend on a running simulation or local LLM.
   * **Miro Swarm Lab** operates independently on port `3001`. It can ingest non-healthcare enterprise decisions (e.g., banking interest rate changes, retail supply chain disruptions) without Healthdoor installed.
   * **MiroFish** remains an independently deployable reference engine on ports `5001`/`5173`.
2. **Explicit Adapter Boundary:**
   * Miro Swarm Lab communicates with MiroFish strictly via an explicit typed HTTP REST client (`MiroFishAdapter`). MiroFish code is never imported into the Healthdoor React client.
3. **No Cross-World State Leakage:**
   * Each simulation world ($W_1, W_2, \dots, W_n$) maintains dedicated, isolated memory tables and event streams. An agent action in World A cannot mutate or influence World B.
4. **Local Hardware Budget Policy:**
   * Local inference is bound to `127.0.0.1:11434`. Memory consumption is capped below 50% total RAM (3.8 GiB) on the EC2 target.
5. **No Autonomous Production Modification:**
   * In strict accordance with capstone scope, all autonomous self-healing, automated PR creation, and production remediation features are excluded. Simulation findings remain human-reviewed decision-support artifacts.

---

## 3. Service & Port Allocations

| Service Name | Port | Host Binding | Process Manager | Primary Responsibility |
| :--- | :--- | :--- | :--- | :--- |
| **Healthdoor App** | `3000` | `0.0.0.0:3000` | PM2 (`healthdoor`) | Patient hospital bill audits, transparency scores |
| **Miro Swarm Lab** | `3001` | `0.0.0.0:3001` | PM2 (`miro-swarm`) | Decision rehearsal, digital-twin, adversarial analysis |
| **MiroFish Engine** | `5001` / `5173` | `127.0.0.1:5001` / `5173` | PM2 (`mirofish-ui`) | Upstream graph & social simulation engine |
| **Ollama Local LLM** | `11434` | `127.0.0.1:11434` | Systemd (`ollama`) | Offline CPU quantized inference (`qwen2.5:1.5b`) |
| **Persistence DB** | — | Local File | SQLite (`miro_swarm.db`)| Relational state, graph snapshots, events |
