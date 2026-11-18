import service from './index'

export const getSampleDemonstrations = () => {
  return service.get('/api/prd/sample-demonstrations')
}

export const parseDemonstration = (data) => {
  return service.post('/api/prd/parse-demonstration', data)
}

export const getPrdEvaluation = (reportId) => {
  return service.get(`/api/prd/evaluation/${reportId}`)
}

export const refinePrd = (data) => {
  return service.post('/api/prd/refine', data)
}

export const makeProduct = (data) => {
  return service.post('/api/prd/make-product', data)
}
