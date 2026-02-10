# Module 05 - Exercises

## Overview

Hands-on exercises to practice embeddings and vector databases.

## Completed Exercises

### ✅ Exercise 01: First Embedding
**File**: `01-first-embedding.py`

Practice generating embeddings and calculating similarity.

**Topics**:
- OpenAI vs Sentence Transformers
- Embedding dimensions
- Cosine similarity
- Batch processing

### ✅ Exercise 02: Chroma Setup  
**File**: `02-chroma-setup.py`

Master ChromaDB for vector storage.

**Topics**:
- Collection management
- CRUD operations
- Metadata filtering
- Persistence

## Exercises to Complete

### 📝 Exercise 03: Semantic Search
Build a production semantic search engine with ChromaDB and embeddings.

### 📝 Exercise 04: Document Chunking
Implement smart document chunking strategies for optimal retrieval.

### 📝 Exercise 05: Classification
Create a text classifier using embeddings and machine learning.

### 📝 Exercise 06: Recommendations
Build a content recommendation system using vector similarity.

## Getting Started

```bash
# Activate virtual environment
source ../../.venv/bin/activate

# Run an exercise
python 01-first-embedding.py

# Run tests
pytest test_exercises.py -v
```

## Learning Path

1. **Start with notebooks** (`../notebooks/`) - Learn concepts interactively
2. **Complete exercises** - Practice with TODO-guided coding
3. **Run tests** - Verify your implementations
4. **Review solutions** - Compare approaches (when available)

## Requirements

- OpenAI API key (for exercises using OpenAI embeddings)
- ChromaDB installed
- Sentence Transformers (for local embeddings)

Set up `.env` file:
```
OPENAI_API_KEY=your_key_here
```

## Success Criteria

For each exercise, you should be able to:
- ✅ Pass all built-in tests
- ✅ Understand the code you wrote
- ✅ Explain the concepts used
- ✅ Extend the solution with new features

## Help & Resources

- **Notebooks**: See `../notebooks/` for detailed tutorials
- **Documentation**: 
  - [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
  - [ChromaDB Docs](https://docs.trychroma.com/)
  - [Sentence Transformers](https://www.sbert.net/)

## Notes

- Exercises 01-02 are complete with TODO markers
- Exercises 03-06 concepts are covered in notebooks 03-06
- Students can implement remaining exercises following notebook patterns
- All key concepts are thoroughly covered in the 6 notebooks

---

**Tip**: Don't skip the notebooks! They contain essential context and examples that make the exercises much easier to complete.
