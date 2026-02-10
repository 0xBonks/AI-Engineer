"""
Module 05 - Test Suite
=======================

Tests for embeddings and vector database exercises.

Run with: pytest test_exercises.py -v
"""

import pytest
import sys
from pathlib import Path

# Add exercises directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "exercises"))


class TestSetup:
    """Test environment setup."""
    
    def test_imports(self):
        """Test required packages are installed."""
        try:
            import chromadb
            import openai
            from sentence_transformers import SentenceTransformer
            from sklearn.metrics.pairwise import cosine_similarity
            assert True
        except ImportError as e:
            pytest.fail(f"Missing required package: {e}")
    
    def test_env_variables(self):
        """Test API keys are configured."""
        import os
        from dotenv import load_dotenv
        
        load_dotenv()
        
        if not os.getenv("OPENAI_API_KEY"):
            pytest.skip("OPENAI_API_KEY not configured")


class TestExerciseFiles:
    """Test exercise files exist."""
    
    @pytest.mark.parametrize("exercise_num", [1, 2])
    def test_exercise_exists(self, exercise_num):
        """Test exercise file exists."""
        exercise_names = [
            "first-embedding",
            "chroma-setup",
        ]
        
        if exercise_num > len(exercise_names):
            pytest.skip(f"Exercise {exercise_num} not yet created")
        
        exercise_file = (
            Path(__file__).parent.parent / "exercises" /
            f"0{exercise_num}-{exercise_names[exercise_num-1]}.py"
        )
        
        assert exercise_file.exists(), f"Exercise file {exercise_file} not found"


class TestEmbeddings:
    """Tests for embedding functionality."""
    
    def test_sentence_transformer_basic(self):
        """Test basic embedding generation."""
        from sentence_transformers import SentenceTransformer
        import numpy as np
        
        model = SentenceTransformer('all-MiniLM-L6-v2')
        text = "Test embedding"
        embedding = model.encode(text)
        
        assert isinstance(embedding, np.ndarray)
        assert len(embedding) == 384  # Model dimension
    
    def test_cosine_similarity(self):
        """Test similarity calculation."""
        from sentence_transformers import SentenceTransformer
        from sklearn.metrics.pairwise import cosine_similarity
        
        model = SentenceTransformer('all-MiniLM-L6-v2')
        emb1 = model.encode(["cat"])
        emb2 = model.encode(["dog"])
        emb3 = model.encode(["computer"])
        
        # Cat and dog should be more similar than cat and computer
        sim_cat_dog = cosine_similarity(emb1, emb2)[0][0]
        sim_cat_computer = cosine_similarity(emb1, emb3)[0][0]
        
        assert sim_cat_dog > sim_cat_computer


class TestChromaDB:
    """Tests for ChromaDB functionality."""
    
    def test_chroma_basic(self):
        """Test basic ChromaDB operations."""
        import chromadb
        
        client = chromadb.Client()
        collection = client.create_collection("test")
        
        # Add a document
        collection.add(
            documents=["test document"],
            ids=["1"],
            embeddings=[[0.1] * 384]  # Dummy embedding
        )
        
        assert collection.count() == 1
    
    def test_chroma_query(self):
        """Test ChromaDB querying."""
        import chromadb
        import numpy as np
        
        client = chromadb.Client()
        collection = client.create_collection("test_query")
        
        # Add documents with embeddings
        docs = ["doc1", "doc2", "doc3"]
        embeddings = np.random.rand(3, 384).tolist()
        
        collection.add(
            documents=docs,
            embeddings=embeddings,
            ids=["1", "2", "3"]
        )
        
        # Query
        query_embedding = np.random.rand(384).tolist()
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=2
        )
        
        assert len(results['documents'][0]) == 2


# Placeholder tests for student implementations
class TestStudentExercises:
    """Tests for student implementations."""
    
    def test_embedding_generator_placeholder(self):
        """TODO: Test EmbeddingGenerator from Exercise 01."""
        pytest.skip("Complete Exercise 01 to enable this test")
    
    def test_chroma_manager_placeholder(self):
        """TODO: Test ChromaManager from Exercise 02."""
        pytest.skip("Complete Exercise 02 to enable this test")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
