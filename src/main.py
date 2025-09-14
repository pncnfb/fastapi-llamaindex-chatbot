from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.lifespan import lifespan
from src.routes import chat

app = FastAPI(
    title="Chatbot",
    summary="Chatbot",
    version="0.0.1",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)

