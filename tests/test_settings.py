from pathlib import Path

import pytest

from astra_config import AstraSettings


def test_settings_use_safe_local_defaults(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv("ASTRA_OLLAMA_HOST", raising=False)
    monkeypatch.delenv("ASTRA_OLLAMA_MODEL", raising=False)
    monkeypatch.delenv("ASTRA_OLLAMA_TIMEOUT_SECONDS", raising=False)

    settings = AstraSettings.from_env(env_file=tmp_path / ".env")

    assert settings.ollama_host == "http://localhost:11434"
    assert settings.ollama_model == "llama3.2"
    assert settings.ollama_timeout_seconds == 60.0


def test_settings_can_be_loaded_from_environment(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setenv("ASTRA_OLLAMA_HOST", "http://example.local:11434/")
    monkeypatch.setenv("ASTRA_OLLAMA_MODEL", "local-model")
    monkeypatch.setenv("ASTRA_OLLAMA_TIMEOUT_SECONDS", "12.5")

    settings = AstraSettings.from_env(env_file=tmp_path / ".env")

    assert settings.ollama_host == "http://example.local:11434"
    assert settings.ollama_model == "local-model"
    assert settings.ollama_timeout_seconds == 12.5


def test_settings_can_be_loaded_from_dotenv(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv("ASTRA_OLLAMA_HOST", raising=False)
    monkeypatch.delenv("ASTRA_OLLAMA_MODEL", raising=False)
    monkeypatch.delenv("ASTRA_OLLAMA_TIMEOUT_SECONDS", raising=False)
    env_file = tmp_path / ".env"
    env_file.write_text(
        "ASTRA_OLLAMA_HOST=http://dotenv.local:11434\n"
        "ASTRA_OLLAMA_MODEL=dotenv-model\n"
        "ASTRA_OLLAMA_TIMEOUT_SECONDS=9\n",
        encoding="utf-8",
    )

    settings = AstraSettings.from_env(env_file=env_file)

    assert settings.ollama_host == "http://dotenv.local:11434"
    assert settings.ollama_model == "dotenv-model"
    assert settings.ollama_timeout_seconds == 9.0


def test_timeout_must_be_positive(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setenv("ASTRA_OLLAMA_TIMEOUT_SECONDS", "0")

    with pytest.raises(ValueError, match="greater than zero"):
        AstraSettings.from_env(env_file=tmp_path / ".env")
