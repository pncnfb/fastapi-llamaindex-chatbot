from pydantic import BaseModel

class Response(BaseModel):
    role: str = "ai"
    text: str
    umore: str
