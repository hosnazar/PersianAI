import httpx
from app.config import settings
from app.schemas import ChatMessage
from app.knowledge import search_local_knowledge

SYSTEM_PROMPT = """
تو یک دستیار هوش مصنوعی فارسی‌زبان هستی.
پاسخ‌ها باید دقیق، عملی، بدون ادعای ساختگی و قابل اجرا باشند.
اگر مطمئن نیستی، صریح بگو.
""".strip()

async def ask_ollama(message: str, history: list[ChatMessage]) -> str:
    knowledge_chunks = search_local_knowledge(message)
    context = "\n\n".join(knowledge_chunks)
    system_prompt = SYSTEM_PROMPT
    if context:
        system_prompt += "\n\nاز کانتکست محلی زیر فقط وقتی مرتبط است استفاده کن و منبع را نام ببر:\n" + context

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend([m.model_dump() for m in history[-10:]])
    messages.append({"role": "user", "content": message})

    payload = {
        "model": settings.ollama_model,
        "messages": messages,
        "stream": False,
    }

    url = f"{settings.ollama_base_url}/api/chat"
    try:
        async with httpx.AsyncClient(timeout=120) as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("message", {}).get("content", "")
    except httpx.ConnectError as exc:
        raise RuntimeError("Ollama is not running. Start it with: ollama serve") from exc
    except httpx.HTTPStatusError as exc:
        raise RuntimeError(f"Ollama error: {exc.response.text}") from exc

async def ask_llm(message: str, history: list[ChatMessage]) -> str:
    if settings.llm_provider == "ollama":
        return await ask_ollama(message, history)
    raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")
