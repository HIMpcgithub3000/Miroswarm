# UPSTREAM REUSE REGISTER
**Project:** Miro Swarm (Project 3 Capstone)  
**Document ID:** D09 (`UPSTREAM_REUSE_REGISTER.md`)  
**Version:** 1.0  
**Date:** November 9, 2026  

---

## 1. Upstream Repositories

### Repository A: MiroFish
* **Upstream URL:** `https://github.com/666ghj/MiroFish.git`
* **Pinned Commit Hash:** `7657031 chore: update Star History (#832)`
* **Primary License:** GNU AGPL-3.0
* **Reused Modules & Design Patterns:**
  1. `backend/app/services/text_processor.py`: Text chunking and sliding window algorithms for uploaded PDFs and Markdown files.
  2. `backend/app/services/oasis_profile_generator.py`: Demographic and behavioral agent attribute sampling inspired by OASIS.
  3. `backend/app/services/graph_builder.py`: D3-compatible node and edge formatting.
  4. `frontend/src/components/GraphPanel.vue`: Force-directed D3 visualization layout.
* **Modifications Made:**
  - Removed cloud-only hard dependencies on Alibaba Bailian (`dashscope`) and paid Zep Cloud tokens.
  - Replaced proprietary API calls with standard OpenAI-compatible local HTTP client configuration targeting localhost Ollama runtime.
  - Configured Linux Rollup native binaries (`@rollup/rollup-linux-x64-gnu`) for headless server execution.
* **Miro Swarm-Authored Contributions (Original Work):**
  - Enterprise Digital Twin 9-entity ontology & 8 directed relationships.
  - Multi-world counterfactual scenario orchestrator with isolated state stores.
  - 3-role adversarial debate protocol (Proposition, Opposition, Adjudicator).
  - Deterministic causal dependency cascade calculations.
  - Business chaos disruption injection engine.
  - Empirical benchmark calibration against IRDAI, AHPI, and NHA datasets.
  - Uncertainty decomposition and mathematical agent-behavior metrics.

---

### Repository B: gstack
* **Upstream URL:** `https://github.com/garrytan/gstack.git`
* **Primary License:** MIT
* **Reused Workflows & Conceptual Patterns:**
  1. Role-based engineering workflows (Product Architect, QA Reviewer, Systems Auditor).
  2. Explicit exclusion: The autonomous self-healing and production-remediation workflow is excluded per Project 3 scope.

---

## 2. Integration & Boundary Rules

1. **Separation of Services:**
   * Healthdoor, Miro Swarm Lab, and MiroFish maintain independent process, directory, and repository boundaries.
   * Healthdoor operates completely without MiroFish or local LLM runtimes.
   * Miro Swarm Lab interfaces with MiroFish strictly over documented REST API endpoints (`/api/graph`, `/api/simulation`).
2. **Attribution Integrity:**
   * Upstream modules remain clearly credited in source comments and documentation. No upstream feature is represented as an original Miro Swarm invention.
