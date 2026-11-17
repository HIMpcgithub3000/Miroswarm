import { createI18n } from 'vue-i18n'
import en from '../../../locales/en.json'

// Always enforce English for a clean, unified experience
const messages = {
  en: en
}

const availableLocales = [
  { key: 'en', label: 'English' }
]

localStorage.setItem('locale', 'en')
if (typeof document !== 'undefined') {
  document.documentElement.lang = 'en'
}

const i18n = createI18n({
  legacy: false,
  locale: 'en',
  fallbackLocale: 'en',
  messages
})

export { availableLocales }
export default i18n
