"""
Module 05 - Exercise 01: First Embedding
=========================================

Task: Create your first embeddings and understand their properties.

Learning Objectives:
- Generate embeddings using different models
- Compare embedding dimensions
- Calculate similarity between texts
- Visualize embeddings

Instructions:
-------------
1. Complete the EmbeddingGenerator class
2. Implement similarity calculations
3. Create visualization functions
4. Test with sample texts

Success Criteria:
-----------------
- Generate embeddings with multiple models
- Calculate cosine similarity correctly
- Visualize embeddings in 2D
- Compare different embedding models
"""

import os
from typing import List, Tuple
from dotenv import load_dotenv
from openai import OpenAI
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from dataclasses import dataclass

load_dotenv()


@dataclass
class EmbeddingResult:
    """Container for embedding results."""
    text: str
    embedding: np.ndarray
    model: str
    dimension: int


class EmbeddingGenerator:
    """Generate and work with text embeddings."""
    
    def __init__(self, use_openai: bool = True):
        """
        Initialize the embedding generator.
        
        Args:
            use_openai: Whether to use OpenAI (True) or local model (False)
        """
        self.use_openai = use_openai
        
        if use_openai:
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            self.model_name = "text-embedding-3-small"
        else:
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            self.model_name = "all-MiniLM-L6-v2"
    
    def generate_embedding(self, text: str) -> EmbeddingResult:
        """
        Generate embedding for a single text.
        
        Args:
            text: Input text
        
        Returns:
            EmbeddingResult object
        
        TODO: Implement this method
        - If use_openai: Use OpenAI API
        - Else: Use Sentence Transformers
        - Return EmbeddingResult with all fields populated
        """
        # Your code here
        pass
    
    def generate_batch(self, texts: List[str]) -> List[EmbeddingResult]:
        """
        Generate embeddings for multiple texts.
        
        Args:
            texts: List of input texts
        
        Returns:
            List of EmbeddingResult objects
        
        TODO: Implement this method
        - Use batch API call for OpenAI (more efficient)
        - Use model.encode() for Sentence Transformers
        - Return list of EmbeddingResult objects
        """
        # Your code here
        pass
    
    def calculate_similarity(
        self,
        text1: str,
        text2: str
    ) -> float:
        """
        Calculate cosine similarity between two texts.
        
        Args:
            text1: First text
            text2: Second text
        
        Returns:
            Similarity score (0-1)
        
        TODO: Implement this method
        - Generate embeddings for both texts
        - Calculate cosine similarity
        - Return single float value
        """
        # Your code here
        pass
    
    def find_most_similar(
        self,
        query: str,
        candidates: List[str],
        top_k: int = 3
    ) -> List[Tuple[str, float]]:
        """
        Find most similar texts to a query.
        
        Args:
            query: Query text
            candidates: List of candidate texts
            top_k: Number of results to return
        
        Returns:
            List of (text, similarity) tuples, sorted by similarity
        
        TODO: Implement this method
        - Generate embeddings for query and all candidates
        - Calculate similarities
        - Sort and return top_k results
        """
        # Your code here
        pass


class EmbeddingVisualizer:
    """Visualize embeddings in 2D."""
    
    @staticmethod
    def reduce_dimensions(embeddings: np.ndarray, n_components: int = 2) -> np.ndarray:
        """
        Reduce embedding dimensions using PCA.
        
        Args:
            embeddings: Array of embeddings (n_samples, n_features)
            n_components: Target dimensions
        
        Returns:
            Reduced embeddings
        
        TODO: Implement this method
        - Use PCA from sklearn
        - Fit and transform embeddings
        - Return reduced array
        """
        # Your code here
        pass
    
    @staticmethod
    def plot_embeddings(
        texts: List[str],
        embeddings: np.ndarray,
        labels: List[str] = None
    ):
        """
        Plot embeddings in 2D space.
        
        Args:
            texts: Original texts
            embeddings: Embedding vectors
            labels: Optional category labels for coloring
        
        TODO: Implement this method
        - Reduce to 2D if needed
        - Create scatter plot
        - Add text annotations
        - Color by labels if provided
        - Use matplotlib
        """
        # Your code here
        pass


def compare_models():
    """
    Compare OpenAI vs local embeddings.
    
    TODO: Implement this function
    - Create generators for both models
    - Test on same texts
    - Compare dimensions, speed, similarity scores
    - Print comparison results
    """
    # Your code here
    pass


def test_embedding_generator():
    """Test the EmbeddingGenerator class."""
    
    print("Test 1: Generate single embedding...")
    gen = EmbeddingGenerator(use_openai=False)  # Use local for testing
    result = gen.generate_embedding("Hello world")
    assert result is not None, "Should return result"
    assert result.embedding is not None, "Should have embedding"
    print(f"✓ Generated {result.dimension}D embedding")
    
    print("\nTest 2: Generate batch...")
    texts = ["First text", "Second text", "Third text"]
    results = gen.generate_batch(texts)
    assert len(results) == 3, "Should return 3 results"
    print(f"✓ Generated {len(results)} embeddings")
    
    print("\nTest 3: Calculate similarity...")
    sim = gen.calculate_similarity("cat", "dog")
    assert 0 <= sim <= 1, "Similarity should be 0-1"
    print(f"✓ Similarity between 'cat' and 'dog': {sim:.3f}")
    
    print("\nTest 4: Find similar texts...")
    query = "machine learning"
    candidates = [
        "artificial intelligence",
        "cooking recipes",
        "neural networks",
        "sports news"
    ]
    results = gen.find_most_similar(query, candidates, top_k=2)
    assert len(results) <= 2, "Should return at most 2 results"
    print(f"✓ Found {len(results)} similar texts")
    for text, score in results:
        print(f"  [{score:.3f}] {text}")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    # TODO: Complete the implementation and run tests
    # test_embedding_generator()
    
    # Example usage:
    # gen = EmbeddingGenerator(use_openai=False)
    # result = gen.generate_embedding("Your text here")
    # print(f"Embedding: {result.embedding[:10]}...")  # First 10 values
    
    # Compare models:
    # compare_models()
    
    print("TODO: Implement the EmbeddingGenerator class")
    print("Run test_embedding_generator() when complete")
