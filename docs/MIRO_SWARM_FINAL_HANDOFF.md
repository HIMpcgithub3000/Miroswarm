# MIRO SWARM — Final Handoff & System Documentation
**Project:** Miro Swarm (Project 3 Capstone — Final Semester, 5-Credit)  
**Document ID:** D10 (`MIRO_SWARM_FINAL_HANDOFF.md`)  
**Version:** 1.0  
**Date:** November 9, 2026  
**Target Environment:** AWS EC2 `13.201.1.13` (`i-07d77d0c076b1a49f` / `prj3`)  

---

## 1. System Inventory & Active Endpoints

All services are running, daemonized under PM2 and Systemd, and verified operational:

| Service | Runtime / Port | PM2 / Systemd Name | Status | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Healthdoor App** | Next.js 16 (`port 3000`) | `healthdoor` | **Online** | Patient-facing hospital bill audits, 4-tier hidden charges, A–F ratings |
| **Miro Swarm Lab API** | FastAPI (`port 3001`) | `miro-swarm-api` | **Online** | Primary Capstone decision platform (Digital Twin, Multi-World, Causal, Adversarial) |
| **MiroFish UI** | Vite / Vue 3 (`port 5173`)| `mirofish-ui` | **Online** | Upstream social simulation engine sandbox |
| **Local LLM Engine** | Ollama (`port 11434`) | `ollama.service` | **Active** | Quantized CPU inference (`qwen2.5:1.5b-instruct`) with AVX-512/AMX acceleration |
| **Persistence Database** | SQLite 3 | `data/miro_swarm.db` | **Active** | Relational state, 13 tables, WAL mode enabled |

---

## 2. Deliverables Register (D01 – D10)

| ID | Document Name | Location on EC2 | Description |
| :--- | :--- | :--- | :--- |
| **D01** | `MIRO_SWARM_IMPLEMENTATION_AUDIT.md` | `/home/ubuntu/` | Baseline audit, 697-assertion deconstruction, mocked vs. real inventory |
| **D02** | `MIRO_SWARM_ARCHITECTURE.md` | `/home/ubuntu/` | Independent service boundaries, process map, and data flow |
| **D03** | `MIRO_SWARM_API_CONTRACTS.md` | `/home/ubuntu/` | Typed REST endpoint specifications for projects, graphs, worlds, and reports |
| **D04** | `MIRO_SWARM_DATA_MODEL.md` | `/home/ubuntu/` | 13 relational tables with foreign keys, provenance, and snapshot invariance |
| **D05** | `MIRO_SWARM_TEST_PLAN.md` | `/home/ubuntu/` | Unit, integration, memory isolation, and live LLM test plan |
| **D06** | `MIRO_SWARM_LOCAL_MODEL_REPORT.md` | `/home/ubuntu/` | Hardware benchmarks, 8.06 tokens/sec, and 27.6% RAM budget compliance |
| **D07** | `MIRO_SWARM_EVALUATION_REPORT.md` | `/home/ubuntu/` | Baselines A/B/C comparisons, MAE = ₹5,000 against AHPI ground truth |
| **D08** | `THIRD_PARTY_NOTICES.md` | `/home/ubuntu/` | MiroFish (AGPL-3.0) and gstack (MIT) notices and boundaries |
| **D09** | `UPSTREAM_REUSE_REGISTER.md` | `/home/ubuntu/` | Reused modules, pinned commits, and modifications register |
| **D10** | `MIRO_SWARM_FINAL_HANDOFF.md` | `/home/ubuntu/` | This master operational handoff document |

---

## 3. How to Connect & Test

### A. Access Services Directly
* **Healthdoor:** `http://13.201.1.13:3000`
* **Miro Swarm Lab API (Interactive Swagger Docs):** `http://13.201.1.13:3001/docs`
* **MiroFish UI:** `http://13.201.1.13:5173`

*(If external security groups restrict ports 3000/3001/5173, tunnel via SSH)*:
```bash
ssh -i ~/.ssh/prj.pem -L 3000:localhost:3000 -L 3001:localhost:3001 -L 5173:localhost:5173 ubuntu@13.201.1.13
```

### B. Run the Full Automated Test Suite on EC2
```bash
ssh -i ~/.ssh/prj.pem ubuntu@13.201.1.13 "cd /home/ubuntu/MiroSwarm && ./venv/bin/python tests/test_miro_swarm.py"
```

### C. Check Server Health & PM2 Processes
```bash
ssh -i ~/.ssh/prj.pem ubuntu@13.201.1.13 "pm2 status && free -h"
```
