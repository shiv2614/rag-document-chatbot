# RAG Document Q&A Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions grounded in the content of a document you provide, built with Python and the Groq API.

## What it does

Upload a `.txt` document (in this demo, a fictional candle brand's FAQ), then ask natural-language questions about it. The chatbot:

1. Loads and splits the document into overlapping chunks
2. Retrieves the chunks most relevant to your question (keyword-overlap scoring)
3. Sends those chunks + your question to an LLM (via Groq's API), instructed to answer *only* from the provided context
4. Returns a grounded answer instead of a hallucinated one

## Why I built this

I run e-commerce businesses, and wanted a way to auto-answer common customer questions (burn time, shipping, returns, wholesale) from an internal FAQ document — a real use case that also let me learn RAG fundamentals hands-on. The included sample document uses a fictional brand name for demo purposes.

## Tech stack

- Python 3
- Groq API (`openai/gpt-oss-20b`)
- No vector database in this version — retrieval uses simple keyword overlap scoring (v1). A natural next step would be embeddings + a vector store (FAISS/Chroma) for semantic search.

## Project structure

```
rag-document-chatbot/
├── main.py         # CLI entry point
├── loader.py       # reads the document
├── chunker.py      # splits text into overlapping chunks
├── retriever.py    # scores and returns the most relevant chunks
├── llm.py          # sends context + question to the Groq API
├── sample.txt       # example document (fictional brand FAQ)
├── requirements.txt
└── README.md
```

## How to run it

1. Clone this repo
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set your Groq API key as an environment variable:
   ```
   export GROQ_API_KEY=your_key_here
   ```
   (Get a free key at [console.groq.com](https://console.groq.com))
4. Run it:
   ```
   python main.py
   ```
5. Ask questions, type `quit` to exit.

## Example

```
Ask a question (or type 'quit' to stop): what is your return policy

Answer: Products may be returned within 7 days of delivery if unused and in
original packaging. Refunds are processed within 5-7 business days after
the returned item is received and inspected. Customized or personalized
items are not eligible for return.
```

## Possible improvements

- Swap keyword retrieval for embedding-based semantic search
- Support PDF and multi-file document uploads
- Add a simple web UI (Streamlit/Gradio) instead of CLI
