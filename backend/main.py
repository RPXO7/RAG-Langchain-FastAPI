from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_logic import create_qa_chain

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # Your frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
qa_chain = create_qa_chain()

class Question(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "RAG Langchain API is running 🚀"}

@app.post("/ask")
def ask_question(q: Question):
    result = qa_chain(q.query)

    sources = [doc.page_content[:200] for doc in result["source_documents"]]  # Limit preview
    return {
        "question": q.query,
        "answer": result["result"],
        "sources": sources
    }
