# Module 05: Embeddings & Vector Databases

## Overview

Learn how to transform text into numerical vectors (embeddings) and store them in vector databases for semantic search. Master similarity matching, chunking strategies, and build real-world applications like semantic search, classification, and recommendation systems.

## Learning Objectives

By completing this module, you will be able to:

- Generate embeddings using OpenAI API and Sentence Transformers
- Set up and use Chroma vector database for storing and querying embeddings
- Implement vector similarity search and understand cosine similarity
- Apply appropriate chunking and indexing strategies for performance
- Build semantic search, classification, and recommendation use cases using embeddings

## Prerequisites

- **Completed**: Module 03 (AI Fundamentals & OpenAI API)
- **Required**: Understanding of API calls and data processing
- **Recommended**: Basic linear algebra concepts (vectors, dot products)

## Estimated Time

**10-12 hours** to complete all exercises and demos

## Key Concepts

### 1. Understanding Embeddings
- What are embeddings and why they matter
- Text to vector transformation
- Embedding dimensions (768, 1536, etc.)
- Semantic similarity vs keyword matching
- Pre-trained vs custom embeddings
- Embedding models comparison

### 2. Creating Embeddings
- OpenAI Embeddings API
- text-embedding-3-small vs text-embedding-3-large
- Sentence Transformers (all-MiniLM, etc.)
- Batch processing for efficiency
- Cost considerations
- Caching strategies

### 3. Vector Databases
- Why vector databases over traditional DBs
- Chroma setup and configuration
- Collections and metadata
- Indexing strategies
- Persistence and backup
- Alternative options: Pinecone, Weaviate, FAISS

### 4. Similarity Search
- Cosine similarity explained
- k-NN (k-nearest neighbors) search
- Distance metrics (cosine, euclidean, dot product)
- Threshold tuning
- Handling edge cases
- Performance optimization

### 5. Chunking Strategies
- Why chunking matters
- Fixed-size vs semantic chunking
- Overlap strategies
- Chunk size optimization
- Metadata preservation
- Document preprocessing

## Structure

```
05-embeddings-vector-databases/
├── README.md                                  # This file
├── notebooks/                                 # Interactive tutorials
│   ├── 01-embeddings-basics.ipynb
│   ├── 02-openai-embeddings.ipynb
│   ├── 03-vector-databases.ipynb
│   ├── 04-similarity-search.ipynb
│   ├── 05-chunking-strategies.ipynb
│   └── 06-real-world-applications.ipynb
├── exercises/                                 # Hands-on challenges
│   ├── 01-first-embedding.py
│   ├── 02-chroma-setup.py
│   ├── 03-semantic-search.py
│   ├── 04-document-chunking.py
│   ├── 05-classification.py
│   └── 06-recommendations.py
├── tests/                                     # Automated validation
│   └── test_exercises.py
└── solutions/                                 # Reference implementations
    └── solutions/
```

## Topics Covered

### Embeddings Fundamentals
- **Concept**: Convert text to high-dimensional vectors
- **Use Case**: Capture semantic meaning, not just keywords
- **Example**: "car" and "automobile" have similar embeddings

### Vector Databases
- **Concept**: Specialized storage for vector similarity search
- **Use Case**: Efficiently find similar items in large datasets
- **Example**: Search 1M documents in milliseconds

### Semantic Search
- **Concept**: Search by meaning, not exact words
- **Use Case**: Better search than keyword matching
- **Example**: Query "CEO" finds "Chief Executive Officer"

### Document Chunking
- **Concept**: Split large texts into searchable pieces
- **Use Case**: Process documents larger than context window
- **Example**: Split 100-page PDF into 500-word chunks

### Classification
- **Concept**: Use embeddings for zero-shot classification
- **Use Case**: Categorize content without training
- **Example**: Classify support tickets by department

## Exercises

### Exercise 1: First Embedding
**File**: `exercises/01-first-embedding.py`

Create your first embeddings using OpenAI API.

**Success Criteria**:
- Generate embeddings for sample texts
- Understand embedding dimensions
- Compare similar vs dissimilar texts

### Exercise 2: Chroma Setup
**File**: `exercises/02-chroma-setup.py`

Set up Chroma vector database and store embeddings.

**Success Criteria**:
- Initialize Chroma collection
- Add documents with metadata
- Persist database to disk

### Exercise 3: Semantic Search
**File**: `exercises/03-semantic-search.py`

Build a semantic search system for a document collection.

**Success Criteria**:
- Index 100+ documents
- Query returns semantically relevant results
- Compare with keyword search

### Exercise 4: Document Chunking
**File**: `exercises/04-document-chunking.py`

Implement chunking strategies for large documents.

