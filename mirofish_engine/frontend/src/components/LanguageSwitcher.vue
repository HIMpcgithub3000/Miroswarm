<template>
  <div class=language-badge>
    <span class=lang-dot></span>
    <span class=lang-text>EN</span>
  </div>
</template>

<script setup>
// English-only indicator
</script>

<style scoped>
.language-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #1a1a1a;
  color: #e5e5e5;
  border: 1px solid #333333;
  padding: 4px 10px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  font-weight: 600;
  border-radius: 4px;
  letter-spacing: 0.5px;
}

.lang-dot {
  width: 6px;
  height: 6px;
  background: #10B981;
  border-radius: 50%;
  box-shadow: 0 0 6px rgba(16, 185, 129, 0.6);
}

.lang-text {
  color: #ffffff;
}
</style>
