from astra_core import TextAssistant


class FakeLLM:
    def __init__(self) -> None:
        self.calls = []

    def generate(self, prompt: str, system_prompt: str) -> str:
        self.calls.append((prompt, system_prompt))
        return "Hello from local Astra."


def test_text_assistant_returns_model_response() -> None:
    llm = FakeLLM()
    assistant = TextAssistant(llm=llm)

    response = assistant.respond(" Hello ")

    assert response == "Hello from local Astra."
    assert llm.calls == [("Hello", assistant.system_prompt)]


def test_text_assistant_handles_empty_input_without_calling_model() -> None:
    llm = FakeLLM()
    assistant = TextAssistant(llm=llm)

    response = assistant.respond("   ")

    assert response == "Please say a little more so I can help."
    assert llm.calls == []
