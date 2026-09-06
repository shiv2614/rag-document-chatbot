def load_document(filepath):
    """Reads a text file and returns its full content as a string."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
