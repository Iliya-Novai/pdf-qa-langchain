
# pdf-qa-langchain
PDF question answering with LangChain, FAISS, Hugging Face and Groq.

A document question-answering application built with Python, Streamlit, LangChain, FAISS, Hugging Face embeddings, and Groq.

## Overview

Upload a PDF document and ask questions about its content. The application extracts text, splits it into chunks, creates vector embeddings, retrieves relevant passages, and uses a Groq-hosted language model to generate an answer based on the retrieved context.

## Tech Stack

- **Python** — application logic
- **Streamlit** — interactive web interface
- **PyPDF2** — PDF text extraction
- **LangChain** — LLM and retrieval integration
- **Hugging Face** — text embeddings
- **FAISS** — vector similarity search
- **Groq API** — language model inference

## Features

- PDF upload and text extraction
- Text chunking with overlap
- Semantic similarity search
- Context-based question answering
- Environment-variable configuration for API credentials

## Getting Started

### 1. Clone the repository

```bash
git clone git@github.com:Iliya-Novai/pdf-qa-langchain.git
cd pdf-qa-langchain
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file using `.env.example` as a template, then add your own Groq API key.

Never commit your real API key.

### 5. Run the application

```bash
streamlit run app.py
```

## How It Works

1. Extract text from the uploaded PDF.
2. Split the text into overlapping chunks.
3. Generate embeddings for the chunks.
4. Retrieve relevant chunks using FAISS.
5. Send the retrieved context and user's question to the language model.
6. Display the generated answer in Streamlit.

## Security and Limitations

- API credentials must remain private.
- Answers depend on the quality of the extracted PDF text and retrieved context.
- Scanned PDFs may require OCR, which is not currently included.
- The application should not be considered a substitute for checking important information against the original document.

## License

No license has been selected yet.
