import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import UnstructuredPDFLoader

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key is None:
    raise ValueError("GOOGLE_API_KEY environment variable not set")
os.environ["GOOGLE_API_KEY"] = google_api_key

DB_DIR = "db"
PDF_PATH = "data/example.pdf"

# Load PDF & prepare Chroma DB
def load_or_create_vector_db():
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    if os.path.exists(DB_DIR) and len(os.listdir(DB_DIR)) > 0:
        vectordb = Chroma(persist_directory=DB_DIR, embedding_function=embedding)
    else:
        loader = UnstructuredPDFLoader(PDF_PATH)
        documents = loader.load()
        vectordb = Chroma.from_documents(documents, embedding, persist_directory=DB_DIR)
    return vectordb

# Initialize LLM + RAG chain
def create_qa_chain():
    vectordb = load_or_create_vector_db()
    retriever = vectordb.as_retriever()
    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-2.0-flash")

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
