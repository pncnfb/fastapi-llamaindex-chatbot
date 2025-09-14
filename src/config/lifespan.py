from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.config.loader import load_toml
from src.config.loader import agent_from_config
from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec


@asynccontextmanager
async def lifespan(app: FastAPI):
    # initialize resources pre-run
    print("-- init resources --")

    ddg_spec = DuckDuckGoSearchToolSpec()
    tools = ddg_spec.to_tool_list()
    app.state.agent__test = await agent_from_config(load_toml("configs/config__agent.toml"), tools)

    yield  # running state