**Success Criteria**:
- Chunk documents with overlap
- Preserve metadata
- Optimize chunk size for retrieval

### Exercise 5: Classification
**File**: `exercises/05-classification.py`

Build a zero-shot text classifier using embeddings.

**Success Criteria**:
- Define categories as embeddings
- Classify new texts
- Measure accuracy

### Exercise 6: Recommendations
**File**: `exercises/06-recommendations.py`

Create a recommendation system using vector similarity.

**Success Criteria**:
- Embed items and user preferences
- Find similar items
- Generate recommendations

## Resources

### Official Documentation
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [Chroma Documentation](https://docs.trychroma.com/)
- [Sentence Transformers](https://www.sbert.net/)

### Vector Database Options
- [Chroma](https://www.trychroma.com/) - Open source, Python-friendly
- [Pinecone](https://www.pinecone.io/) - Managed, scalable
- [Weaviate](https://weaviate.io/) - Open source, GraphQL
- [FAISS](https://github.com/facebookresearch/faiss) - Facebook's library

### Recommended Reading
- [Embeddings: What, Why, How](https://vickiboykis.com/what_are_embeddings/)
- [Vector Database Comparison](https://benchmark.vectorview.ai/)

## Next Steps

After completing this module:

1. ✅ Build semantic search for your own documents
2. ✅ Experiment with different chunking strategies
3. ➡️ Proceed to **Module 06: RAG Systems**

## Code Patterns

### Creating Embeddings
```python
from openai import OpenAI

client = OpenAI()

def create_embedding(text: str, model: str = "text-embedding-3-small") -> list[float]:
    """Generate embedding for given text."""
    response = client.embeddings.create(
        input=text,
        model=model
    )
    return response.data[0].embedding

# Batch processing for efficiency
def create_embeddings_batch(texts: list[str]) -> list[list[float]]:
    response = client.embeddings.create(
        input=texts,  # Up to 2048 texts at once
        model="text-embedding-3-small"
    )
    return [item.embedding for item in response.data]
```

### Chroma Setup
```python
import chromadb

# Initialize client
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name="my_documents",
    metadata={"description": "Document embeddings"}
)

# Add documents
collection.add(
    documents=["Document text here..."],
    embeddings=[[0.1, 0.2, 0.3, ...]],  # Your embeddings
    metadatas=[{"source": "file.pdf", "page": 1}],
    ids=["doc1"]
)

# Query
results = collection.query(
    query_embeddings=[[0.1, 0.2, 0.3, ...]],
    n_results=5
)
```

### Semantic Search
```python
def semantic_search(query: str, collection, top_k: int = 5):
    """Search documents by semantic similarity."""
    
    # Create query embedding
    query_embedding = create_embedding(query)
    
    # Search vector database
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    
    return results
```

### Document Chunking
```python
def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """Split text into overlapping chunks."""
    
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    
    return chunks
```

## Embedding Model Comparison

| Model | Dimensions | Cost | Best For |
|-------|-----------|------|----------|
| text-embedding-3-small | 1536 | $0.02/1M tokens | Most use cases |
| text-embedding-3-large | 3072 | $0.13/1M tokens | Highest quality |
| all-MiniLM-L6-v2 | 384 | Free (local) | Low resource |
| all-mpnet-base-v2 | 768 | Free (local) | Better quality |

## Chunking Strategies

### Fixed Size Chunking
- **When**: Simple documents, uniform structure
- **Chunk Size**: 500-1000 words
- **Overlap**: 10-20% of chunk size

### Semantic Chunking
- **When**: Preserving meaning is critical
- **Method**: Split at paragraph/section boundaries
- **Overlap**: Natural (e.g., include previous heading)

### Sliding Window
- **When**: Need comprehensive coverage
- **Window Size**: 300-500 words
- **Stride**: 250-400 words (creates overlap)

## Common Issues

### Poor Search Results
- Try different chunk sizes (smaller often better)
- Increase overlap between chunks
- Add more metadata for filtering
- Use better embedding model

### Slow Performance
- Batch embedding creation
- Use smaller embedding models
- Implement caching
- Consider managed vector DB

### High Costs
- Use text-embedding-3-small (cheaper)
- Cache embeddings for reused text
- Batch API calls
- Consider local models

## Notes

- **Cost**: ~$0.02 per 1M tokens for text-embedding-3-small
- **Performance**: Chroma works well up to millions of vectors
- **Quality**: Larger embeddings ≠ always better results
- **Foundation**: This module is prerequisite for RAG systems

---

**Module Status**: 🚧 Content Development | ⬅️ Prev: Open Source AI & Safety | ⏭️ Next: RAG Systems
