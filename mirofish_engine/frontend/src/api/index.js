import axios from 'axios'
import i18n from '../i18n'

// Create Axios instance with relative /mirofish/api baseURL
const service = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '/mirofish',
  timeout: 300000, // 5 min timeout for ontology and graph generation
  headers: {
    'Content-Type': 'application/json'
  }
})

// Request interceptor
service.interceptors.request.use(
  config => {
    config.headers['Accept-Language'] = i18n.global.locale.value || 'en'
    return config
  },
  error => {
    console.error('Request error:', error)
    return Promise.reject(error)
  }
)

// Response interceptor
service.interceptors.response.use(
  response => {
    const res = response.data
    
    if (!res.success && res.success !== undefined) {
      console.error('API Error:', res.error || res.message || 'Unknown error')
      return Promise.reject(new Error(res.error || res.message || 'Error'))
    }
    
    return res
  },
  error => {
    console.error('Response error:', error)
    const apiError = error.response?.data?.error || error.response?.data?.message
    
    if (error.code === 'ECONNABORTED' && error.message.includes('timeout')) {
      console.error('Request timeout')
    }
    
    if (error.message === 'Network Error') {
      console.error('Network error - please check connection to /mirofish/api')
    }

    if (typeof apiError === 'string' && apiError) {
      error.message = apiError
    }
    
    return Promise.reject(error)
  }
)

export default service
