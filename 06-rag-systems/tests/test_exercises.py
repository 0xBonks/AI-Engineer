"""
Module 06 - Test Suite
=======================

Tests for RAG system implementations.

Run with: pytest test_exercises.py -v
"""

import pytest
import sys
from pathlib import Path


class TestSetup:
    """Test environment setup."""
    
    def test_imports(self):
        """Test RAG packages are installed."""
        try:
            import chromadb
            import openai
            from sentence_transformers import SentenceTransformer
            from langchain.text_splitter import RecursiveCharacterTextSplitter
            from langchain.schema import Document
            assert True
        except ImportError as e:
            pytest.fail(f"Missing required package: {e}")
    
    def test_api_key(self):
        """Test OpenAI API key is configured."""
        import os
        from dotenv import load_dotenv
        
        load_dotenv()
        if not os.getenv("OPENAI_API_KEY"):
            pytest.skip("OPENAI_API_KEY not configured")


class TestRAGComponents:
    """Test individual RAG components."""
    
    def test_embedding_generation(self):
        """Test embedding creation."""
        from sentence_transformers import SentenceTransformer
        
        model = SentenceTransformer('all-MiniLM-L6-v2')
        text = "Test document for RAG"
        embedding = model.encode(text)
        
        assert embedding is not None
        assert len(embedding) == 384
    
    def test_chroma_operations(self):
        """Test ChromaDB basic operations."""
        import chromadb
        
        client = chromadb.Client()
        collection = client.create_collection("test_rag")
        
        # Add document
        collection.add(
            documents=["test doc"],
            ids=["1"],
            embeddings=[[0.1] * 384]
        )
        
        assert collection.count() == 1
        
        # Query
        results = collection.query(
            query_embeddings=[[0.1] * 384],
            n_results=1
        )
        
        assert len(results['documents'][0]) == 1
    
    def test_document_chunking(self):
        """Test text chunking."""
        from langchain.text_splitter import RecursiveCharacterTextSplitter
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=10
        )
        
        long_text = "This is a sentence. " * 20
        chunks = splitter.split_text(long_text)
        
        assert len(chunks) > 1
        assert all(len(chunk) <= 120 for chunk in chunks)  # Allow some overflow


class TestRAGSystem:
    """Test complete RAG system."""
    
    def test_simple_rag_flow(self):
        """Test basic RAG retrieve + generate flow."""
        import chromadb
        from sentence_transformers import SentenceTransformer
        
        # Setup
        client = chromadb.Client()
        collection = client.create_collection("test_simple_rag")
        model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Add documents
        docs = ["Python is a programming language", "AI is the future"]
        embeddings = model.encode(docs).tolist()
        collection.add(
            documents=docs,
            embeddings=embeddings,
            ids=["1", "2"]
        )
        
        # Retrieve
        query = "Tell me about programming"
        query_emb = model.encode(query).tolist()
        results = collection.query(
            query_embeddings=[query_emb],
            n_results=1
        )
        
        assert len(results['documents'][0]) > 0
        assert "Python" in results['documents'][0][0]


class TestStudentImplementations:
    """Placeholder tests for student work."""
    
    def test_student_rag_placeholder(self):
        """TODO: Test student RAG implementation."""
        pytest.skip("Implement your RAG system to enable this test")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
