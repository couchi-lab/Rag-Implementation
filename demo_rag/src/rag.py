from sentence_transformers import CrossEncoder

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq

from src.config import CHROMA_PATH, MODEL_NAME, AI_KEY, MODEL
print("CHROMA_PATH:", CHROMA_PATH)
print("MODEL_NAME:", MODEL_NAME)
print("AI_KEY:", AI_KEY)
print("MODEL:", MODEL)


embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embeddings
)

retriever = db.as_retriever(
    search_kwargs={"k": 5}
)

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

llm = ChatGroq(
  
    api_key=AI_KEY,
    model=MODEL
)

def ask(question):

    docs = retriever.invoke(question)

    pairs = [
        (question, doc.page_content)
        for doc in docs
    ]

    scores = reranker.predict(pairs)

    ranked = sorted(
        zip(docs, scores),
        key=lambda x: x[1],
        reverse=True
    )

    top_docs = ranked[:3]

    context = "\n\n".join(
        doc.page_content
        for doc, score in top_docs
    )

    prompt = f"""
    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = llm.invoke(prompt)

    return response.content