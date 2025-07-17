import os
import logging
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import UnstructuredPDFLoader

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

DB_DIR = "db"
PDF_PATH = "data/example.pdf"

# Load PDF & prepare Chroma DB
def load_or_create_vector_db():
    logger.info("Starting vector database initialization...")
    
    # Check for API key
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if google_api_key is None:
        logger.error("GOOGLE_API_KEY environment variable not set")
        raise ValueError("GOOGLE_API_KEY environment variable not set")
    
    # Set API key for Google libraries
    os.environ["GOOGLE_API_KEY"] = google_api_key
    
    try:
        logger.info("Initializing embeddings model...")
        embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        
        # Check if vector database already exists
        if os.path.exists(DB_DIR) and os.listdir(DB_DIR):
            logger.info(f"Loading existing vector database from {DB_DIR}")
            vectordb = Chroma(persist_directory=DB_DIR, embedding_function=embedding)
        else:
            logger.info(f"Creating new vector database from {PDF_PATH}")
            
            # Check if PDF file exists
            if not os.path.exists(PDF_PATH):
                logger.error(f"PDF file not found: {PDF_PATH}")
                raise FileNotFoundError(f"PDF file not found: {PDF_PATH}")
            
            # Load and process documents
            logger.info("Loading PDF documents...")
            loader = UnstructuredPDFLoader(PDF_PATH)
            documents = loader.load()
            logger.info(f"Loaded {len(documents)} documents from PDF")
            
            # Create vector database
            vectordb = Chroma.from_documents(documents, embedding, persist_directory=DB_DIR)
            logger.info("Vector database created and persisted successfully")
        
        return vectordb
    
    except Exception as e:
        logger.error(f"Error in load_or_create_vector_db: {str(e)}")
        raise

# Initialize LLM + RAG chain
def create_qa_chain():
    logger.info("Creating QA chain...")
    
    try:
        # Load or create vector database
        vectordb = load_or_create_vector_db()
        retriever = vectordb.as_retriever()
        
        # Initialize LLM
        logger.info("Initializing LLM...")
        llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-2.0-flash")
        
        # Create QA chain
        logger.info("Building retrieval QA chain...")
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=True
        )
        
        logger.info("QA chain created successfully")
        return qa_chain
    
    except Exception as e:
        logger.error(f"Error in create_qa_chain: {str(e)}")
        raise
