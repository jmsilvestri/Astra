from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Protocol
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class LLMClient(Protocol):
    def generate(self, prompt: str, system_prompt: str) -> str:
        pass


class LLMError(RuntimeError):
    pass


@dataclass(frozen=True)
class OllamaClient:
    host: str
    model: str
    timeout_seconds: float = 60.0

    def generate(self, prompt: str, system_prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system_prompt,
            "stream": False,
        }
        request = Request(
            url=f"{self.host.rstrip('/')}/api/generate",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urlopen(request, timeout=self.timeout_seconds) as response:
                data = json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError) as exc:
            raise LLMError(
                "Could not reach Ollama. Is it running locally?"
            ) from exc
        except json.JSONDecodeError as exc:
            raise LLMError("Ollama returned invalid JSON.") from exc

        generated_text = data.get("response")
        if not isinstance(generated_text, str):
            raise LLMError("Ollama returned an unexpected response.")

        return generated_text.strip()
