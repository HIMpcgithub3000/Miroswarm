<template>
  <div class=mirofish-app-root>
    <router-view />
  </div>
</template>

<script setup>
// MiroFish - Decision Simulation Engine Root
</script>

<style>
/* Global Modern Reset */
:root {
  --black: #0a0a0c;
  --white: #ffffff;
  --orange: #ff4500;
  --orange-hover: #e03d00;
  --gray-50: #f9fafb;
  --gray-100: #f3f4f6;
  --gray-200: #e5e7eb;
  --gray-300: #d1d5db;
  --gray-400: #9ca3af;
  --gray-500: #6b7280;
  --gray-600: #4b5563;
  --gray-700: #374151;
  --gray-800: #1f2937;
  --gray-900: #111827;
  
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
  --font-sans: 'Space Grotesk', 'Inter', -apple-system, sans-serif;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: #fafbfc;
  color: var(--black);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app {
  min-height: 100vh;
}

/* Custom Sleek Scrollbar */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: var(--gray-100);
}

::-webkit-scrollbar-thumb {
  background: var(--gray-400);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--gray-600);
}

button {
  font-family: inherit;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}
</style>
