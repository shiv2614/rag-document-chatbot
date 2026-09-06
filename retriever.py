def retrieve(query, chunks, top_k=2):
    """
    Scores each chunk by keyword overlap with the query and
    returns the top_k most relevant chunks.

    This is a simple keyword-based retriever (v1). It can be upgraded
    later to use embeddings + a vector store (e.g. FAISS, Chroma) for
    semantic similarity instead of exact word overlap.
    """
    query_words = set(query.lower().split())
    scored = []
    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(query_words & chunk_words)
        scored.append((score, chunk))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [c for _, c in scored[:top_k]]
