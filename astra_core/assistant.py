from __future__ import annotations

from dataclasses import dataclass

from astra_core.prompts import ASTRA_SYSTEM_PROMPT
from astra_llm.ollama import LLMClient


@dataclass
class TextAssistant:
    llm: LLMClient
    system_prompt: str = ASTRA_SYSTEM_PROMPT

    def respond(self, user_input: str) -> str:
        normalized_input = user_input.strip()
        if not normalized_input:
            return "Please say a little more so I can help."

        return self.llm.generate(
            prompt=normalized_input,
            system_prompt=self.system_prompt,
        )
