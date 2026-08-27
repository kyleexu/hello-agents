"""配置管理"""

import os
from typing import Any

from pydantic import BaseModel


class Config(BaseModel):
    """HelloAgents配置类"""

    # LLM配置
    default_model: str = "gpt-3.5-turbo"
    default_provider: str = "openai"
    temperature: float = 0.7
    max_tokens: int | None = None

    # 系统配置
    debug: bool = False
    log_level: str = "INFO"

    # 其他配置
    max_history_length: int = 100

    @classmethod
    def from_env(cls) -> "Config":
        """从环境变量创建配置"""
        max_tokens_env = os.getenv("MAX_TOKENS")
        return cls(
            debug=os.getenv("DEBUG", "false").lower() == "true",
            log_level=os.getenv("LOG_LEVEL", "INFO"),
            temperature=float(os.getenv("TEMPERATURE", "0.7")),
            max_tokens=int(max_tokens_env) if max_tokens_env is not None else None,
        )

    def to_dict(self) -> dict[str, Any]:
        """转换为字典"""
        return self.dict()
