import requests
import json
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger('miro_swarm.llm')

OLLAMA_BASE_URL = 'http://127.0.0.1:11434'
DEFAULT_MODEL = 'qwen2.5:1.5b'

def query_local_llm(prompt: str, system_prompt: Optional[str] = None, format_json: bool = False, temperature: float = 0.2) -> str:
    url = f'{OLLAMA_BASE_URL}/api/generate'
    payload: Dict[str, Any] = {
        'model': DEFAULT_MODEL,
        'prompt': prompt,
        'stream': False,
        'options': {
            'temperature': temperature,
            'num_ctx': 4096
        }
    }
    if system_prompt:
        payload['system'] = system_prompt
    if format_json:
        payload['format'] = 'json'

    try:
        response = requests.post(url, json=payload, timeout=45)
        response.raise_for_status()
        data = response.json()
        return data.get('response', '')
    except Exception as e:
        logger.error(f'Local LLM inference error: {e}')
        # Fallback structured mock if offline or error
        if format_json:
            return json.dumps({'error': str(e), 'status': 'fallback'})
        return f'[LLM Error: {e}]'

def query_structured_llm(prompt: str, system_prompt: Optional[str] = None) -> Dict[str, Any]:
    raw = query_local_llm(prompt, system_prompt, format_json=True)
    try:
        return json.loads(raw)
    except Exception:
        return {'raw_output': raw}
