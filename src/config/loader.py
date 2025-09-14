from typing import Optional, List
from llama_index.core.tools.function_tool import FunctionTool

from src.agents.core import ChatAgent, LLMConfig


def load_toml(filename: Optional[str] = None):
    import os
    import jinja2
    import toml

    from src.config import settings

    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(filename) or "."))
    template = environment.get_template(os.path.basename(filename))
    rendered = template.render(settings.__dict__)
    return toml.loads(rendered)

async def agent_from_config(CONFIG, tools: Optional[List[FunctionTool]] = None) -> ChatAgent:
    return ChatAgent(
        prompt_template=CONFIG["prompt"],
        llm_provider=CONFIG["model"]["provider"],
        config=LLMConfig.from_dict(CONFIG["model"]["config"]),
        memory_config=CONFIG["model"]["memory"],
        tools=tools
    )