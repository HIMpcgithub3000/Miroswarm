<template>
  <div class="home-container">
    <!-- Top Navigation Bar -->
    <nav class="navbar">
      <div class="nav-left">
        <div class="nav-brand">MIROFISH</div>
        <span class="brand-tag">DECISION SIMULATION ENGINE</span>
      </div>

      <div class="nav-center">
        <div class="status-pill">
          <span class="status-dot-pulse"></span>
          <span class="status-text">Local CPU Engine Active</span>
          <span class="zero-cost-tag">Zero API Credits</span>
        </div>
      </div>

      <div class="nav-links">
        <LanguageSwitcher />
        <a href="https://github.com/666ghj/MiroFish" target="_blank" class="github-link">
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
            <span class="orange-tag">Concise &amp; Universal Swarm Intelligence Engine</span>
            <span class="version-text">/ v0.1-Preview</span>
          </div>

          <h1 class="main-title">
            Upload Reports,<br>
            <span class="gradient-text">Predict the Future</span>
          </h1>

          <div class="hero-desc">
            <p>
              From a single document or policy brief, <span class="highlight-bold">MiroFish</span> extracts reality seeds to auto-generate a parallel world of autonomous stakeholder agents. Inject variables to stress-test decisions before real-world rollout.
            </p>
            <p class="slogan-text">
              Let Agents rehearse the future, let decisions prevail<span class="blinking-cursor">_</span>
            </p>
          </div>

          <div class="decoration-square"></div>
        </div>

        <div class="hero-right">
          <div class="logo-container">
            <img src="../assets/logo/MiroFish_logo_left.jpeg" alt="MiroFish Logo" class="hero-logo" />
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
            <span class="status-dot">■</span> System Status
          </div>

          <h2 class="section-title">Ready</h2>
          <p class="section-desc">
            Prediction engine on standby. Upload reality seeds or choose a scenario preset to initialize a simulation sequence.
          </p>

          <!-- Metric Cards -->
          <div class="metrics-row">
            <div class="metric-card">
              <div class="metric-value">Zero API Cost</div>
              <div class="metric-label">Runs locally on CPU</div>
            </div>
            <div class="metric-card">
              <div class="metric-value">OASIS Swarm</div>
              <div class="metric-label">Autonomous multi-agent twin</div>
            </div>
          </div>

          <!-- 5-Step Workflow Sequence -->
          <div class="steps-container">
            <div class="steps-header">
              <span class="diamond-icon">◇</span> Workflow Sequence
            </div>
            <div class="workflow-list">
              <div class="workflow-item">
                <span class="step-num">01</span>
                <div class="step-info">
                  <div class="step-title">Graph Build</div>
                  <div class="step-desc">Seed extraction, entity-relationship ontology &amp; knowledge graph construction</div>
                </div>
              </div>
              <div class="workflow-item">
                <span class="step-num">02</span>
                <div class="step-info">
                  <div class="step-title">Env Setup</div>
                  <div class="step-desc">Entity extraction, OASIS persona generation &amp; stakeholder config injection</div>
                </div>
              </div>
              <div class="workflow-item">
                <span class="step-num">03</span>
                <div class="step-info">
                  <div class="step-title">Run Simulation</div>
                  <div class="step-desc">Multi-turn parallel simulation across social media sandboxes (Twitter / Reddit)</div>
                </div>
              </div>
              <div class="workflow-item">
                <span class="step-num">04</span>
                <div class="step-info">
                  <div class="step-title">Report Generation</div>
                  <div class="step-desc">ReACT analytical report evaluating causal outcomes, metrics &amp; risk factors</div>
                </div>
              </div>
              <div class="workflow-item">
                <span class="step-num">05</span>
                <div class="step-info">
                  <div class="step-title">Deep Interaction</div>
                  <div class="step-desc">Direct 1-on-1 interview dialogue with any synthetic stakeholder agent</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Panel: Interactive Simulation Console -->
        <div class="right-panel">
          <div class="console-box">
            <!-- 01: Reality Seed Upload -->
            <div class="console-section">
              <div class="console-header">
                <span class="console-label">01 / Reality Seed</span>
                <div class="header-actions">
                  <button type="button" class="sample-btn" @click.prevent="loadSampleSeed" :disabled="loading">
                    + Load Sample Seed
                  </button>
                  <span class="console-meta">PDF, MD, TXT</span>
                </div>
              </div>

              <div
                class="upload-zone"
                :class="{ 'drag-over': isDragOver, 'has-files': files.length > 0 }"
                @dragover.prevent="handleDragOver"
                @dragleave.prevent="handleDragLeave"
                @drop.prevent="handleDrop"
                @click="triggerFileInput"
              >
                <input
                  ref="fileInput"
                  type="file"
                  multiple
                  accept=".pdf,.md,.txt"
                  @change="handleFileSelect"
                  style="display: none"
                  :disabled="loading"
                />

                <div v-if="files.length === 0" class="upload-placeholder">
                  <div class="upload-icon">↑</div>
                  <div class="upload-title">Drag reality seed documents here</div>
                  <div class="upload-hint">or click to browse from disk</div>
                </div>

                <div v-else class="file-list">
                  <div v-for="(file, index) in files" :key="index" class="file-item" @click.stop>
                    <span class="file-icon">📄</span>
                    <span class="file-name">{{ file.name }}</span>
                    <button @click.stop="removeFile(index)" class="remove-btn" title="Remove file">×</button>
                  </div>
                </div>
              </div>
            </div>

            <!-- Divider -->
            <div class="console-divider">
              <span>Input Parameters</span>
            </div>

            <!-- 02: Simulation Prompt & Presets -->
            <div class="console-section">
              <div class="console-header">
                <span class="console-label">>_ 02 / Simulation Prompt</span>
              </div>

              <!-- Quick Presets -->
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
                  placeholder="// Describe your policy change, business decision, or simulation objective..."
                  rows="5"
                  :disabled="loading"
                ></textarea>
                <div class="model-badge">Engine: Antigravity-Qwen2.5-Local</div>
              </div>
            </div>

            <!-- 03: Start Engine Button -->
            <div class="console-section btn-section">
              <button
                class="start-engine-btn"
                @click="startSimulation"
                :disabled="!canSubmit || loading"
              >
                <span v-if="!loading">START SIMULATION ENGINE</span>
                <span v-else>INITIALIZING ENGINE...</span>
                <span class="btn-arrow">→</span>
              </button>
              <div v-if="!canSubmit && files.length === 0" class="btn-hint">
                * Please attach at least 1 reality seed document (or click 'Load Sample Seed') and specify a prompt.
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
import LanguageSwitcher from '../components/LanguageSwitcher.vue'

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
  font-family: var(--font-mono);
  font-size: 0.75rem;
}

