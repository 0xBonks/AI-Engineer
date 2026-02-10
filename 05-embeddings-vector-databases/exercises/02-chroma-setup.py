"""
Module 05 - Exercise 02: Chroma Setup
======================================

Task: Set up and use ChromaDB for vector storage and retrieval.

Learning Objectives:
- Initialize ChromaDB client and collections
- Add documents with embeddings
- Query with semantic search
- Use metadata filtering
- Implement persistence

Instructions:
-------------
1. Complete the ChromaManager class
2. Implement CRUD operations
3. Add metadata filtering
4. Test persistence

Success Criteria:
-----------------
- Successfully create and manage collections
- Add and retrieve documents
- Query with metadata filters
- Persist data across sessions
"""

import chromadb
from chromadb.config import Settings
from typing import List, Dict, Optional
from dataclasses import dataclass
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


@dataclass
class SearchResult:
    """Container for search results."""
    document: str
    distance: float
    metadata: Dict
    id: str


class ChromaManager:
    """Manage ChromaDB collections and operations."""
    
    def __init__(self, persist_directory: Optional[str] = None):
        """
        Initialize Chroma client.
        
        Args:
            persist_directory: Path for persistent storage (None = in-memory)
        
        TODO: Implement initialization
        - Create client (persistent or in-memory)
        - Initialize OpenAI client for embeddings
        """
        # Your code here
        pass
    
    def create_collection(
        self,
        name: str,
        metadata: Optional[Dict] = None
    ):
        """
        Create a new collection.
        
        Args:
            name: Collection name
            metadata: Optional collection metadata
        
        Returns:
            Collection object
        
        TODO: Implement this method
        - Use client.create_collection()
        - Handle if collection already exists
        - Return collection
        """
        # Your code here
        pass
    
    def add_documents(
        self,
        collection_name: str,
        documents: List[str],
        metadatas: Optional[List[Dict]] = None,
        ids: Optional[List[str]] = None
    ) -> int:
        """
        Add documents to a collection.
        
        Args:
            collection_name: Target collection
            documents: List of text documents
            metadatas: Optional metadata for each document
            ids: Optional IDs (will generate if not provided)
        
        Returns:
            Number of documents added
        
        TODO: Implement this method
        - Get or create collection
        - Generate embeddings using OpenAI
        - Generate IDs if not provided
        - Add to collection
        - Return count
        """
        # Your code here
        pass
    
    def search(
        self,
        collection_name: str,
        query: str,
        n_results: int = 5,
        where: Optional[Dict] = None
    ) -> List[SearchResult]:
        """
        Search a collection.
        
        Args:
            collection_name: Collection to search
            query: Search query
            n_results: Number of results
            where: Metadata filter (e.g., {"category": "tech"})
        
        Returns:
            List of SearchResult objects
        
        TODO: Implement this method
        - Get collection
        - Generate query embedding
        - Query collection (with filter if provided)
        - Return SearchResult objects
        """
        # Your code here
        pass
    
    def update_document(
        self,
        collection_name: str,
        doc_id: str,
        new_text: str,
        new_metadata: Optional[Dict] = None
    ):
        """
        Update an existing document.
        
        Args:
            collection_name: Collection name
            doc_id: Document ID to update
            new_text: New document text
            new_metadata: New metadata
        
        TODO: Implement this method
        - Get collection
        - Generate new embedding
        - Update document
        """
        # Your code here
        pass
    
    def delete_document(self, collection_name: str, doc_id: str):
        """
        Delete a document.
        
        Args:
            collection_name: Collection name
            doc_id: Document ID to delete
        
        TODO: Implement this method
        - Get collection
        - Delete by ID
        """
        # Your code here
        pass
    
    def get_collection_stats(self, collection_name: str) -> Dict:
        """
        Get statistics about a collection.
        
        Args:
            collection_name: Collection name
        
        Returns:
            Dictionary with stats (count, metadata, etc.)
        
        TODO: Implement this method
        - Get collection
        - Count documents
        - Get metadata
        - Return stats dict
        """
        # Your code here
        pass
    
    def list_collections(self) -> List[str]:
        """
        List all collections.
        
        Returns:
            List of collection names
        
        TODO: Implement this method
        - Use client.list_collections()
        - Extract names
        - Return list
        """
        # Your code here
        pass


def test_chroma_manager():
    """Test the ChromaManager class."""
    
    print("Test 1: Create collection...")
    manager = ChromaManager()  # In-memory for testing
    collection = manager.create_collection("test_collection")
    assert collection is not None, "Should create collection"
    print("✓ Collection created")
    
    print("\nTest 2: Add documents...")
    docs = [
        "Python is a programming language",
        "Machine learning is awesome",
        "The weather is nice today"
    ]
    metadata = [
        {"category": "tech"},
        {"category": "tech"},
        {"category": "weather"}
    ]
    count = manager.add_documents("test_collection", docs, metadata)
    assert count == 3, "Should add 3 documents"
    print(f"✓ Added {count} documents")
    
    print("\nTest 3: Search...")
    results = manager.search("test_collection", "AI programming", n_results=2)
    assert len(results) > 0, "Should return results"
    print(f"✓ Found {len(results)} results")
    for r in results:
        print(f"  [{r.distance:.3f}] {r.document[:50]}...")
    
    print("\nTest 4: Metadata filtering...")
    filtered = manager.search(
        "test_collection",
        "technology",
        where={"category": "tech"}
    )
    assert len(filtered) > 0, "Should return filtered results"
    print(f"✓ Filtered search returned {len(filtered)} results")
    
    print("\nTest 5: Collection stats...")
    stats = manager.get_collection_stats("test_collection")
    assert "count" in stats, "Should have count"
    print(f"✓ Collection has {stats['count']} documents")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    # TODO: Complete the implementation and run tests
    # test_chroma_manager()
    
    # Example usage:
    # manager = ChromaManager(persist_directory="./chroma_data")
    # manager.create_collection("my_docs")
    # manager.add_documents("my_docs", ["doc1", "doc2"])
    # results = manager.search("my_docs", "query")
    
    print("TODO: Implement the ChromaManager class")
    print("Run test_chroma_manager() when complete")
