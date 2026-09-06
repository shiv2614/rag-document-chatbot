import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

MODEL = "openai/gpt-oss-20b"


def ask_llm(query, context_chunks):
    """
    Sends the retrieved context and user question to the LLM,
    instructing it to answer only from the given context.
    """
    context = "\n\n".join(context_chunks)
    prompt = f"""Answer the question using ONLY the context below.
If the answer isn't in the context, say "I don't have that information."

Context:
{context}

Question: {query}"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