.status-dot-pulse {
  width: 7px;
  height: 7px;
  background: #10b981;
  border-radius: 50%;
  box-shadow: 0 0 8px #10b981;
}

.status-text {
  color: #d1d5db;
}

.zero-cost-tag {
  color: #ff4500;
  font-weight: 700;
  background: rgba(255, 69, 0, 0.15);
  padding: 1px 6px;
  border-radius: 3px;
  font-size: 0.7rem;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 16px;
}

.github-link {
  color: #ffffff;
  text-decoration: none;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 4px;
  transition: all 0.2s;
}

.github-link:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: #ffffff;
}

.arrow {
  color: #ff4500;
  font-weight: bold;
}

/* Main Content */
.main-content {
  max-width: 1360px;
  margin: 0 auto;
  padding: 40px 32px 80px;
}

/* Hero Section */
.hero-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 50px 0 60px;
  border-bottom: 1px solid #e5e7eb;
  position: relative;
}

.hero-left {
  max-width: 760px;
}

.tag-row {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
}

.orange-tag {
  background: #ff4500;
  color: #ffffff;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  padding: 4px 10px;
  letter-spacing: 0.5px;
  border-radius: 2px;
  text-transform: uppercase;
}

.version-text {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: #6b7280;
  font-weight: 600;
}

