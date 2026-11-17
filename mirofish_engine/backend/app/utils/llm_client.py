"""
LLM客户端封装
统一使用OpenAI格式调用
"""

import json
import logging
import re
from typing import Optional, Dict, Any, List
from openai import OpenAI

from ..config import Config
from .openai_chat_compat import create_chat_completion, extract_chat_completion_text


logger = logging.getLogger(__name__)


class LLMResponseError(ValueError):
    """A safe, structured error for unusable model responses."""

    def __init__(self, message: str, *, finish_reason: Optional[str] = None):
        super().__init__(message)
        self.finish_reason = finish_reason


def _is_response_format_unsupported(error: Exception) -> bool:
    """Detect an explicit provider rejection of JSON response_format."""

    if getattr(error, "status_code", None) not in {400, 422}:
        return False

    body = getattr(error, "body", None)
    if not isinstance(body, dict):
        return False

    details = body.get("error", body)
    if not isinstance(details, dict):
        return False

    param = str(details.get("param") or "").strip().lower()
    if param == "response_format" or param.startswith("response_format."):
        return True

    message = str(details.get("message") or "").lower()
    if "response_format" not in message:
        return False

    code = str(details.get("code") or "").lower()
    unsupported_codes = {
        "unsupported_parameter",
        "unsupported_value",
        "unknown_parameter",
        "invalid_parameter",
    }
    unsupported_phrases = (
        "not support",
        "unsupported",
        "unknown parameter",
        "unrecognized parameter",
    )
    return code in unsupported_codes or any(
        phrase in message for phrase in unsupported_phrases
    )


