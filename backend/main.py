from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_logic import create_qa_chain
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Your frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize QA chain at startup instead of top level
qa_chain = None

@app.on_event("startup")
async def startup_event():
    global qa_chain
    logger.info("Starting QA chain initialization...")
    try:
        qa_chain = create_qa_chain()
        logger.info("QA chain initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize QA chain: {str(e)}")
        raise

class Question(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "RAG Langchain API is running 🚀"}

@app.post("/ask")
def ask_question(q: Question):
    if qa_chain is None:
        logger.error("QA chain not initialized")
        return {"error": "Service not ready. Please try again later."}
    
    try:
        result = qa_chain(q.query)
        sources = [doc.page_content[:200] for doc in result["source_documents"]]  # Limit preview
        return {
            "question": q.query,
            "answer": result["result"],
            "sources": sources
        }
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}")
        return {
            "question": q.query,
            "error": "An error occurred while processing your question.",
            "sources": []
        }
