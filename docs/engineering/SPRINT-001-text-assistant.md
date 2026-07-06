# Sprint 001: Text Assistant

## Context

Sprint 0 established Astra's open source foundation and architectural direction. Sprint 1 introduces the smallest useful assistant behavior: a local text loop that sends user input to an Ollama-backed model and returns the response.

This sprint keeps the architecture modular and avoids tool calling, voice, memory, and paid token APIs.

## Objective

Create a working text assistant path that can run locally with Ollama, while keeping the model client replaceable and the core assistant flow testable without a running LLM.

## Deliverables

- `astra_core` package for assistant orchestration and CLI loop.
- `astra_llm` package with an Ollama client boundary.
- `astra_config` package for environment-based settings.
- `main.py` entry point delegated to the CLI.
- `pyproject.toml` script entry point for `uv run astra`.
- `.env.example` for safe local configuration.
- Tests for assistant behavior and settings.
- README updates for Sprint 1 usage.

## Out of Scope

- Voice input or output.
- Wake word support.
- Tool calling.
- Memory.
- Personal integrations.
- Cloud LLM or paid token APIs in the primary runtime.
- Complex prompt management.

## Acceptance Criteria

Sprint 001 is complete when:

- The assistant can be started from the command line.
- The assistant reads local settings from environment variables or `.env`.
- Ollama usage is isolated behind a replaceable client.
- Tests cover the core assistant response flow without requiring Ollama.
- Tests cover default and overridden settings.
- No secrets are committed.
- No voice, memory, or tool logic is added.

## Validation Checklist

- [ ] Run `uv run pytest`.
- [x] Confirm the text loop starts and exits cleanly.
- [x] Confirm missing Ollama produces a helpful local error.
- [x] Confirm `.env` is ignored and `.env.example` is safe to commit.
- [x] Confirm no paid token API integration exists in the runtime.

## Risks

- Ollama may not be installed or running on a contributor machine.
- The default model may not be available locally.
- Early prompt behavior may feel basic until conversation design improves.
- Future tool calling should not be hardcoded into the text loop.

## Notes

The assistant loop is intentionally small. The main design value of this sprint is the replaceable boundary between core assistant behavior and local model generation.
