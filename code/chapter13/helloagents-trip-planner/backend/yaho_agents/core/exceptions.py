"""异常体系"""


class HelloAgentsException(Exception):
    """HelloAgents基础异常类"""


class LLMException(HelloAgentsException):
    """LLM相关异常"""


class AgentException(HelloAgentsException):
    """Agent相关异常"""


class ConfigException(HelloAgentsException):
    """配置相关异常"""


class ToolException(HelloAgentsException):
    """工具相关异常"""
