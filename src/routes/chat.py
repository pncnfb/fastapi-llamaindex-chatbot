from fastapi import APIRouter, Request
from llama_index.core.llms import ChatMessage

from src.models.chat import Response

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/send_message")
async def send_message(req: Request, prompt:ChatMessage):
    return await req.app.state.agent__test(prompt)


@router.post("/test", response_model=ChatMessage)
async def test(req: Request,tone_of_voice: str, user_request: str):
    return req.app.state.agent__test(output_cls=Response, tone_of_voice=tone_of_voice, richiesta_utente=user_request)