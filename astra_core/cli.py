from __future__ import annotations

from astra_config import AstraSettings
from astra_core import TextAssistant
from astra_llm import LLMError, OllamaClient

EXIT_COMMANDS = {"exit", "quit", "q"}


def build_assistant() -> TextAssistant:
    settings = AstraSettings.from_env()
    llm = OllamaClient(
        host=settings.ollama_host,
        model=settings.ollama_model,
        timeout_seconds=settings.ollama_timeout_seconds,
    )
    return TextAssistant(llm=llm)


def run_text_loop(assistant: TextAssistant) -> None:
    print("Astra text assistant")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in EXIT_COMMANDS:
            print("Astra: Goodbye.")
            return

        try:
            response = assistant.respond(user_input)
        except LLMError as exc:
            print(f"Astra: {exc}")
            continue

        print(f"Astra: {response}")


def main() -> None:
    run_text_loop(build_assistant())