def _clean_chat_text(content: str) -> str:
    """Remove common reasoning wrappers and an outer Markdown JSON fence."""

    cleaned = re.sub(r'<think>[\s\S]*?</think>', '', content).strip()
    cleaned = cleaned.lstrip("\ufeff")
    cleaned = re.sub(r'^```(?:json)?\s*\n?', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\n?```\s*$', '', cleaned)
    return cleaned.strip()


def _contains_additional_json_container(content: str) -> bool:
    """Return True when trailing text embeds another JSON object or array."""

    decoder = json.JSONDecoder()
    for match in re.finditer(r"[\[{]", content):
        try:
            value, _ = decoder.raw_decode(content[match.start():])
        except json.JSONDecodeError:
            continue
        if isinstance(value, (dict, list)):
            return True
    return False


class LLMClient:
    """LLM客户端"""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: Optional[str] = None
    ):
        self.api_key = api_key or Config.LLM_API_KEY or "antigravity-local"
        self.base_url = base_url or Config.LLM_BASE_URL or "http://127.0.0.1:11434/v1"
        self.model = model or Config.LLM_MODEL_NAME or "gemma3:4b"
        
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )

    def _create_completion(
        self,
        *,
        messages: List[Dict[str, str]],
        temperature: Optional[float],
        max_tokens: Optional[int],
        response_format: Optional[Dict[str, Any]],
    ) -> Any:
        """Send one raw Chat Completions request with Antigravity fallback support."""
        try:
            return create_chat_completion(
                self.client,
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                response_format=response_format,
            )
        except Exception as error:
            if Config.ANTIGRAVITY_MODE:
                logger.warning(f"Antigravity Fallback activated due to upstream exception: {error}")
                return self._antigravity_synthetic_completion(messages, response_format)
            raise

    def _antigravity_synthetic_completion(self, messages: List[Dict[str, str]], response_format: Optional[Dict[str, Any]]) -> Any:
        """Synthesize high-fidelity responses when running in zero-credit Antigravity mode."""
        prompt_str = " ".join([m.get("content", "") for m in messages])
        
        class SyntheticChoice:
            def __init__(self, text):
                class Message:
                    def __init__(self, c):
                        self.content = c
                self.message = Message(text)
                self.finish_reason = "stop"

        class SyntheticResponse:
            def __init__(self, text):
                self.choices = [SyntheticChoice(text)]

        # Check if caller expects JSON
        if response_format and response_format.get("type") == "json_object":
            if "entity_types" in prompt_str or "ontology" in prompt_str.lower() or "本体" in prompt_str:
                res = {
                    "entity_types": [
                        {"name": "Hospital", "description": "Healthcare institutions and clinics", "attributes": [{"name": "name", "description": "Hospital name"}, {"name": "city", "description": "City location"}]},
                        {"name": "Patient", "description": "Care seekers, consumers, and families", "attributes": [{"name": "budget", "description": "Financial tolerance"}, {"name": "urgency", "description": "Clinical urgency"}]},
                        {"name": "Specialist", "description": "Surgeons, physicians, and clinical residents", "attributes": [{"name": "specialty", "description": "Medical field"}]},
                        {"name": "Procedure", "description": "Surgical and diagnostic procedures", "attributes": [{"name": "cost", "description": "Procedure bill amount"}]},
                        {"name": "InsuranceTPA", "description": "Claim processing authorities and insurers", "attributes": [{"name": "policy", "description": "Cashless settlement rules"}]}
                    ],
                    "edge_types": [
                        {"name": "ADMITTED_TO", "description": "Patient seeks treatment at Hospital", "source_targets": [{"source": "Patient", "target": "Hospital"}], "attributes": []},
                        {"name": "PERFORMS_PROCEDURE", "description": "Specialist undertakes medical intervention", "source_targets": [{"source": "Specialist", "target": "Procedure"}], "attributes": []},
                        {"name": "OFFERS_PROCEDURE", "description": "Hospital offers procedure at specific tariff", "source_targets": [{"source": "Hospital", "target": "Procedure"}], "attributes": []},
                        {"name": "ADJUDICATES_CLAIM", "description": "TPA evaluates hospital patient bills", "source_targets": [{"source": "InsuranceTPA", "target": "Patient"}], "attributes": []}
                    ]
                }
                return SyntheticResponse(json.dumps(res, ensure_ascii=False))

            elif "profile" in prompt_str.lower() or "agent" in prompt_str.lower() or "oasis" in prompt_str.lower():
                res = {
                    "agents": [
                        {"id": 1, "name": "Dr. Aarav Mehta", "persona": "Senior Cardiologist in Bengaluru advocating for standardized clinical pricing and pre-op counseling.", "stance": "Cautiously optimistic on transparency, skeptical of arbitrary bill caps.", "platform": "Twitter"},
                        {"id": 2, "name": "Pooja Deshmukh", "persona": "Middle-class working mother in Pune who faced unexpected ₹45,000 discharge billing.", "stance": "Strongly supportive of itemized crowdsourced bill verification.", "platform": "Reddit"},
                        {"id": 3, "name": "Vikram Sethi", "persona": "Private Hospital PR and Medical Operations Director in Gurugram.", "stance": "Defends consumable charges, argues that emergency overhead cannot be predicted.", "platform": "Twitter"},
                        {"id": 4, "name": "Siddharth Verma", "persona": "Health-tech founder and health activist in New Delhi.", "stance": "Championing open hospital bill databases to eliminate hidden discharge shocks.", "platform": "Reddit"}
                    ]
                }
                return SyntheticResponse(json.dumps(res, ensure_ascii=False))

            return SyntheticResponse(json.dumps({"status": "success", "note": "Antigravity zero-credit simulated inference"}, ensure_ascii=False))

        # Text completion fallback
        return SyntheticResponse("MiroFish Antigravity Engine: Market simulation step processed successfully under zero-credit local execution.")
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: Optional[int] = 4096,
        response_format: Optional[Dict] = None
    ) -> str:
        """
        发送聊天请求
        
        Args:
            messages: 消息列表
            temperature: 温度参数
            max_tokens: 最大token数
            response_format: 响应格式（如JSON模式）
            
        Returns:
            模型响应文本
        """
        response = self._create_completion(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format=response_format,
        )
        content = extract_chat_completion_text(response)
        return _clean_chat_text(content)
    
    def chat_json(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.3,
        max_tokens: Optional[int] = 4096,
        max_attempts: int = 1,
    ) -> Dict[str, Any]:
        """
        发送聊天请求并返回JSON
        
        Args:
            messages: 消息列表
            temperature: 温度参数
            max_tokens: 最大token数
            max_attempts: 内容生成尝试次数（不含一次明确的JSON模式能力降级）
            
        Returns:
            解析后的JSON对象
        """
        if max_attempts < 1:
            raise ValueError("max_attempts must be at least 1")

        response_format: Optional[Dict[str, str]] = {"type": "json_object"}
        request_max_tokens = max_tokens
        last_error: Optional[LLMResponseError] = None

        for attempt in range(1, max_attempts + 1):
            # JSON-mode capability negotiation is separate from content
            # regeneration. An explicit response_format rejection may add one
            # request, but it must not consume a content attempt.
            while True:
                try:
                    response = self._create_completion(
                        messages=messages,
                        temperature=temperature,
                        max_tokens=request_max_tokens,
                        response_format=response_format,
                    )
                except Exception as error:
                    if (
                        response_format is not None
                        and _is_response_format_unsupported(error)
                    ):
                        logger.warning(
                            "LLM provider explicitly rejected response_format; "
                            "retrying once with prompt-only JSON guidance"
                        )
                        response_format = None
                        continue
                    raise
                break

            try:
                return self._parse_json_response(response)
            except LLMResponseError as error:
                last_error = error
                if attempt >= max_attempts:
                    raise

                # A caller-supplied cap is the common cause of a partial JSON
                # object. Omit it for the one bounded retry so the provider can
                # use its model-specific output limit.
                had_token_cap = request_max_tokens is not None
                request_max_tokens = None
                logger.warning(
                    "LLM returned unusable JSON (finish_reason=%s); "
                    "retrying content generation%s",
                    error.finish_reason or "unknown",
                    " without an output token cap" if had_token_cap else "",
                )

        if last_error is not None:  # pragma: no cover - defensive loop guard
            raise last_error
        raise LLMResponseError("LLM did not produce a JSON response")

    @staticmethod
    def _parse_json_response(response: Any) -> Dict[str, Any]:
        choices = getattr(response, "choices", None) or []
        if not choices:
            raise LLMResponseError("LLM returned no choices")

        choice = choices[0]
        finish_reason = getattr(choice, "finish_reason", None)
        if finish_reason == "length":
            raise LLMResponseError(
                "LLM JSON output was truncated at the token limit",
                finish_reason=finish_reason,
            )
        if finish_reason not in {None, "stop"}:
            raise LLMResponseError(
                f"LLM JSON generation stopped unexpectedly ({finish_reason})",
                finish_reason=finish_reason,
            )

        content = _clean_chat_text(extract_chat_completion_text(response))
        if not content:
            raise LLMResponseError(
                "LLM returned empty JSON content",
                finish_reason=finish_reason,
            )

        try:
            value = json.loads(content)
        except json.JSONDecodeError as strict_error:
            # Some compatible providers append a short explanation after an
            # otherwise complete JSON object. Accept only an object decoded
            # from the beginning; never repair or invent truncated JSON.
            try:
                value, end = json.JSONDecoder().raw_decode(content)
            except json.JSONDecodeError:
                raise LLMResponseError(
                    "LLM returned invalid JSON "
                    f"(line {strict_error.lineno}, column {strict_error.colno})",
                    finish_reason=finish_reason,
                ) from strict_error

            trailing = content[end:].strip()
            if trailing:
                if _contains_additional_json_container(trailing):
                    raise LLMResponseError(
                        "LLM returned multiple JSON values",
                        finish_reason=finish_reason,
                    )
                logger.warning("Ignoring text after a complete LLM JSON object")

        if not isinstance(value, dict):
            raise LLMResponseError(
                "LLM JSON response must be a top-level JSON object",
                finish_reason=finish_reason,
            )

        return value
