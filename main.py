from loader import load_document
from chunker import chunk_text
from retriever import retrieve
from llm import ask_llm

DOCUMENT_PATH = "sample.txt"


def main():
    doc_text = load_document(DOCUMENT_PATH)
    chunks = chunk_text(doc_text)
    print(f"Loaded document with {len(doc_text.split())} words, split into {len(chunks)} chunks.\n")

    while True:
        query = input("Ask a question (or type 'quit' to stop): ")
        if query.lower() == "quit":
            break
        relevant_chunks = retrieve(query, chunks)
        answer = ask_llm(query, relevant_chunks)
        print(f"\nAnswer: {answer}\n")


if __name__ == "__main__":
    main()
