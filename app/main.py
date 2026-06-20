from fastapi import FastAPI, HTTPException
from app.config import settings
from app.schemas import ChatRequest, ChatResponse
from app.llm import ask_llm

app = FastAPI(title=settings.app_name)

@app.get("/health")
def health():
    return {"status": "ok", "app": settings.app_name}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        answer = await ask_llm(request.message, request.history)
        return ChatResponse(
            answer=answer,
            provider=settings.llm_provider,
            model=settings.ollama_model,
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
