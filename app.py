import os
from dotenv import load_dotenv
import streamlit as st 
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def main():
    load_dotenv()

    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF")

    # upload file
    pdf = st.file_uploader("Upload your PDf", type="pdf")     

    # extract the text 
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        
        if not text.strip():
            st.warning("No readable text found in this PDF.")
            return
        
        # split into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
    
        # create  embeddings  
        embeddings = HuggingFaceEmbeddings(
          model_name="sentence-transformers/all-MiniLM-L6-v2"
        )       
        
        knowledge_base = FAISS.from_texts(chunks, embeddings)
        # Groq chat 
        llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0
        )
        response = llm.invoke("Explain what LangChain is.")
        
        # show user input 
        user_question = st.text_input("Ask a question about your PDF:")
        if user_question:
            docs = knowledge_base.similarity_search(user_question)
            
            context = "\n\n".join(
                doc.page_content for doc in docs
            )
            
            prompt = f"""
            Answer the user's question using only the context below.
            If the answer is not found in the context, say that the provided PDF
            does not conain the answer.
            
            PDF context:
            {context}
            
            User question:
            {user_question}
            """
            
            response = llm.invoke(prompt)
            
            st.write(response.content)
        
            
if __name__ == "__main__":
    main()