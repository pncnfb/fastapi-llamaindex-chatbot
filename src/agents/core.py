from dataclasses import dataclass, asdict
from typing import List, Optional
from importlib import import_module

from llama_index.core.agent.workflow import ReActAgent  # , FunctionAgent

from llama_index.core.llms import ChatMessage, MessageRole, TextBlock
from llama_index.core.memory import Memory

from llama_index.core.tools.function_tool import FunctionTool


@dataclass
class LLMConfig:
    """Configuration for the LLM model."""

    model: str = "gpt-4o"
    api_key: Optional[str] = None
    temperature: float = 0
    project: Optional[str] = None
    location: Optional[str] = None
    base_url: Optional[str] = None
    max_tokens: Optional[int] = None

    @classmethod
    def from_dict(cls, config: dict) -> "LLMConfig":
        """Create LLMConfig from dictionary."""
        return cls(**config)

    def to_dict(self) -> dict:
        """Convert to dictionary, filtering None values."""
        config_dict = asdict(self)
        return {k: v for k, v in config_dict.items() if v is not None}


class ChatAgent:
    """ChatAgent class"""

    def __init__(
        self,
        llm_provider: str,
        config: LLMConfig,
        memory_config: dict,
        prompt_template: str,
        tools: Optional[List[FunctionTool]] = None,
    ):
        self.config = config.to_dict()
        self.prompt_template = prompt_template
        self.memory = Memory.from_defaults(**memory_config)

        module = import_module(f"llama_index.llms.{llm_provider}")
        self.llm = module.__dict__[module.__all__[0]](**self.config)

        self.agent = ReActAgent(llm=self.llm, tools=tools)

    async def __call__(self, message: ChatMessage):
        self.memory.put_messages([message])
        res = await self.agent.run(chat_history=self.memory.get())
        self.memory.put_messages(
            [ChatMessage(role=MessageRole.ASSISTANT, blocks=[TextBlock(text=str(res))])]
        )

        return res
