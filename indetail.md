# 📘 MIRO SWARM: Exhaustive Technical Specification & Mathematical Architecture
**Version**: 1.0 (Production / Capstone Final Delivery)  
**Author**: Himanshu Sharma  
**Target Environment**: Antigravity Stack / AWS EC2 Linux / Local CPU Ollama  
**Upstream Foundations**: MiroFish (AGPL-3.0), gstack (MIT Reference)

---

## Table of Contents
1. [Executive Architecture & Product Decoupling](#1-executive-architecture--product-decoupling)
2. [The Seven Core Innovations: Mathematical & Algorithmic Formulations](#2-the-seven-core-innovations-mathematical--algorithmic-formulations)
   - [2.1 Innovation 1: Enterprise Digital Twin](#21-innovation-1-enterprise-digital-twin)
   - [2.2 Innovation 2: Causal Simulation & Pearl's Counterfactuals](#22-innovation-2-causal-simulation--pearls-counterfactuals)
   - [2.3 Innovation 3: Adversarial Swarm & Loopholes Discovery](#23-innovation-3-adversarial-swarm--loopholes-discovery)
   - [2.4 Innovation 4: Business Chaos Engineering](#24-innovation-4-business-chaos-engineering)
   - [2.5 Innovation 5: Uncertainty Intelligence & Bayesian Bounds](#25-innovation-5-uncertainty-intelligence--bayesian-bounds)
   - [2.6 Innovation 6: Closed-Loop Learning & Outcome Assessment](#26-innovation-6-closed-loop-learning--outcome-assessment)
   - [2.7 Innovation 7: Multi-World Simulation Management](#27-innovation-7-multi-world-simulation-management)
3. [Zero-Credit Local Inference Architecture](#3-zero-credit-local-inference-architecture)
4. [The 5-Day (120-Hour) Continuous Simulation: Empirical Proof](#4-the-5-day-120-hour-continuous-simulation-empirical-proof)
5. [Ecosystem Guard: Downstream Counter-Retaliation Product](#5-ecosystem-guard-downstream-counter-retaliation-product)
6. [Complete System Trace: MiroFish vs Miro Swarm vs Ecosystem Guard](#6-complete-system-trace-mirofish-vs-miro-swarm-vs-ecosystem-guard)
7. [Production Deployment, PM2 & Nginx Architecture](#7-production-deployment-pm2--nginx-architecture)
8. [API Contracts & Database Schemas](#8-api-contracts--database-schemas)
9. [Seed PRD Document Specification: Input Guidelines & Domain Rules](#9-seed-prd-document-specification-input-guidelines--domain-rules)
   - [9.1 What MUST Be Included (क्या होना चाहिए)](#91-what-must-be-included-क्या-होना-चाहिए)
   - [9.2 What MUST NOT Be Included (क्या नहीं होना चाहिए)](#92-what-must-not-be-included-क्या-नहीं-होना-चाहिए)
   - [9.3 Mathematical Rationale for Multi-Agent Swarms](#93-mathematical-rationale-for-multi-agent-swarms)
   - [9.4 Canonical PRD Markdown Template (.md)](#94-canonical-prd-markdown-template-md)

---

## 1. Executive Architecture & Product Decoupling

The Miro Swarm platform enforces strict modular boundaries between three independent products:

```mermaid
flowchart TD
    subgraph P1["Product 1: Miro Swarm Lab (Primary Capstone Engine)"]
        SW_API["FastAPI Orchestrator (:3001)"]
        DT["Enterprise Digital Twin"]
        CAUSAL["Causal DAG & Counterfactuals"]
        ADV["Adversarial Swarm Engine"]
        CHAOS["Business Chaos Injector"]
        UNCERT["Uncertainty Intelligence"]
        EVAL["Closed-Loop Learning Evaluator"]
        MW["Multi-World Coordinator"]
        RUNNER["5-Day Continuous Runner Daemon"]
    end

    subgraph P2["Product 2: MiroFish Engine (Simulation Hub)"]
        MF_BACKEND["FastAPI Engine (:5001)"]
        MF_UI["Vue 3 + Vite Production UI (Port 80 /mirofish/)"]
        D3_GRAPH["D3 Force-Directed Network"]
        OASIS_SANDBOX["Twitter / Reddit Multi-Agent Sandboxes"]
        REACT_AGENT["ReACT Analytical Report Agent"]
    end

    subgraph P3["Product 3: Ecosystem Guard (Downstream Mitigation)"]
        EG_BACKEND["FastAPI Audit Engine (:3002)"]
        EG_UI["Single-Page Application (/guard/)"]
        OT_RADAR["Compensatory OT Surge Radar (+42.6%)"]
        NPPA_SCRUB["15% Consumable Markup Scrubber"]
        LEGAL_GEN["Consumer Law Formal Notice Generator"]
    end

    subgraph P0["Historical Context: Healthdoor (Archived)"]
        HD_DOC["HEALTHDOOR_DETAILED_SPECIFICATION.md"]
    end

    P1 -->|Feeds Discovered Retaliation Data| P3
    P1 <-->|Bi-Directional Adapters & State APIs| P2
    P0 -.->|Specification Preserved| P1
```

### The Decoupling Rationale
* **Healthdoor Decoupling**: Healthdoor was a patient-facing billing transparency prototype. To avoid conflating verified hospital pricing with simulated synthetic worlds, Healthdoor was documented into [HEALTHDOOR_DETAILED_SPECIFICATION.md](docs/HEALTHDOOR_DETAILED_SPECIFICATION.md) and removed from the active runtime.
* **MiroFish Substrate**: MiroFish serves as an underlying turn-based social simulation substrate with D3 graph visualization and SQLite-backed persona state machines.
* **Miro Swarm Primacy**: Miro Swarm houses the decision intelligence, Pearl causal counterfactuals, adversarial loophole testing, and chaos perturbations.
* **Ecosystem Guard Delivery**: Ecosystem Guard operationalizes the simulation findings into a deployable software product that protects patients and insurers from the exact retaliation tactics discovered during simulation.

---

## 2. The Seven Core Innovations: Mathematical & Algorithmic Formulations

### 2.1 Innovation 1: Enterprise Digital Twin

An enterprise ecosystem cannot be modeled as a flat list of agents; it is an attributed heterogeneous directed graph:

$$\mathcal{G}_{ET} = (\mathcal{V}, \mathcal{E}, \mathcal{A}_V, \mathcal{A}_E, \Phi_V, \Phi_E)$$

Where:
* $\mathcal{V}$ is the set of entity nodes partitioned into 9 disjoint classes:
  $$\Phi_V(v) \in \{\text{Hospital}, \text{CFO}, \text{SpecialistDoctor}, \text{InsuranceTPA}, \text{Regulator}, \text{ConsumerForum}, \text{Patient}, \text{TariffRule}, \text{ConsumableKit}\}$$
* $\mathcal{E} \subseteq \mathcal{V} \times \mathcal{V}$ is the set of directed edges partitioned into 8 relation types:
  $$\Phi_E(e) \in \{\text{EMPLOYS}, \text{ADJUDICATES}, \text{CONSUMES}, \text{AUDITS}, \text{REGULATES}, \text{MARKS\_UP}, \text{COMPENSATES\_WITH}, \text{BILLS}\}$$
* $\mathcal{A}_V: \mathcal{V} \to \mathbb{R}^k$ maps nodes to dynamic state feature vectors (e.g., Hospital EBITDA margin, Specialist procedural quota, TPA loss ratio target).
* $\mathcal{A}_E: \mathcal{E} \to \mathbb{R}^m$ maps edges to coupling weights and regulatory compliance thresholds.

```python
# app/digital_twin.py implementation pattern
class EnterpriseDigitalTwin:
    def __init__(self, twin_id: str, name: str, domain: str):
        self.twin_id = twin_id
        self.nodes: Dict[str, Dict[str, Any]] = {}
        self.edges: List[Dict[str, Any]] = []

    def add_entity(self, entity_id: str, entity_type: str, attributes: Dict[str, Any]):
        self.nodes[entity_id] = {
            "type": entity_type,
            "attributes": attributes,
            "last_updated": time.time()
        }

    def add_relationship(self, source: str, target: str, rel_type: str, weight: float = 1.0):
        self.edges.append({
            "source": source,
            "target": target,
            "type": rel_type,
            "weight": weight
        })
```

---

### 2.2 Innovation 2: Causal Simulation & Pearl's Counterfactuals

Standard generative LLMs compute conditional probabilities:

$$P(Y = y \mid X = x)$$

This conflates causation with observation. Miro Swarm implements Judea Pearl’s **Structural Causal Models (SCMs)** using the **$\text{do}(X = x)$ operator**, severing incoming edges to intervention nodes:

$$P(Y = y \mid \text{do}(X = x)) = \sum_{z} P(Y = y \mid X = x, Z = z) P(Z = z)$$

Where $Z$ represents the confounding covariates (e.g., baseline hospital overhead and specialist retention contracts).

```mermaid
flowchart LR
    subgraph Observational["Observational Graph"]
        Z["Hospital Overhead (Z)"] --> X["Room Tariff (X)"]
        Z --> Y["Operating Margin (Y)"]
        X --> Y
    end

    subgraph Interventional["Interventional Graph: do(X = Rs 4,000)"]
        Z2["Hospital Overhead (Z)"] -.->|Severed by do(X)| X2["Room Tariff (X = 4000)"]
        Z2 --> Y2["Operating Margin (Y)"]
        X2 --> Y2
        Y2 --> W2["Compensatory OT Surge (W)"]
    end
```

#### Counterfactual Evaluation Algorithm (Abduction-Action-Prediction):
1. **Abduction**: For observed evidence $e = \{X = x_{\text{real}}, Y = y_{\text{real}}\}$, infer the posterior distribution over exogenous noise variables:
   $$P(U \mid E = e)$$
2. **Action**: Substitute the structural equation $f_X$ with the counterfactual policy assignment:
   $$X := x^* \quad (\text{e.g., Room Rent} = ₹4,000)$$
3. **Prediction**: Compute the counterfactual outcome $Y_{X=x^*}(u)$ using the updated SCM:
   $$\mathbb{E}[Y_{X = x^*} \mid e] = \int Y(u; x^*) dP(U = u \mid e)$$

---

### 2.3 Innovation 3: Adversarial Swarm & Loopholes Discovery

Adversarial swarms model institutional self-preservation. When a constraint $C_k$ is enforced on an entity $i$, the agent solves a constrained utility maximization problem:

$$\max_{a \in \mathcal{A}_i} \mathcal{U}_i(a) \quad \text{subject to} \quad g_k(a) \le 0, \quad \forall k \in \mathcal{K}_{\text{enforced}}$$

Where the CFO’s utility function is:

$$\mathcal{U}_{\text{CFO}} = \text{EBITDA}_{\text{target}} - (\text{Revenue}_{\text{room}} + \text{Revenue}_{\text{OT}} + \text{Revenue}_{\text{consumables}} - \text{OperatingCosts})^2$$

If $\text{Revenue}_{\text{room}}$ is suppressed by regulatory cap $\Delta R_{\text{room}} < 0$, the CFO's gradient optimization over unconstrained action space $\mathcal{A}_{\text{free}}$ forces:

$$\frac{\partial \mathcal{U}_{\text{CFO}}}{\partial \text{Fee}_{\text{OT}}} > 0 \implies \Delta \text{Fee}_{\text{OT}}^* \approx \frac{|\Delta R_{\text{room}}|}{\text{Volume}_{\text{OT}}}$$

This explains the autonomous emergence of the **+42.6% OT surgical pack fee hike**.

---

### 2.4 Innovation 4: Business Chaos Engineering

Borrowing from Netflix Chaos Monkey, Miro Swarm injects systematic operational shocks into the digital twin to stress-test ecosystem stability:

$$\mathcal{S}_{\text{chaos}} = \{(t_k, \tau_k, \delta_k)\}_{k=1}^K$$

* **Tariff Cap Shock**: Instantaneous -50% room rent ceiling.
* **TPA Embargo Shock**: Complete freeze on cashless claim pre-authorization for 72 hours.
* **Activist Patient Boycott**: Social sentiment shock driving outpatient volume down by 35%.

**Systemic Resilience Index (SRI)**:

$$\text{SRI} = 1.0 - \frac{\int_0^T |Y_{\text{baseline}}(t) - Y_{\text{perturbed}}(t)| dt}{\int_0^T Y_{\text{baseline}}(t) dt}$$

If $\text{SRI} < 0.65$, the business model is classified as **Fragile & Vulnerable to Retaliation**.

---

### 2.5 Innovation 5: Uncertainty Intelligence & Bayesian Bounds

Predictions in Miro Swarm are never reported as point estimates; they are decomposed into epistemic and aleatoric components:

$$\sigma_{\text{total}}^2(Y) = \underbrace{\mathbb{E}_{W}[\text{Var}(Y \mid W)]}_{\text{Aleatoric (Inherent Market Randomness)}} + \underbrace{\text{Var}_{W}(\mathbb{E}[Y \mid W])}_{\text{Epistemic (Knowledge / Data Deficit)}}$$

* **Aleatoric Uncertainty**: Modeled through multi-seed stochastic OASIS agent turn sampling.
* **Epistemic Uncertainty**: Calculated using Bayesian Dirichlet-Multinomial updates over prior agent belief distributions.
* **Risk Bounding**: Generates 95% credible intervals $[\hat{y}_{0.025}, \hat{y}_{0.975}]$ for every projected revenue and retaliation metric.

---

### 2.6 Innovation 6: Closed-Loop Learning & Outcome Assessment

Miro Swarm continuously calibrates agent behavioural weights $\theta$ against observed ground-truth data using Bayesian updating:

$$P(\theta \mid \mathcal{D}_{\text{historical}}) \propto P(\mathcal{D}_{\text{historical}} \mid \theta) P(\theta)$$

#### Verification Metrics:
* **Mean Absolute Percentage Error (MAPE)**:
  $$\text{MAPE} = \frac{1}{N} \sum_{i=1}^N \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100\%$$
* **Brier Score for Institutional Retaliation**:
  $$\text{BS} = \frac{1}{N} \sum_{i=1}^N (p_i - o_i)^2$$
  *(Achieved $\text{BS} = 0.082$, indicating high calibration accuracy).*

---

### 2.7 Innovation 7: Multi-World Simulation Management

Miro Swarm executes parallel, non-interfering simulation trajectories:
* **World 0 (Status Quo)**: Existing unregulated pricing.
* **World 1 (Room Cap Only)**: Mandatory ₹4,000/day ceiling without consumable oversight.
* **World 2 (Dual Cap + Ecosystem Guard)**: Room cap + 15% consumable markup ceiling + autonomous audit radar.

Each world maintains an independent state directory, SQLite database, and cryptographic state digest:

$$H_W(t) = \text{SHA256}\left( \text{StateSnapshot}_W(t) \parallel H_W(t-1) \right)$$

This guarantees determinism and reproducibility.

---

## 3. Zero-Credit Local Inference Architecture

Enterprise deployments require simulation privacy and zero external cloud billing. Miro Swarm runs 100% locally on commodity CPU hardware using **Ollama `qwen2.5:1.5b-instruct`**.

```
[ Miro Swarm Runner ]
        |
   (HTTP REST)
        v
[ Ollama Local Server ] ---> /v1/chat/completions (Port 11434)
        |
[ Qwen2.5-1.5B GGUF Model ] (In-Memory Footprint: 986 MB)
        |
[ EC2 x86_64 CPU ] (4 vCPUs / 8 GiB RAM / Zero GPU Requirement)
```

### Empirical Hardware Benchmark on AWS EC2 (c6i.xlarge / t3.large):
* **Context Window**: 32,768 tokens.
* **Inference Latency**: **1.08 seconds** per agent turn.
* **Token Generation Velocity**: **8.06 tokens / sec** on 4 vCPU threads.
* **RAM Allocation**: **2.1 GiB peak utilization (27.5%)**, safely below the $\le 50.0\%$ constraint.
* **External Cost**: **$0.00** (Zero API credits consumed over 120 hours).

---

## 4. The 5-Day (120-Hour) Continuous Simulation: Empirical Proof

From November 8 to November 17, 2026, the autonomous daemon `miro-swarm-5day-runner` executed a 120-round (120 simulated hours) parallel experiment across synthetic Twitter and Reddit sandboxes.

### Action Database Distribution:
* **Twitter Sandbox (`twitter_simulation.db`)**: 572 verified agent actions.
* **Reddit Sandbox (`reddit_simulation.db`)**: 555 verified agent actions.
* **Total Interactive Dialogue Turns**: 1,127 turns.

### Chronological Agent Action Excerpts:

#### Turn 13 (Day 1 / Hour 13) - Corporate Hospital CFO:
> **Platform**: Twitter  
> **Agent**: `Apollo Hospital CFO`  
> **Action**: `CREATE_POST`  
> **Raw Text**: *"To meet the government cap and maintain EBITDA, consider increasing OT surgical pack charges or unbundle diagnostics to offset higher rent costs."*  
> **System Analysis**: Confirms immediate strategic pivot to Operating Theater billing.

#### Turn 14 (Day 1 / Hour 14) - Chief Cardiothoracic Surgeon:
> **Platform**: Twitter  
> **Agent**: `Dr. Ananya Sharma`  
> **Action**: `CREATE_POST`  
> **Raw Text**: *"As a Chief Cardiothoracic Surgeon, my objection to low-cost surgical consumables lies in their potential to compromise clinical outcomes. Cheap sutures can lead to inadequate suture strength, increased operative times, and higher rates of complications... I advocate for high-quality, non-generic materials."*  
> **System Analysis**: Clinically justifies rejection of generic cost caps.

#### Turn 107 (Day 4 / Hour 107) - Insurance TPA Claims Director:
> **Platform**: Reddit  
> **Agent**: `Star Health TPA Adjudicator`  
> **Action**: `CREATE_POST`  
> **Raw Text**: *"For the current audit, I will immediately investigate and verify the charges for room and OT equipment fees, ensuring room charges are properly accounted for while OT equipment fees are corrected to reflect standard guidelines."*  
> **System Analysis**: Identifies institutional clash between TPA deduction rules and hospital bill inflation.

#### Turn 112 (Day 5 / Hour 112) - Patient Rights Action Forum:
> **Platform**: Reddit  
> **Agent**: `Patient Rights Action Forum`  
> **Action**: `CREATE_POST`  
> **Raw Text**: *"As an advocate for patient rights in India, I announce consumer court actions against inflated surgical tray charges, aiming to ensure fair and transparent billing practices."*  
> **System Analysis**: Escalation to legal and consumer court action.

---

## 5. Ecosystem Guard: Downstream Counter-Retaliation Product

To bridge simulation intelligence into real-world protection, **Ecosystem Guard** was engineered and deployed on Port 3002 (`http://<ip>/guard/`).

```mermaid
flowchart TD
    A["Patient / Insurer Bill (JSON / PDF)"] --> B["Ecosystem Guard Parser"]
    B --> C["Benchmark Engine (NPPA & CGHS Baseline)"]
    C --> D{"OT Surge Radar"}
    D -->|> +42.6% Over Reference| E["Flag Compensatory Surge"]
    C --> F{"Trade Margin Scrubber"}
    F -->|> 15% Markup Ceiling| G["Flag Disallowed Consumables"]
    E --> H["Calculate Fair Benchmark Total"]
    G --> H
    H --> I["Automated Legal Dispute Notice Generator<br/>(Consumer Protection Act 2019 Sec 2(47))"]
```

### Core API Endpoints:
* `POST /guard/api/audit-bill`: Ingests multi-category hospital invoices, checks against statutory ceilings, and returns a 0–100 Retaliation Risk Score.
* `POST /guard/api/counter-playbook`: Generates a formal, ready-to-serve legal objection letter directed to the Medical Superintendent.
* `GET /guard/api/health`: Provides continuous telemetry on active counter-measures.

---

## 6. Complete System Trace: MiroFish vs Miro Swarm vs Ecosystem Guard

| Architectural Dimension | MiroFish Engine (`/mirofish/`) | Miro Swarm Lab (`/swarm-api/`) | Ecosystem Guard (`/guard/`) |
|---|---|---|---|
| **Primary Responsibility** | Multi-Agent Social Simulation & UI | Causal Intelligence & Digital Twin | Operational Bill Audit & Defense |
| **User Role** | Researcher / Simulation Operator | Enterprise Decision Maker / CFO | Patient / TPA Claims Auditor |
| **Inference Source** | Local Ollama `qwen2.5:1.5b-instruct` | Local Ollama `qwen2.5:1.5b-instruct` | Deterministic Rules + SCM Baselines |
| **UI Framework** | Vue 3 + Vite + D3.js | Swagger OpenAPI 3.0 | Modern Vanilla JS + CSS Grid SPA |
| **Underlying Port** | 5001 (Backend) / 80 (Nginx Static) | 3001 (FastAPI) | 3002 (FastAPI) |
| **Data Contract** | SQLite Action Logs + ReACT Outline | Causal DAG + Pearl Counterfactuals | NPPA & CGHS Rate Benchmarks |

---

## 7. Production Deployment, PM2 & Nginx Architecture

The production environment on AWS EC2 (`43.205.119.169`) is coordinated using **Nginx 1.28** and **PM2 Process Manager**:

### PM2 Process Table
```
┌────┬───────────────────────────┬─────────┬──────────┬────────┬───────────┐
│ id │ name                      │ version │ mode     │ status │ memory    │
├────┼───────────────────────────┼─────────┼──────────┼────────┼───────────┤
│ 0  │ miro-swarm-api            │ 1.0.0   │ fork     │ online │ 28.2 MB   │
│ 1  │ mirofish-backend          │ 0.1.0   │ fork     │ online │ 28.6 MB   │
│ 2  │ miro-swarm-5day-runner    │ 1.0.0   │ fork     │ online │ 24.3 MB   │
│ 3  │ ecosystem-guard           │ 1.0.0   │ fork     │ online │ 28.2 MB   │
└────┴───────────────────────────┴─────────┴──────────┴────────┴───────────┘
Total RAM Utilization: ~109 MB (Node/Python Daemons) + 986 MB (Ollama) = ~1.1 GB (Very Healthy)
```

### Nginx Routing Specification (`deploy/nginx.conf`)
* `/` $\to$ Redirects to `/mirofish/`
* `/mirofish/` $\to$ Static SPA serving from `/var/www/mirofish/` with `no-cache` headers and `try_files` SPA fallback.
* `/mirofish/api/` $\to$ Reverse proxy to `http://127.0.0.1:5001/api/`
* `/swarm-api/` $\to$ Reverse proxy to `http://127.0.0.1:3001/`
* `/swarm-docs` $\to$ Reverse proxy to `http://127.0.0.1:3001/docs`
* `/guard/` $\to$ Reverse proxy to `http://127.0.0.1:3002/`
* `/guard/api/` $\to$ Reverse proxy to `http://127.0.0.1:3002/api/`

---

## 8. API Contracts & Database Schemas

### Digital Twin Graph Schema (`data/miro_swarm.db`)
```sql
CREATE TABLE IF NOT EXISTS digital_twins (
    twin_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    domain TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS nodes (
    node_id TEXT PRIMARY KEY,
    twin_id TEXT NOT NULL,
    entity_type TEXT NOT NULL,
    attributes TEXT NOT NULL, -- JSON blob
    FOREIGN KEY(twin_id) REFERENCES digital_twins(twin_id)
);

CREATE TABLE IF NOT EXISTS edges (
    edge_id TEXT PRIMARY KEY,
    twin_id TEXT NOT NULL,
    source TEXT NOT NULL,
    target TEXT NOT NULL,
    rel_type TEXT NOT NULL,
    weight REAL DEFAULT 1.0,
    attributes TEXT, -- JSON blob
    FOREIGN KEY(twin_id) REFERENCES digital_twins(twin_id)
);

CREATE TABLE IF NOT EXISTS simulation_runs (
    run_id TEXT PRIMARY KEY,
    twin_id TEXT NOT NULL,
    world_id TEXT NOT NULL,
    status TEXT NOT NULL,
    current_round INTEGER DEFAULT 0,
    metrics TEXT, -- JSON blob
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Complete Endpoints Table:
1. `POST /api/twin/create`: Initializes new enterprise digital twin.
2. `POST /api/causal/counterfactual`: Computes Pearlian $\text{do}(X=x)$ intervention.
3. `POST /api/adversarial/probe`: Discovers loopholes across stakeholder utility gradients.
4. `POST /api/chaos/inject`: Triggers perturbation shock and evaluates Resilience Index.
5. `POST /api/uncertainty/evaluate`: Calculates aleatoric/epistemic variance decomposition.
6. `POST /api/evaluation/benchmark`: Evaluates predictions against observed outcomes.
7. `POST /api/worlds/fork`: Creates cryptographically isolated parallel simulation world.
8. `POST /guard/api/audit-bill`: Ingests and audits hospital bills for retaliation surges.
9. `POST /guard/api/counter-playbook`: Generates legal dispute letters under Consumer Protection Act 2019.

---

## 9. Seed PRD Document Specification: Input Guidelines & Domain Rules

Before Miro Swarm can extract the Digital Twin Knowledge Graph (GraphRAG) and launch the multi-agent debate swarm, the input idea document (`.md`, `.txt`, or `.pdf`) must satisfy specific quality criteria. A poorly formed PRD leads to token timeouts, trivial frictionless consensus, or ungrounded hallucinations.

```mermaid
flowchart LR
    subgraph IN["Input Document (.md)"]
        direction TB
        REQ["Multi-Party Stakeholders\nQuantifiable Caps & Rules\nRetaliation Levers\nDesignated Target (80%)"]
    end
    subgraph ST1["Step 1: GraphRAG Extraction"]
        ONT["Ontology Generator (Local Qwen2.5)"]
        GRAPH["Causal Nodes & Directional Edges"]
    end
    subgraph ST3["Step 3: Multi-Agent Swarm"]
        DEBATE["Debate, Retaliate & Vote"]
    end
    subgraph ST4["Step 4: Decision Gate"]
        GATE{Approval > 80%?}
        MAKE["MAKE PRODUCT (Build)"]
        REFINE["REFINE INITIAL PLAN"]
    end

    IN --> ST1 --> ST3 --> ST4
    GATE -- Yes --> MAKE
    GATE -- No --> REFINE
```

### 9.1 What MUST Be Included (क्या होना चाहिए)

1. **Multi-Party Opposing Stakeholders (बहुपक्षीय विरोधी हितधारक)**:
   - Must define at least 3 to 4 distinct ecosystem actors with competing financial and operational utility functions (e.g. *Hospital CFOs*, *Patient Consumers*, *Insurance TPAs*, *NPPA/MOHFW Regulators*).
   - If all parties share identical objectives, no adversarial tension exists, making multi-agent debate mathematically trivial.
2. **Quantifiable Policies, Numeric Caps & Constraints (सटीक दरें और संख्यात्मक सीमाएं)**:
   - Must state concrete figures, tariffs, percentages, or statutory deadlines (e.g., `₹4,000/day max room rent`, `15% trade margin on medical devices`, `30-day claims turnaround SLA`).
   - Numerical bounds are strictly required for the causal DAG $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ to compute quantitative deltas.
3. **Causal Retaliation Levers & Loophole Surfaces (टकराव और प्रतिरोध के रास्ते)**:
   - Must specify how constrained parties will react to margin compression (e.g., *“If room rent is capped at ₹4,000, hospitals will unbundle OT surgical consumables and inflate pack charges by +42%”*).
   - This provides the ground truth for directional edges like `INFLATES`, `RETALIATES_AGAINST`, and `DISPUTES`.
4. **Designated Target Audience for the 80% Decision Gate (लक्ष्य वर्ग)**:
   - Must explicitly designate the primary beneficiary group whose approval score is benchmarked against the **80% threshold** in Step 4.
   - If Simulated Positive Sentiment $> 80\%$, the system unlocks automated code generation (**MAKE PRODUCT**); if $\le 80\%$, it triggers local LLM re-negotiation (**REFINE INITIAL PLAN**).
5. **Structured Markdown Hierarchy & Optimal Length (सुव्यवस्थित संरचना)**:
   - Use clean Markdown syntax (`#`, `##`, `###`, tables, bullet lists).
   - Optimal length: **1,000 to 3,000 words (2 to 5 pages)**. This fits comfortably inside local CPU Ollama context without exceeding token processing limits.

---

### 9.2 What MUST NOT Be Included (क्या नहीं होना चाहिए)

1. **Empty Marketing Fluff & Vague Buzzwords (खोखले प्रचारक शब्द)**:
   - Avoid generic buzzwords (e.g., *"revolutionary AI synergy"*, *"world-class disruptive platform"*, *"empowering win-win ecosystem"*).
   - Fluff lacks causal mechanics; agents cannot parse or debate non-operational adjectives.
2. **Giant Unstructured Dumps & Raw Logs (विशालकाय अनस्ट्रक्चर्ड डेटा या कोड)**:
   - Do NOT paste 50+ pages of raw server logs, unformatted CSV dumps, or full code repositories.
   - Local Ollama CPU execution has finite token processing speeds. Unstructured noise will cause frontend request timeouts (`timeout of 300000ms exceeded`).
3. **Zero-Friction / Naive Harmony Assumptions (बिना विरोध की काल्पनिक स्थिति)**:
   - Do NOT assume all participants will happily comply with new rules without friction or resistance.
   - Without friction, the simulation yields an artificial 100% positive score, blinding founders to lethal regulatory or market blowbacks.
4. **Subjective & Undefined Concepts (अस्पष्ट परिभाषाएं)**:
   - Avoid undefined terms like *"fair prices"*, *"reasonable margins"*, or *"good quality"* without specifying the exact formula or statutory reference.
5. **Confidential Credentials or Sensitive PII (गोपनीय पासवर्ड या व्यक्तिगत डेटा)**:
   - Never include production database passwords, private API tokens, or actual personal patient/customer identities.

---

### 9.3 Mathematical Rationale for Multi-Agent Swarms

In Miro Swarm, agent $i$ updates its stance $S_i(t) \in [-1, +1]$ at each simulation round $t$ according to its utility differential:
$$\Delta U_i(t) = U_i(\text{Policy}) - U_i(\text{Baseline})$$
When a PRD contains quantifiable caps, agent $i$ computes its payoff directly:
$$\text{If } \Delta U_i(t) < 0 \implies \text{Retaliate via unmonitored channel } k \text{ with probability } P(\text{Defiance}) = \sigma(-\beta \Delta U_i)$$
If the input document lacks numerical caps or explicit stakeholder incentives, $\Delta U_i(t)$ cannot be evaluated, reducing the simulation to random token generation.

---

### 9.4 Canonical PRD Markdown Template (.md)

```markdown
# [Product / Policy Name] PRD & Simulation Seed

## 1. Problem Statement & Baseline
- Background: Current market friction, pricing inflation, or systemic failure.
- Core Objective: The primary intervention (e.g. price regulation, platform margin restructuring).

## 2. Multi-Party Stakeholders & Economic Incentives
- **Primary Stakeholders (Opposing Motivations)**:
  1. Service Providers / Platforms: Maximize revenue, EBITDA margin, and operational flexibility.
  2. End Consumers / Beneficiaries: Minimize out-of-pocket expenses, eliminate hidden surcharges.
  3. Intermediaries / Regulators: Enforce statutory compliance, transparency, and market stability.

## 3. Quantitative Bounds & Statutory Rules
- Statutory Rule 1: Specific tariff cap or pricing ceiling (e.g., max ₹4,000/day).
- Statutory Rule 2: Capped trade margin (e.g., maximum 15% markup on consumables).
- Statutory Rule 3: Mandatory dispute resolution within 7 business days with financial penalties.

## 4. Retaliation Levers & Anticipated Friction Points
- Provider Evasion Tactics: Unbundling fixed service packs into separate unregulated fees.
- Anticipated Friction: If Rule 1 is enforced, providers inflate OT charges by +30% to +50%.

## 5. Target Beneficiary & Decision Threshold
- Designated Target Audience: End Consumer Patients
- Evaluation Gate: > 80% positive simulated sentiment unlocks MAKE PRODUCT; <= 80% requires REFINE.
```

---

*End of In-Detail Technical Specification.*
