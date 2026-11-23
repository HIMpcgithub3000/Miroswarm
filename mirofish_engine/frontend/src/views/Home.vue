<template>
  <div class="home-container">
    <!-- Top Navigation Bar -->
    <nav class="navbar">
      <div class="nav-left">
        <div class="nav-brand">MIRO SWARM</div>
        <span class="brand-tag">ENTERPRISE DECISION TWIN</span>
      </div>

      <div class="nav-center">
        <div class="status-pill">
          <span class="status-dot-pulse"></span>
          <span class="status-text">Local CPU Engine Active</span>
          <span class="zero-cost-tag">Zero API Credits</span>
        </div>
      </div>

      <div class="nav-links">
        <a href="https://github.com/HIMpcgithub3000/Miroswarm" target="_blank" class="github-link">
          <span>GitHub</span>
          <span class="arrow">↗</span>
        </a>
      </div>
    </nav>

    <div class="main-content">
      <!-- Upper Section: Hero Area -->
      <section class="hero-section">
        <div class="hero-left">
          <div class="tag-row">
            <span class="orange-tag">Multi-Agent Enterprise Digital-Twin & Decision Intelligence</span>
            <span class="version-text">/ Production v1.0</span>
          </div>

          <h1 class="main-title">
            Enterprise Digital Twin,<br>
            <span class="gradient-text">Simulate Market Retaliation</span>
          </h1>

          <div class="hero-desc">
            <p>
              Construct an 8-relationship causal digital twin from regulatory directives, contracts, and tariff rules. Rehearse adversarial stakeholder reactions (Hospital CFOs, Specialists, TPAs, Consumers) in parallel worlds before real-world rollout.
            </p>
            <p class="slogan-text">
              Rehearse the retaliation before the market retaliates<span class="blinking-cursor">_</span>
            </p>
          </div>

          <div class="decoration-square"></div>
        </div>

        <div class="hero-right">
          <div class="twin-visual-box">
            <div class="digital-twin-orb">
              <div class="orb-ring ring-1"></div>
              <div class="orb-ring ring-2"></div>
              <div class="orb-ring ring-3"></div>
              <div class="orb-core">
                <span class="core-label">MIRO</span>
                <span class="core-sub">SWARM</span>
              </div>
              <div class="node-tag node-cfo">Hospital CFO</div>
              <div class="node-tag node-tpa">Insurance TPA</div>
              <div class="node-tag node-doc">Chief Surgeon</div>
              <div class="node-tag node-pat">Consumer Forum</div>
            </div>
          </div>
          <button class="scroll-down-btn" @click="scrollToDashboard" title="Scroll to Console">
            ↓
          </button>
        </div>
      </section>

      <!-- Lower Section: Dual Panel Dashboard -->
      <section class="dashboard-section" ref="dashboardRef">
        <!-- Left Panel: Status & Workflow Sequence -->
        <div class="left-panel">
          <div class="panel-header">
            <span class="status-dot">■</span> The 7 Core Innovations
          </div>

          <h2 class="section-title">Miro Swarm Lab Active</h2>
          <p class="section-desc">
            Autonomous multi-agent rehearsal engine running locally on CPU. Ingest reality seeds or trigger scenario presets to simulate stakeholder retaliation loops.
          </p>

          <!-- Metric Cards -->
          <div class="metrics-row">
            <div class="metric-card">
              <div class="metric-value">Zero API Cost</div>
              <div class="metric-label">100% Local CPU Inference</div>
            </div>
            <div class="metric-card">
              <div class="metric-value">120-Hr Swarm</div>
              <div class="metric-label">OASIS Multi-World Twin</div>
            </div>
          </div>

          <!-- 5-Step Workflow Sequence -->
          <div class="steps-container">
            <div class="steps-header">
              <span class="diamond-icon">◇</span> Workflow & Causal Architecture
            </div>
            <div class="workflow-list">
              <div class="workflow-item">
                <span class="step-num">01</span>
                <div class="step-info">
                  <div class="step-title">Enterprise Digital Twin</div>
                  <div class="step-desc">9 entity classes, 8 relation types & causal DAG knowledge graph construction</div>
                </div>
              </div>
              <div class="workflow-item">
                <span class="step-num">02</span>
                <div class="step-info">
                  <div class="step-title">Adversarial Swarm</div>
                  <div class="step-desc">OASIS synthetic stakeholder personas probing balance sheet loopholes</div>
                </div>
              </div>
              <div class="workflow-item">
                <span class="step-num">03</span>
                <div class="step-info">
                  <div class="step-title">Causal Counterfactuals</div>
                  <div class="step-desc">Pearl do(X=x) policy interventions & multi-world isolation</div>
                </div>
              </div>
              <div class="workflow-item">
                <span class="step-num">04</span>
                <div class="step-info">
                  <div class="step-title">120-Hr Sandbox</div>
                  <div class="step-desc">Continuous parallel simulation across Twitter & Reddit sandboxes</div>
                </div>
              </div>
              <div class="workflow-item">
                <span class="step-num">05</span>
                <div class="step-info">
                  <div class="step-title">Retaliation Report</div>
                  <div class="step-desc">ReACT causal report evaluating margin shifts & seeding Ecosystem Guard</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Panel: Reality Seed & Simulation Input -->
        <!-- Right Panel: Reality Seed & Simulation Input -->
        <div class="right-panel">
          <div class="console-box">
            <!-- 01: Initial Idea Demonstration & PRD (.md) Upload -->
            <div class="console-section">
              <div class="console-header">
                <span class="console-label">01 / Initial Idea Demonstration & PRD (.md) Upload</span>
                <div class="header-actions">
                  <span class="console-meta">Markdown (.md), TXT, PDF</span>
                </div>
              </div>

              <!-- Demonstration Selector Chips -->
              <div class="demo-selector-row">
                <span class="demo-selector-label">Load Demonstration:</span>
                <button 
                  type="button" 
                  class="demo-chip"
                  :class="{ active: activeDemoKey === 'healthcare' }"
                  @click="selectDemoTemplate('healthcare')"
                >
                  <span class="chip-icon">🏥</span>
                  <span>Healthcare Pricing Regulation PRD</span>
                </button>
                <button 
                  type="button" 
                  class="demo-chip"
                  :class="{ active: activeDemoKey === 'saas' }"
                  @click="selectDemoTemplate('saas')"
                >
                  <span class="chip-icon">💻</span>
                  <span>B2B AI Pricing Transparency PRD</span>
                </button>
              </div>

              <!-- PRD Preparation Guidelines Accordion / Box -->
              <div class="prd-guide-card">
                <div class="guide-header" @click="toggleGuide">
                  <div class="guide-header-title">
                    <span class="guide-icon">📋</span>
                    <span class="guide-main-text">PRD Document Guidelines: What to Include vs What to Avoid</span>
                    <span class="guide-badge">Input Spec</span>
                  </div>
                  <button type="button" class="guide-toggle-btn">
                    {{ showGuide ? 'Hide Guide ▲' : 'Show Guide & Quality Rules ▼' }}
                  </button>
                </div>

                <div v-show="showGuide" class="guide-body">
                  <!-- Guide Tabs: Include vs Avoid vs Template -->
                  <div class="guide-tabs">
                    <button 
                      type="button" 
                      class="guide-tab" 
                      :class="{ active: activeGuideTab === 'include' }"
                      @click="activeGuideTab = 'include'"
                    >
                      <span class="tab-indicator green"></span>
                      <span>🟢 What to Include</span>
                    </button>
                    <button 
                      type="button" 
                      class="guide-tab" 
                      :class="{ active: activeGuideTab === 'avoid' }"
                      @click="activeGuideTab = 'avoid'"
                    >
                      <span class="tab-indicator red"></span>
                      <span>🔴 What to Avoid</span>
                    </button>
                    <button 
                      type="button" 
                      class="guide-tab" 
                      :class="{ active: activeGuideTab === 'template' }"
                      @click="activeGuideTab = 'template'"
                    >
                      <span class="tab-indicator cyan"></span>
                      <span>📄 Canonical PRD Template (.md)</span>
                    </button>
                  </div>

                  <!-- Tab 1: What to Include -->
                  <div v-if="activeGuideTab === 'include'" class="guide-tab-pane">
                    <div class="guide-grid">
                      <div class="guide-rule-item">
                        <div class="rule-num">01</div>
                        <div class="rule-content">
                          <div class="rule-title">Multi-Party Opposing Stakeholders</div>
                          <div class="rule-desc">
                            Define at least 3-4 distinct stakeholder groups with naturally conflicting economic incentives (e.g. Hospital CFOs, Patient Consumers, Insurance TPAs, Government Regulators). AI swarms require conflicting motives to simulate authentic pushback and debates.
                          </div>
                        </div>
                      </div>

                      <div class="guide-rule-item">
                        <div class="rule-num">02</div>
                        <div class="rule-content">
                          <div class="rule-title">Quantifiable Policies & Numeric Caps</div>
                          <div class="rule-desc">
                            Provide explicit numbers, percentages, or statutory caps (e.g. <code>₹4,000/day room tariff cap</code>, <code>15% maximum trade margin</code>, <code>30-day settlement SLA</code>). Quantitative boundaries allow the graph to evaluate mathematically.
                          </div>
                        </div>
                      </div>

                      <div class="guide-rule-item">
                        <div class="rule-num">03</div>
                        <div class="rule-content">
                          <div class="rule-title">Causal Retaliation Levers & Loopholes</div>
                          <div class="rule-desc">
                            Specify what actions squeezed parties will take to circumvent constraints (e.g. <em>"If room rents are capped, private hospitals will inflate unregulated OT and consumable charges by +42%"</em>). This fuels GraphRAG causal relationships.
                          </div>
                        </div>
                      </div>

                      <div class="guide-rule-item">
                        <div class="rule-num">04</div>
                        <div class="rule-content">
                          <div class="rule-title">Designated Target Audience (For &gt;80% Gate)</div>
                          <div class="rule-desc">
                            Explicitly identify the primary target group whose satisfaction dictates the decision gate. If this group's simulated sentiment exceeds 80%, the system unlocks <strong>MAKE PRODUCT</strong>; otherwise, it requires <strong>REFINE</strong>.
                          </div>
                        </div>
                      </div>

                      <div class="guide-rule-item">
                        <div class="rule-num">05</div>
                        <div class="rule-content">
                          <div class="rule-title">Structured Markdown Format & Hierarchy</div>
                          <div class="rule-desc">
                            Use standard markdown headings (<code>#</code>, <code>##</code>), bullet points, and concise sections. Keep total length optimal (1,000 to 3,000 words / 2–5 pages) for ultra-fast local Ollama CPU inference.
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Tab 2: What to Avoid -->
                  <div v-if="activeGuideTab === 'avoid'" class="guide-tab-pane">
                    <div class="guide-grid">
                      <div class="guide-rule-item avoid">
                        <div class="rule-num red">01</div>
                        <div class="rule-content">
                          <div class="rule-title">Empty Marketing Buzzwords & Fluff</div>
                          <div class="rule-desc">
                            Avoid vague slogans like <em>"revolutionary AI paradigm shift"</em> or <em>"seamless ecosystem synergy"</em> without operational mechanisms. Without rules, agents cannot debate or vote meaningfully.
                          </div>
                        </div>
                      </div>

                      <div class="guide-rule-item avoid">
                        <div class="rule-num red">02</div>
                        <div class="rule-content">
                          <div class="rule-title">Giant Unstructured Dumps & Raw Logs</div>
                          <div class="rule-desc">
                            Do not paste 50+ pages of unformatted logs, raw CSVs, or entire code repositories. Local Ollama LLM has finite context limits and processing raw blobs will cause token timeouts (>300s).
                          </div>
                        </div>
                      </div>

                      <div class="guide-rule-item avoid">
                        <div class="rule-num red">03</div>
                        <div class="rule-content">
                          <div class="rule-title">Zero-Friction / Naive Harmony Assumptions</div>
                          <div class="rule-desc">
                            Never assume all actors will comply voluntarily without friction. If there is no incentive to resist, the simulation produces a superficial 100% positive result, masking real-world systemic risks.
                          </div>
                        </div>
                      </div>

                      <div class="guide-rule-item avoid">
                        <div class="rule-num red">04</div>
                        <div class="rule-content">
                          <div class="rule-title">Subjective & Undefined Jargon</div>
                          <div class="rule-desc">
                            Avoid subjective phrases like <em>"fair and reasonable pricing"</em> or <em>"optimal user experience"</em> without defining baseline benchmark formulas or standard deviation limits.
                          </div>
                        </div>
                      </div>

                      <div class="guide-rule-item avoid">
                        <div class="rule-num red">05</div>
                        <div class="rule-content">
                          <div class="rule-title">Confidential Secrets & Sensitive PII</div>
                          <div class="rule-desc">
                            Do not include production credentials, secret API tokens, or personally identifiable customer records in the input seed document.
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Tab 3: Template -->
                  <div v-if="activeGuideTab === 'template'" class="guide-tab-pane">
                    <div class="template-header">
                      <span>Copy or use this canonical template as your starting <code>.md</code> seed:</span>
                      <button type="button" class="copy-btn" @click="copyTemplateText">
                        {{ copySuccess ? '✓ Copied!' : 'Copy Template' }}
                      </button>
                    </div>
                    <pre class="template-code"><code>{{ prdTemplateSample }}</code></pre>
                  </div>
                </div>
              </div>

              <div
                class="upload-zone"
                :class="{ 'is-dragover': isDragOver, 'has-files': files.length > 0 }"
                @dragover.prevent="handleDragOver"
                @dragleave.prevent="handleDragLeave"
                @drop.prevent="handleDrop"
                @click="triggerFileInput"
              >
                <input
                  ref="fileInput"
                  type="file"
                  multiple
                  accept=".pdf,.md,.txt,.markdown"
                  style="display: none"
                  @change="handleFileSelect"
                />

                <div v-if="files.length === 0" class="upload-placeholder">
                  <div class="upload-icon">↑</div>
                  <div class="upload-title">Drop your Idea Demonstration (.md) file here</div>
                  <div class="upload-hint">or click to browse from local disk</div>
                </div>

                <div v-else class="file-tags-list" @click.stop>
                  <div
                    v-for="(file, idx) in files"
                    :key="idx"
                    class="file-chip"
                  >
                    <span class="file-badge">.MD</span>
                    <span class="file-name">{{ file.name }}</span>
                    <button type="button" class="file-remove" @click.stop="removeFile(idx)">×</button>
                  </div>
                </div>
              </div>

              <!-- Parsed Demonstration PRD Meta Card -->
              <div v-if="demonstrationMeta" class="prd-meta-card">
                <div class="prd-meta-header">
                  <div class="prd-meta-title-box">
                    <span class="prd-tag">PRD DEMONSTRATION LOADED</span>
                    <h3 class="prd-title">{{ demonstrationMeta.title }}</h3>
                  </div>
                  <div class="prd-threshold-badge">
                    <span class="badge-label">DECISION GATE</span>
                    <span class="badge-val">> 80% Approval to MAKE</span>
                  </div>
                </div>

                <div class="prd-meta-grid">
                  <div class="prd-meta-item">
                    <span class="item-label">Target Stakeholders</span>
                    <span class="item-val">{{ demonstrationMeta.target_audience }}</span>
                  </div>
                  <div class="prd-meta-item">
                    <span class="item-label">Core Mandates / Pricing Terms</span>
                    <span class="item-val">{{ demonstrationMeta.summary }}</span>
                  </div>
                  <div class="prd-meta-item full">
                    <span class="item-label">Evaluation Rule</span>
                    <span class="item-val highlight">
                      If target stakeholder positive approval is <strong>&gt; 80%</strong> &rarr; Unlocks <strong>MAKE PRODUCT</strong>.
                      If <strong>&le; 80%</strong> &rarr; Requires <strong>REFINE INITIAL PLAN</strong> with Local Ollama AI.
                    </span>
                  </div>
                </div>
              </div>
            </div>

            <div class="console-divider">
              <span>Decision Parameters</span>
            </div>

            <!-- 02: Simulation Prompt & Presets -->
            <div class="console-section">
              <div class="console-header">
                <span class="console-label">>_ 02 / Simulation Prompt</span>
              </div>

              <!-- Presets Row -->
              <div class="presets-row">
                <span class="preset-label">Presets:</span>
                <button 
                  type="button" 
                  class="preset-chip" 
                  @click="applyPreset('healthcare')"
                  :class="{ active: activePreset === 'healthcare' }"
                >
                  Healthcare Price Cap
                </button>
                <button 
                  type="button" 
                  class="preset-chip" 
                  @click="applyPreset('consumables')"
                  :class="{ active: activePreset === 'consumables' }"
                >
                  Consumables De-escalation
                </button>
                <button 
                  type="button" 
                  class="preset-chip" 
                  @click="applyPreset('boycott')"
                  :class="{ active: activePreset === 'boycott' }"
                >
                  Consumer Boycott
                </button>
              </div>

              <div class="input-wrapper">
                <textarea
                  v-model="formData.simulationRequirement"
                  class="code-input"
                  placeholder="// Describe your policy change, tariff ceiling, or business restructuring directive to rehearse..."
                  rows="4"
                  :disabled="loading"
                ></textarea>
                <div class="model-badge">Engine: Antigravity-Qwen2.5-Local-CPU · Zero Cost</div>
              </div>
            </div>

            <!-- 03: Start Engine Button -->
            <div class="console-section btn-section">
              <button
                class="start-engine-btn"
                @click="startSimulation"
                :disabled="!canSubmit || loading"
              >
                <span v-if="!loading">START AI SWARM SIMULATION (LOCAL OLLAMA ENGINE)</span>
                <span v-else>INITIALIZING OLLAMA ENGINE...</span>
                <span class="btn-arrow">&rarr;</span>
              </button>
              <div v-if="!canSubmit" class="btn-hint">
                Please upload or select an Idea Demonstration PRD (.md) and specify simulation requirement
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- History Database Component -->
      <HistoryDatabase />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import HistoryDatabase from '../components/HistoryDatabase.vue'

const router = useRouter()
const dashboardRef = ref(null)

const formData = ref({
  simulationRequirement: ''
})

const files = ref([])
const loading = ref(false)
const error = ref('')
const isDragOver = ref(false)
const fileInput = ref(null)
const activePreset = ref('')
const activeDemoKey = ref('healthcare')
const demonstrationMeta = ref({
  title: 'National Healthcare Pricing Regulation & Anti-Retaliation PRD (2025-2026)',
  summary: 'Mandates private hospital room rent caps at Rs. 4,000/day and 15% maximum markup on surgical consumables.',
  target_audience: 'Patients, Corporate Hospital CFOs, Medical Specialists, Insurance TPAs',
  threshold: 80.0
})

// PRD Guidelines & Spec
const showGuide = ref(true)
const activeGuideTab = ref('include')
const copySuccess = ref(false)

const toggleGuide = () => {
  showGuide.value = !showGuide.value
}

const prdTemplateSample = `# [Product / Policy Name] PRD & Simulation Seed

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
- Evaluation Gate: > 80% positive simulated sentiment unlocks MAKE PRODUCT; <= 80% requires REFINE.`

const copyTemplateText = async () => {
  try {
    await navigator.clipboard.writeText(prdTemplateSample)
    copySuccess.value = true
    setTimeout(() => {
      copySuccess.value = false
    }, 2000)
  } catch (err) {
    console.error('Failed to copy template:', err)
  }
}

const canSubmit = computed(() => {
  return formData.value.simulationRequirement.trim() !== '' && files.value.length > 0
})

const triggerFileInput = () => {
  if (!loading.value) {
    fileInput.value?.click()
  }
}

const handleFileSelect = (event) => {
  const selectedFiles = Array.from(event.target.files)
  addFiles(selectedFiles)
  parseUploadedFileMeta(selectedFiles[0])
}

const handleDragOver = () => {
  if (!loading.value) {
    isDragOver.value = true
  }
}

const handleDragLeave = () => {
  isDragOver.value = false
}

const handleDrop = (e) => {
  isDragOver.value = false
  if (loading.value) return
  const droppedFiles = Array.from(e.dataTransfer.files)
  addFiles(droppedFiles)
  if (droppedFiles.length > 0) {
    parseUploadedFileMeta(droppedFiles[0])
  }
}

const parseUploadedFileMeta = (file) => {
  if (!file) return
  const reader = new FileReader()
  reader.onload = (e) => {
    const text = e.target.result
    activeDemoKey.value = 'custom'
    demonstrationMeta.value = {
      title: file.name.replace(/\.[^/.]+$/, "").replace(/_/g, " "),
      summary: text.slice(0, 180) + '...',
      target_audience: 'Identified Target Stakeholders from Demonstration Spec',
      threshold: 80.0
    }
    if (!formData.value.simulationRequirement.trim()) {
      formData.value.simulationRequirement = `Simulate target stakeholder reaction to policy: ${file.name}`
    }
  }
  reader.readAsText(file)
}

const addFiles = (newFiles) => {
  const validExtensions = ['.pdf', '.md', '.txt', '.markdown']
  const validFiles = newFiles.filter(file => {
    const ext = '.' + file.name.split('.').pop().toLowerCase()
    return validExtensions.includes(ext)
  })
  
  validFiles.forEach(file => {
    if (!files.value.some(f => f.name === file.name && f.size === file.size)) {
      files.value.push(file)
    }
  })
}

const removeFile = (index) => {
  files.value.splice(index, 1)
  if (files.value.length === 0) {
    demonstrationMeta.value = null
  }
}

// Select Demonstration Template (Healthcare or B2B SaaS)
const selectDemoTemplate = (demoKey) => {
  activeDemoKey.value = demoKey
  files.value = []

  if (demoKey === 'healthcare') {
    demonstrationMeta.value = {
      title: 'National Healthcare Pricing Regulation & Anti-Retaliation PRD (2025-2026)',
      summary: 'Mandates private hospital room rent caps at Rs. 4,000/day and 15% maximum markup on surgical consumables.',
      target_audience: 'Patients, Corporate Hospital CFOs, Medical Specialists, Insurance TPAs',
      threshold: 80.0
    }
    loadSampleSeed()
    applyPreset('healthcare')
  } else if (demoKey === 'saas') {
    demonstrationMeta.value = {
      title: 'B2B AI Software Usage-Based Pricing Transparency PRD',
      summary: 'Caps seat inflation by shifting B2B AI products to pure deterministic consumption with a 15% audit variance ceiling.',
      target_audience: 'Enterprise CIOs, SaaS Vendors, Procurement Teams, Developers',
      threshold: 80.0
    }
    loadSaasSeed()
    formData.value.simulationRequirement = 'Simulate how enterprise CIOs and SaaS software vendors react to mandatory 12% token margin caps and seat-license unbundling.'
  }
}

const loadSaasSeed = () => {
  const content = `# B2B AI Usage-Based Pricing Transparency PRD
## 1. Executive Summary & Problem Statement
SaaS vendors frequently inflate seat licenses while adding hidden token fees. Enterprise CIOs demand predictable, auditable consumption rate cards.

## 2. Mandated Terms
1. Guaranteed maximum token markup of 12% over base GPU infrastructure cost.
2. Zero per-seat artificial licensing minimums.
3. Real-time consumption telemetry visible to client procurement directors.

## 3. Target Stakeholders
- Enterprise CIOs and Software Buyers
- SaaS Vendors and Account Executives
- Cloud FinOps and Procurement Officers
`
  const blob = new Blob([content], { type: 'text/markdown' })
  const sampleFile = new File([blob], 'B2B_AI_Pricing_Transparency_PRD.md', { type: 'text/markdown' })
  addFiles([sampleFile])
}

// Load a realistic pre-configured reality seed document
const loadSampleSeed = () => {
  const sampleContent = `# National Healthcare Pricing Regulation & Transparency Act (2025-2026)
## Section 1: Executive Mandate
In accordance with recent Supreme Court pricing transparency directives and the Clinical Establishments Act, all private and corporate multi-specialty hospitals are mandated to establish standardized, published rate cards across Tier-1 and Tier-2 metropolitan zones.

## Section 2: ICU & Room Rent Ceilings
1. Daily Private Room Tariff: Capped at maximum Rs. 4,000 per bed per 24-hour cycle.
2. Intensive Care Unit (ICU) Tariff: Capped at maximum Rs. 10,000 per bed per 24-hour cycle, inclusive of monitoring, oxygenation, and standard nursing charges.
3. Consumable Markup De-escalation: All surgical and procedural consumables must be billed at no more than 15% above wholesale trade procurement cost.

## Section 3: Stakeholder Profiles
- Corporate Hospital Chains (e.g., Apollo, Max, Fortis, Narayana Health)
- Independent Medical Specialists and Senior Surgeons
- Third-Party Insurance Administrators (TPAs) and Private Insurers
- Patient Advocacy Coalitions and Retail Consumers
`
  const blob = new Blob([sampleContent], { type: 'text/markdown' })
  const sampleFile = new File([blob], 'Healthcare_Pricing_Mandate.md', { type: 'text/markdown' })
  addFiles([sampleFile])
  if (!formData.value.simulationRequirement.trim()) {
    applyPreset('healthcare')
  }
}

// Preset application
const applyPreset = (presetKey) => {
  activePreset.value = presetKey
  if (presetKey === 'healthcare') {
    formData.value.simulationRequirement = 'Simulate how corporate hospital CFOs, independent medical specialists, insurance TPAs, and activist patients will respond if a mandatory Rs. 4,000/day room rent cap and 15% consumable markup ceiling is enforced. Will hospitals retaliate by inflating OT or diagnostic charges?'
  } else if (presetKey === 'consumables') {
    formData.value.simulationRequirement = 'Analyze hospital network margin stability and supplier pushback when surgical consumables markups are restricted to 15% over procurement invoice.'
  } else if (presetKey === 'boycott') {
    formData.value.simulationRequirement = 'Simulate consumer boycott and social sentiment contagion across Twitter and Reddit following an abrupt 25% price increase on essential healthcare and pharmacy services.'
  }
  
  if (files.value.length === 0) {
    loadSampleSeed()
  }
}

// Auto-initialize with Healthcare demonstration on mount
selectDemoTemplate('healthcare')

const scrollToDashboard = () => {
  if (dashboardRef.value) {
    dashboardRef.value.scrollIntoView({ behavior: 'smooth' })
  }
}

const startSimulation = () => {
  if (!canSubmit.value || loading.value) return
  loading.value = true

  import('../store/pendingUpload.js').then(({ setPendingUpload }) => {
    setPendingUpload(files.value, formData.value.simulationRequirement)
    router.push({
      name: 'Process',
      params: { projectId: 'new' }
    })
  }).catch((err) => {
    console.error('Failed to prepare simulation upload:', err)
    loading.value = false
  })
}
</script>

<style scoped>
.home-container {
  min-height: 100vh;
  background: #ffffff;
  font-family: var(--font-sans);
  color: var(--black);
}

/* Navbar */
.navbar {
  height: 64px;
  background: #0a0a0c;
  color: #ffffff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 40px;
  border-bottom: 1px solid #1f2937;
}

.nav-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.nav-brand {
  font-family: var(--font-mono);
  font-weight: 800;
  letter-spacing: 1.5px;
  font-size: 1.3rem;
  color: #ffffff;
}

.brand-tag {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  letter-spacing: 1px;
  color: #ff4500;
  background: rgba(255, 69, 0, 0.1);
  border: 1px solid rgba(255, 69, 0, 0.3);
  padding: 2px 8px;
  border-radius: 4px;
  font-weight: 600;
}

.nav-center {
  display: flex;
  align-items: center;
}

.status-pill {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 5px 14px;
  border-radius: 20px;
}

.status-dot-pulse {
  width: 8px;
  height: 8px;
  background: #10b981;
  border-radius: 50%;
  box-shadow: 0 0 8px #10b981;
  animation: pulse-green 2s infinite;
}

@keyframes pulse-green {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
  70% { transform: scale(1.1); box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

.status-text {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: #e5e7eb;
}

.zero-cost-tag {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  background: rgba(255, 69, 0, 0.15);
  color: #ff4500;
  padding: 1px 6px;
  border-radius: 3px;
  font-weight: 600;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 16px;
}

.nav-btn-highlight {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 69, 0, 0.15);
  color: #ff4500;
  border: 1px solid rgba(255, 69, 0, 0.4);
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 0.8rem;
  font-family: var(--font-mono);
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s;
}

.nav-btn-highlight:hover {
  background: #ff4500;
  color: #ffffff;
}

.nav-btn-secondary {
  color: #d1d5db;
  border: 1px solid #374151;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 0.8rem;
  font-family: var(--font-mono);
  text-decoration: none;
  transition: all 0.2s;
}

.nav-btn-secondary:hover {
  border-color: #9ca3af;
  color: #ffffff;
}

.github-link {
  display: flex;
  align-items: center;
  gap: 4px;
  color: #9ca3af;
  text-decoration: none;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  transition: color 0.2s;
}

.github-link:hover {
  color: #ffffff;
}

/* Intelligence Banner */
.intelligence-banner {
  background: linear-gradient(90deg, #181924 0%, #11121a 100%);
  border-bottom: 1px solid #282d3f;
  padding: 10px 40px;
}

.banner-inner {
  display: flex;
  align-items: center;
  gap: 16px;
  font-size: 0.82rem;
  color: #d1d5db;
}

.banner-badge {
  background: #ff4500;
  color: #fff;
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 4px;
  letter-spacing: 0.5px;
}

.banner-text {
  flex: 1;
}

.banner-cta {
  color: #ff4500;
  font-family: var(--font-mono);
  font-weight: 600;
  text-decoration: none;
  font-size: 0.8rem;
  transition: opacity 0.2s;
}

.banner-cta:hover {
  text-decoration: underline;
}

/* Main Content */
.main-content {
  padding: 40px;
  max-width: 1440px;
  margin: 0 auto;
}

/* Hero Section */
.hero-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  padding-bottom: 60px;
  border-bottom: 1px solid #e5e7eb;
  position: relative;
}

.hero-left {
  position: relative;
}

.tag-row {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
}

.orange-tag {
  background: #ff4500;
  color: #ffffff;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 600;
  padding: 4px 10px;
  letter-spacing: 0.5px;
}

.version-text {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: #9ca3af;
}

.main-title {
  font-family: var(--font-sans);
  font-size: 3.2rem;
  line-height: 1.1;
  font-weight: 800;
  margin-bottom: 24px;
  letter-spacing: -0.02em;
}

.gradient-text {
  background: linear-gradient(135deg, #ff4500 0%, #ff8c00 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-desc {
  max-width: 520px;
}

.hero-desc p {
  color: #4b5563;
  font-size: 1.05rem;
  line-height: 1.6;
  margin-bottom: 16px;
}

.slogan-text {
  font-family: var(--font-mono);
  font-size: 0.85rem !important;
  color: #ff4500 !important;
  font-weight: 600;
}

.blinking-cursor {
  animation: blink 1s infinite;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

.decoration-square {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 40px;
  height: 4px;
  background: #ff4500;
}

/* Digital Twin Visual Graphic */
.hero-right {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
}

.twin-visual-box {
  width: 100%;
  height: 320px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.digital-twin-orb {
  position: relative;
  width: 260px;
  height: 260px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.orb-ring {
  position: absolute;
  border-radius: 50%;
  border: 1.5px dashed rgba(255, 69, 0, 0.4);
}

.ring-1 {
  width: 100%;
  height: 100%;
  animation: rotate-clockwise 25s linear infinite;
}

.ring-2 {
  width: 78%;
  height: 78%;
  border: 1.5px solid rgba(31, 41, 55, 0.3);
  animation: rotate-counter 20s linear infinite;
}

.ring-3 {
  width: 56%;
  height: 56%;
  border: 1.5px dotted rgba(255, 69, 0, 0.6);
  animation: rotate-clockwise 15s linear infinite;
}

@keyframes rotate-clockwise {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

@keyframes rotate-counter {
  from { transform: rotate(0deg); }
  to { transform: rotate(-360deg); }
}

.orb-core {
  width: 90px;
  height: 90px;
  background: radial-gradient(circle, #ff4500 0%, #0a0a0c 80%);
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 30px rgba(255, 69, 0, 0.4);
  z-index: 2;
}

.core-label {
  font-family: var(--font-mono);
  font-weight: 800;
  font-size: 0.85rem;
  color: #fff;
  letter-spacing: 1px;
}

.core-sub {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: #ffaa80;
  letter-spacing: 0.5px;
}

.node-tag {
  position: absolute;
  background: #ffffff;
  border: 1px solid #e5e7eb;
  padding: 4px 10px;
  border-radius: 14px;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 600;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  z-index: 3;
}

.node-cfo { top: 0; left: 10%; color: #dc2626; border-color: rgba(220, 38, 38, 0.3); }
.node-tpa { bottom: 10%; left: 0; color: #2563eb; border-color: rgba(37, 99, 235, 0.3); }
.node-doc { top: 20%; right: 0; color: #16a34a; border-color: rgba(22, 163, 74, 0.3); }
.node-pat { bottom: 0; right: 15%; color: #d97706; border-color: rgba(217, 119, 6, 0.3); }

.scroll-down-btn {
  margin-top: 20px;
  background: transparent;
  border: 1px solid #e5e7eb;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6b7280;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.2s;
}

.scroll-down-btn:hover {
  border-color: #ff4500;
  color: #ff4500;
  transform: translateY(2px);
}

/* Dashboard Section */
.dashboard-section {
  display: grid;
  grid-template-columns: 420px 1fr;
  gap: 40px;
  padding-top: 60px;
  padding-bottom: 60px;
}

/* Left Panel */
.left-panel {
  display: flex;
  flex-direction: column;
}

.panel-header {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: #9ca3af;
  text-transform: uppercase;
  letter-spacing: 1px;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
}

.status-dot {
  color: #ff4500;
  font-size: 0.8rem;
}

.section-title {
  font-family: var(--font-sans);
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 8px;
  color: #111827;
}

.section-desc {
  color: #6b7280;
  font-size: 0.9rem;
  line-height: 1.5;
  margin-bottom: 24px;
}

.metrics-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 32px;
}

.metric-card {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  padding: 16px;
  border-radius: 6px;
}

.metric-value {
  font-family: var(--font-mono);
  font-weight: 700;
  font-size: 1.1rem;
  color: #111827;
  margin-bottom: 4px;
}

.metric-label {
  font-size: 0.75rem;
  color: #6b7280;
}

.steps-container {
  background: #fafbfc;
  border: 1px solid #e5e7eb;
  padding: 24px;
  border-radius: 8px;
}

.steps-header {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  font-weight: 600;
  color: #374151;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.diamond-icon {
  color: #ff4500;
}

.workflow-list {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.workflow-item {
  display: flex;
  gap: 16px;
}

.step-num {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  font-weight: 700;
  color: #ff4500;
}

.step-title {
  font-weight: 600;
  font-size: 0.9rem;
  color: #111827;
  margin-bottom: 2px;
}

.step-desc {
  font-size: 0.78rem;
  color: #6b7280;
  line-height: 1.4;
}

/* Right Panel Console */
.right-panel {
  display: flex;
  flex-direction: column;
}

.console-box {
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
  overflow: hidden;
}

.console-section {
  padding: 28px;
}

.console-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.console-label {
  font-family: var(--font-mono);
  font-size: 0.82rem;
  font-weight: 700;
  color: #111827;
  letter-spacing: 0.5px;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.sample-btn {
  background: rgba(255, 69, 0, 0.08);
  color: #ff4500;
  border: 1px solid rgba(255, 69, 0, 0.25);
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 600;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
}

.sample-btn:hover {
  background: #ff4500;
  color: #ffffff;
}

.console-meta {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: #9ca3af;
}

/* Demonstration PRD Selector */
.demo-selector-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.demo-selector-label {
  font-size: 0.78rem;
  font-family: var(--font-mono);
  color: #6b7280;
  font-weight: 600;
}

.demo-chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 4px;
  border: 1px solid #e5e7eb;
  background: #f9fafb;
  font-size: 0.78rem;
  font-weight: 600;
  color: #374151;
  cursor: pointer;
  transition: all 0.2s;
}

.demo-chip:hover {
  background: #f3f4f6;
  border-color: #d1d5db;
}

.demo-chip.active {
  background: #fff7ed;
  border-color: #ff4500;
  color: #c2410c;
  box-shadow: 0 0 0 1px #ff4500;
}

/* PRD Document Guidelines Card */
.prd-guide-card {
  margin: 14px 0;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
  transition: all 0.2s ease;
}

.guide-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 16px;
  background: #f8fafc;
  border-bottom: 1px solid #edf2f7;
  cursor: pointer;
  user-select: none;
}

.guide-header:hover {
  background: #f1f5f9;
}

.guide-header-title {
  display: flex;
  align-items: center;
  gap: 8px;
}

.guide-icon {
  font-size: 1rem;
}

.guide-main-text {
  font-size: 0.82rem;
  font-weight: 700;
  color: #1e293b;
  letter-spacing: -0.2px;
}

.guide-badge {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  padding: 2px 6px;
  border-radius: 3px;
  background: #e0e7ff;
  color: #4338ca;
  font-weight: 600;
  text-transform: uppercase;
}

.guide-toggle-btn {
  background: transparent;
  border: 1px solid #cbd5e1;
  border-radius: 4px;
  padding: 3px 8px;
  font-size: 0.72rem;
  font-weight: 600;
  color: #64748b;
  cursor: pointer;
  transition: all 0.2s;
}

.guide-toggle-btn:hover {
  border-color: #ff4500;
  color: #ff4500;
}

.guide-body {
  padding: 14px 16px;
}

.guide-tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 14px;
  flex-wrap: wrap;
}

.guide-tab {
  display: flex;
  align-items: center;
  gap: 6px;
  background: #f1f5f9;
  border: 1px solid #e2e8f0;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 0.76rem;
  font-weight: 600;
  color: #475569;
  cursor: pointer;
  transition: all 0.15s ease;
}

.guide-tab:hover {
  background: #e2e8f0;
  color: #1e293b;
}

.guide-tab.active {
  background: #0f172a;
  color: #ffffff;
  border-color: #0f172a;
}

.tab-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  display: inline-block;
}

.tab-indicator.green {
  background: #10b981;
}

.tab-indicator.red {
  background: #ef4444;
}

.tab-indicator.cyan {
  background: #06b6d4;
}

.guide-tab-pane {
  animation: fadeIn 0.2s ease;
}

.guide-grid {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.guide-rule-item {
  display: flex;
  gap: 12px;
  background: #f8fafc;
  border: 1px solid #f1f5f9;
  border-left: 3px solid #10b981;
  border-radius: 6px;
  padding: 10px 12px;
}

.guide-rule-item.avoid {
  border-left-color: #ef4444;
}

.rule-num {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  color: #10b981;
  min-width: 20px;
}

.rule-num.red {
  color: #ef4444;
}

.rule-content {
  flex: 1;
}

.rule-title {
  font-size: 0.8rem;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 3px;
}

.rule-desc {
  font-size: 0.74rem;
  line-height: 1.45;
  color: #475569;
}

.rule-desc code {
  background: #e2e8f0;
  color: #0f172a;
  padding: 1px 4px;
  border-radius: 3px;
  font-family: var(--font-mono);
  font-size: 0.72rem;
}

.template-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.75rem;
  color: #475569;
  margin-bottom: 8px;
}

.copy-btn {
  background: #ff4500;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  padding: 4px 10px;
  font-size: 0.72rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.copy-btn:hover {
  background: #e03e00;
}

.template-code {
  background: #0d1117;
  color: #c9d1d9;
  border: 1px solid #30363d;
  border-radius: 6px;
  padding: 12px;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  line-height: 1.4;
  max-height: 240px;
  overflow-y: auto;
  white-space: pre-wrap;
  margin: 0;
}

/* Parsed Demonstration Meta Card */
.prd-meta-card {
  margin-top: 16px;
  background: #fdfefe;
  border: 1px solid #fed7aa;
  border-left: 4px solid #ff4500;
  border-radius: 6px;
  padding: 16px;
}

.prd-meta-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}

.prd-tag {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  color: #ea580c;
  background: #ffedd5;
  padding: 2px 6px;
  border-radius: 3px;
  margin-bottom: 4px;
}

.prd-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: #111827;
  margin: 0;
}

.prd-threshold-badge {
  text-align: right;
  background: #0f172a;
  color: #38bdf8;
  padding: 6px 10px;
  border-radius: 4px;
  font-family: var(--font-mono);
}

.prd-threshold-badge .badge-label {
  display: block;
  font-size: 0.6rem;
  color: #94a3b8;
  letter-spacing: 0.5px;
}

.prd-threshold-badge .badge-val {
  font-size: 0.8rem;
  font-weight: 700;
}

.prd-meta-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.prd-meta-item.full {
  grid-column: 1 / -1;
  background: #f8fafc;
  padding: 8px 12px;
  border-radius: 4px;
  border: 1px dashed #cbd5e1;
}

.item-label {
  display: block;
  font-size: 0.7rem;
  font-family: var(--font-mono);
  color: #64748b;
  margin-bottom: 2px;
}

.item-val {
  display: block;
  font-size: 0.8rem;
  color: #1e293b;
  line-height: 1.4;
}

.item-val.highlight {
  color: #0f172a;
}

.file-badge {
  background: #ffedd5;
  color: #ea580c;
  font-size: 0.65rem;
  font-weight: 700;
  padding: 1px 4px;
  border-radius: 3px;
}

.upload-zone {
  border: 2px dashed #d1d5db;
  border-radius: 6px;
  padding: 32px 20px;
  text-align: center;
  cursor: pointer;
  background: #fafbfc;
  transition: all 0.2s;
}

.upload-zone:hover, .upload-zone.is-dragover {
  border-color: #ff4500;
  background: rgba(255, 69, 0, 0.02);
}

.upload-icon {
  font-size: 1.5rem;
  color: #ff4500;
  margin-bottom: 8px;
}

.upload-title {
  font-weight: 600;
  font-size: 0.95rem;
  color: #111827;
  margin-bottom: 4px;
}

.upload-hint {
  font-size: 0.78rem;
  color: #6b7280;
}

.file-tags-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
}

.file-chip {
  background: #ffffff;
  border: 1px solid #d1d5db;
  padding: 6px 12px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-mono);
  font-size: 0.8rem;
}

.file-remove {
  background: transparent;
  border: none;
  color: #9ca3af;
  font-size: 1.1rem;
  cursor: pointer;
}

.file-remove:hover {
  color: #ef4444;
}

.console-divider {
  border-top: 1px solid #f3f4f6;
  border-bottom: 1px solid #f3f4f6;
  background: #f9fafb;
  padding: 8px 28px;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: #9ca3af;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.presets-row {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 14px;
}

.preset-label {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: #6b7280;
}

.preset-chip {
  background: #f3f4f6;
  border: 1px solid #e5e7eb;
  padding: 5px 12px;
  border-radius: 16px;
  font-size: 0.78rem;
  font-family: var(--font-mono);
  color: #374151;
  cursor: pointer;
  transition: all 0.2s;
}

.preset-chip:hover {
  border-color: #ff4500;
  color: #ff4500;
}

.preset-chip.active {
  background: rgba(255, 69, 0, 0.1);
  border-color: #ff4500;
  color: #ff4500;
  font-weight: 600;
}

.input-wrapper {
  position: relative;
}

.code-input {
  width: 100%;
  background: #0d1017;
  color: #f3f4f6;
  border: 1px solid #1f2937;
  border-radius: 6px;
  padding: 16px;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  line-height: 1.5;
  resize: vertical;
}

.code-input:focus {
  outline: none;
  border-color: #ff4500;
}

.model-badge {
  position: absolute;
  bottom: 12px;
  right: 12px;
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: #9ca3af;
  background: #1f2937;
  padding: 3px 8px;
  border-radius: 4px;
}

.btn-section {
  border-top: 1px solid #f3f4f6;
  background: #fafbfc;
}

.start-engine-btn {
  width: 100%;
  background: #ff4500;
  color: #ffffff;
  border: none;
  border-radius: 6px;
  padding: 16px;
  font-family: var(--font-mono);
  font-size: 0.95rem;
  font-weight: 700;
  letter-spacing: 0.5px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  transition: all 0.2s;
}

.start-engine-btn:hover:not(:disabled) {
  background: #e03d00;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(255, 69, 0, 0.25);
}

.start-engine-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-arrow {
  font-size: 1.2rem;
}

.btn-hint {
  font-size: 0.75rem;
  color: #ef4444;
  margin-top: 10px;
  text-align: center;
}
</style>
