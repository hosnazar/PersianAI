from pathlib import Path

KNOWLEDGE_DIR = Path("knowledge_base")


def search_local_knowledge(query: str, limit: int = 3) -> list[str]:
    """Tiny zero-cost keyword retrieval. Replace with embeddings later."""
    if not KNOWLEDGE_DIR.exists():
        return []

    query_terms = {t.strip().lower() for t in query.split() if len(t.strip()) > 2}
    scored: list[tuple[int, str]] = []

    for path in KNOWLEDGE_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        text_lower = text.lower()
        score = sum(1 for term in query_terms if term in text_lower)
        if score > 0:
            scored.append((score, f"Source: {path.name}\n{text[:1500]}"))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [content for _, content in scored[:limit]]
