from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AstraSettings:
    ollama_host: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"
    ollama_timeout_seconds: float = 60.0

    @classmethod
    def from_env(cls, env_file: str | Path = ".env") -> "AstraSettings":
        _load_dotenv(Path(env_file))

        return cls(
            ollama_host=os.getenv("ASTRA_OLLAMA_HOST", cls.ollama_host).rstrip("/"),
            ollama_model=os.getenv("ASTRA_OLLAMA_MODEL", cls.ollama_model),
            ollama_timeout_seconds=_float_env(
                "ASTRA_OLLAMA_TIMEOUT_SECONDS",
                cls.ollama_timeout_seconds,
            ),
        )


def _load_dotenv(path: Path) -> None:
    if not path.exists():
        return

    for line in path.read_text(encoding="utf-8").splitlines():
        stripped_line = line.strip()
        if not stripped_line or stripped_line.startswith("#") or "=" not in stripped_line:
            continue

        key, value = stripped_line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def _float_env(name: str, default: float) -> float:
    raw_value = os.getenv(name)
    if raw_value is None or raw_value.strip() == "":
        return default

    try:
        value = float(raw_value)
    except ValueError as exc:
        raise ValueError(f"{name} must be a number.") from exc

    if value <= 0:
        raise ValueError(f"{name} must be greater than zero.")

    return value
