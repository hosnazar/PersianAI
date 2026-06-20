from pydantic import BaseModel, Field
from typing import List, Literal

class ChatMessage(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    history: List[ChatMessage] = []

class ChatResponse(BaseModel):
    answer: str
    provider: str
    model: str
