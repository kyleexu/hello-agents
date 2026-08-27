"""本地化 YahoAgents 精简版（旅行助手所需模块）"""

import logging

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

from .agents.simple_agent import SimpleAgent
from .core.config import Config
from .core.exceptions import HelloAgentsException
from .core.llm import HelloAgentsLLM
from .core.message import Message
from .tools import MCPTool
from .tools.registry import ToolRegistry, global_registry
from .version import __author__, __description__, __email__, __version__

__all__ = [
    "Config",
    "HelloAgentsException",
    "HelloAgentsLLM",
    "MCPTool",
    "Message",
    "SimpleAgent",
    "ToolRegistry",
    "__author__",
    "__description__",
    "__email__",
    "__version__",
    "global_registry",
]