.main-title {
  font-size: 3.4rem;
  font-weight: 800;
  line-height: 1.12;
  letter-spacing: -1px;
  margin-bottom: 24px;
  color: #0a0a0c;
}

.gradient-text {
  color: #ff4500;
}

.hero-desc {
  font-size: 1.15rem;
  color: #4b5563;
  line-height: 1.6;
  max-width: 680px;
}

.highlight-bold {
  font-weight: 700;
  color: #0a0a0c;
}

.slogan-text {
  margin-top: 16px;
  font-family: var(--font-mono);
  font-size: 0.95rem;
  color: #111827;
  font-weight: 600;
}

.blinking-cursor {
  color: #ff4500;
  font-weight: bold;
  animation: blink 1s step-end infinite;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

.hero-right {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
}

.logo-container {
  width: 260px;
  height: 260px;
  border: 1px solid #e5e7eb;
  padding: 12px;
  background: #ffffff;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-logo {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.scroll-down-btn {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: 1px solid #d1d5db;
  background: #ffffff;
  color: #111827;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.scroll-down-btn:hover {
  background: #0a0a0c;
  color: #ffffff;
  border-color: #0a0a0c;
  transform: translateY(2px);
}

/* Dashboard Section */
.dashboard-section {
  display: grid;
  grid-template-columns: 460px 1fr;
  gap: 40px;
  padding-top: 60px;
  padding-bottom: 40px;
}

/* Left Panel */
.left-panel {
  border-right: 1px solid #e5e7eb;
  padding-right: 36px;
}

.panel-header {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  letter-spacing: 1.5px;
  color: #6b7280;
  text-transform: uppercase;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.status-dot {
  color: #10b981;
}

.section-title {
  font-size: 2rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  margin-bottom: 12px;
  color: #0a0a0c;
}

.section-desc {
  font-size: 0.95rem;
  color: #6b7280;
  line-height: 1.55;
  margin-bottom: 24px;
}

.metrics-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 32px;
}

.metric-card {
  border: 1px solid #e5e7eb;
  padding: 16px;
  background: #f9fafb;
}

.metric-value {
  font-family: var(--font-mono);
  font-size: 1.1rem;
  font-weight: 800;
  color: #0a0a0c;
  margin-bottom: 4px;
}

.metric-label {
  font-size: 0.75rem;
  color: #6b7280;
}

/* Workflow Sequence */
.steps-container {
  border-top: 1px solid #e5e7eb;
  padding-top: 24px;
}

.steps-header {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: #111827;
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
  gap: 16px;
}

.workflow-item {
  display: flex;
  align-items: flex-start;
  gap: 14px;
}

.step-num {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  font-weight: 800;
  color: #ff4500;
  background: rgba(255, 69, 0, 0.08);
  padding: 2px 6px;
  border-radius: 2px;
}

.step-info {
  flex: 1;
}

.step-title {
  font-size: 0.9rem;
  font-weight: 700;
  color: #111827;
  margin-bottom: 2px;
}

.step-desc {
  font-size: 0.8rem;
  color: #6b7280;
  line-height: 1.4;
}

/* Right Panel: Console */
.right-panel {
  display: flex;
  flex-direction: column;
}

.console-box {
  border: 1px solid #0a0a0c;
  background: #ffffff;
  box-shadow: 6px 6px 0px #0a0a0c;
}

.console-section {
  padding: 24px;
}

.console-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 14px;
}

