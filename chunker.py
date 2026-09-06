def chunk_text(text, chunk_size=100, overlap=20):
    """
    Splits text into overlapping word chunks.
    Overlap helps preserve context that might otherwise be cut mid-thought.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        if chunk:
            chunks.append(chunk)
    return chunks
