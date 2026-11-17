# THIRD-PARTY SOFTWARE NOTICES & LICENSES
**Project:** Miro Swarm (Project 3 Capstone)  
**Document ID:** D08 (`THIRD_PARTY_NOTICES.md`)  
**Version:** 1.0  
**Date:** November 9, 2026  

---

## 1. Upstream Open-Source Projects

This project studies and selectively interfaces with the following open-source repositories:

### 1.1 MiroFish
* **Upstream URL:** https://github.com/666ghj/MiroFish.git
* **Pinned Commit:** `7657031 chore: update Star History (#832)`
* **License:** GNU Affero General Public License v3.0 (AGPL-3.0)
* **Copyright:** Copyright (C) 2025-2026 MiroFish Contributors
* **License Text Summary:** The AGPL-3.0 grants permissions to run, copy, distribute, and modify the software, provided that any modified version made available over a computer network provides access to its source code under the same license terms.
* **Architecture Boundary Policy:** Miro Swarm maintains strict process and network isolation. MiroFish is deployed as a standalone backend service communicating exclusively across standard HTTP REST API contracts. Miro Swarm's proprietary enterprise digital twin, causal cascade, adversarial debate, and evaluation engines are engineered as independent modular systems.

### 1.2 gstack
* **Upstream URL:** https://github.com/garrytan/gstack.git
* **License:** MIT License
* **Copyright:** Copyright (c) 2024 Garry Tan
* **License Text Summary:** Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies.
* **Usage in Miro Swarm:** Reused purely as a reference for role-based software development workflows and audit disciplines. Autonomous code recovery workflows are excluded from Miro Swarm scope.

---

## 2. Key Dependencies & Runtimes

| Component | Upstream Package | License | Scope |
| :--- | :--- | :--- | :--- |
| **Frontend Framework** | Next.js (Vercel, Inc.) | MIT | Healthdoor application & Swarm UI |
| **Component Library** | Lucide React | ISC | UI iconography |
| **Python Web Framework** | Flask (Pallets Projects) | BSD-3-Clause | MiroFish backend API server |
| **PDF Extraction** | PyMuPDF (Artifex Software, Inc.) | AGPL-3.0 | Document text ingestion |
| **Local Inference Runtime** | Ollama | MIT | Local CPU inference on EC2 |
| **Process Manager** | PM2 | AGPL-3.0 | Daemonization of background workers |