.console-label {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  font-weight: 800;
  letter-spacing: 1px;
  color: #0a0a0c;
  text-transform: uppercase;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.sample-btn {
  background: #f3f4f6;
  border: 1px solid #d1d5db;
  color: #111827;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 3px;
  cursor: pointer;
  transition: all 0.2s;
}

.sample-btn:hover:not(:disabled) {
  background: #ff4500;
  color: #ffffff;
  border-color: #ff4500;
}

.console-meta {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: #9ca3af;
}

/* Upload Zone */
.upload-zone {
  border: 2px dashed #d1d5db;
  padding: 28px 20px;
  text-align: center;
  background: #f9fafb;
  cursor: pointer;
  transition: all 0.2s;
  min-height: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.upload-zone:hover,
.upload-zone.drag-over {
  border-color: #ff4500;
  background: rgba(255, 69, 0, 0.03);
}

.upload-zone.has-files {
  padding: 16px;
  border-style: solid;
  border-color: #e5e7eb;
  background: #ffffff;
}

.upload-icon {
  font-size: 1.6rem;
  color: #ff4500;
  margin-bottom: 6px;
  font-weight: bold;
}

.upload-title {
  font-size: 0.95rem;
  font-weight: 600;
  color: #111827;
  margin-bottom: 2px;
}

.upload-hint {
  font-size: 0.8rem;
  color: #9ca3af;
}

.file-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: 100%;
}

.file-item {
  display: flex;
  align-items: center;
  gap: 10px;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  padding: 8px 12px;
  border-radius: 4px;
}

.file-icon {
  font-size: 1.1rem;
}

.file-name {
  flex: 1;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: #111827;
  text-align: left;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.remove-btn {
  background: transparent;
  border: none;
  color: #9ca3af;
  font-size: 1.2rem;
  cursor: pointer;
  line-height: 1;
  padding: 0 4px;
}

.remove-btn:hover {
  color: #ef4444;
}

/* Console Divider */
.console-divider {
  display: flex;
  align-items: center;
  padding: 0 24px;
  background: #f3f4f6;
  height: 32px;
  border-top: 1px solid #e5e7eb;
  border-bottom: 1px solid #e5e7eb;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 1.5px;
  color: #6b7280;
  text-transform: uppercase;
}

/* Presets Row */
.presets-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}

.preset-label {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: #6b7280;
  font-weight: 600;
}

.preset-chip {
  background: #f3f4f6;
  border: 1px solid #e5e7eb;
  color: #374151;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  padding: 4px 10px;
  border-radius: 12px;
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
  font-weight: 700;
}

/* Textarea Input */
.input-wrapper {
  position: relative;
}

.code-input {
  width: 100%;
  font-family: var(--font-mono);
  font-size: 0.9rem;
  line-height: 1.6;
  padding: 16px;
  padding-bottom: 36px;
  background: #f9fafb !important;
  border: 1px solid #d1d5db !important;
  color: #111827 !important;
  border-radius: 4px;
  resize: vertical;
}

.code-input:focus {
  border-color: #ff4500 !important;
  box-shadow: 0 0 0 2px rgba(255, 69, 0, 0.15) !important;
}

.model-badge {
  position: absolute;
  bottom: 10px;
  right: 12px;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: #9ca3af;
  background: #ffffff;
  padding: 2px 6px;
  border: 1px solid #e5e7eb;
  border-radius: 2px;
}

/* Start Button Section */
.btn-section {
  padding-top: 16px;
  border-top: 1px solid #e5e7eb;
}

.start-engine-btn {
  width: 100%;
  height: 56px;
  background: #ff4500;
  color: #ffffff;
  border: 2px solid #0a0a0c;
  font-family: var(--font-mono);
  font-size: 1rem;
  font-weight: 800;
  letter-spacing: 1px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  box-shadow: 4px 4px 0px #0a0a0c;
  cursor: pointer;
  transition: all 0.2s;
}

.start-engine-btn:hover:not(:disabled) {
  background: #e03d00;
  transform: translate(-1px, -1px);
  box-shadow: 5px 5px 0px #0a0a0c;
}

.start-engine-btn:disabled {
  background: #e5e7eb;
  color: #9ca3af;
  border-color: #d1d5db;
  box-shadow: none;
  cursor: not-allowed;
}

.btn-arrow {
  font-size: 1.2rem;
  font-weight: bold;
}

.btn-hint {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: #ef4444;
  margin-top: 8px;
  text-align: center;
}

@media (max-width: 1024px) {
  .dashboard-section {
    grid-template-columns: 1fr;
  }
  .left-panel {
    border-right: none;
    border-bottom: 1px solid #e5e7eb;
    padding-right: 0;
    padding-bottom: 36px;
  }
}
</style>
