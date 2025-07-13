# RAG LangChain FastAPI Application

A modern RAG (Retrieval-Augmented Generation) application built with FastAPI, LangChain, and Google Gemini AI. This application allows users to ask questions about PDF documents and get intelligent, context-aware answers.

## 🚀 Features

- **PDF Document Processing**: Upload and process PDF documents
- **Vector Database**: Chroma vector database for efficient document retrieval
- **Google Gemini AI**: Powered by Google's latest AI models
- **FastAPI Backend**: Modern, fast REST API
- **CORS Enabled**: Ready for frontend integration
- **Interactive Q&A**: Ask questions and get answers with source citations

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python
- **AI/ML**: LangChain, Google Gemini AI
- **Vector Database**: Chroma
- **Document Processing**: Unstructured PDF Loader
- **Frontend**: React (separate repository)

## 📁 Project Structure

```
rag-langchain-app/
├── backend/                 # FastAPI backend
│   ├── main.py             # FastAPI server
│   ├── rag_logic.py        # RAG implementation
│   ├── requirements.txt    # Python dependencies
│   ├── data/              # PDF documents
│   └── db/                # Vector database
├── frontend/               # React frontend
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google AI API key
- PDF document to analyze

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/RPXO7/RAG-Langchain-FastAPI.git
   cd RAG-Langchain-FastAPI/backend
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the backend directory:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Add your PDF document**
   Place your PDF file in `backend/data/example.pdf`

5. **Start the server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd ../frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```

## 📖 API Documentation

Once the backend is running, visit:
- **Interactive API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/

### API Endpoints

- `GET /` - Health check
- `POST /ask` - Ask a question about your document

#### Example Request
```json
{
  "query": "What is this document about?"
}
```

#### Example Response
```json
{
  "question": "What is this document about?",
  "answer": "This document discusses...",
  "sources": ["Relevant text chunks from the PDF..."]
}
```

## 🔧 Configuration

### Environment Variables

- `GOOGLE_API_KEY`: Your Google AI API key

### Vector Database

The application automatically creates and manages a Chroma vector database in the `db/` directory. The database persists between sessions.

## 🛡️ Security

- API keys are stored in `.env` files (not committed to git)
- CORS is configured for frontend integration
- Input validation and sanitization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the RAG framework
- [Google Gemini AI](https://ai.google.dev/) for the AI models
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework
- [Chroma](https://www.trychroma.com/) for the vector database

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub. 