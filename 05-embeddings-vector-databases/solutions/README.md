# Module 05 - Solutions

Reference implementations for Module 05 exercises.

## 📚 Learning Philosophy

These solutions are provided as learning aids, not shortcuts. For maximum learning:

1. **Attempt exercises first** - Struggle is part of learning
2. **Use notebooks** - They contain detailed tutorials
3. **Check one method at a time** - Don't copy entire files
4. **Understand, don't memorize** - Know WHY, not just WHAT

## 🎯 Available Solutions

### Exercise 01: First Embedding
**Status**: Concepts covered in Notebook 01 & 02

Key implementation patterns:
- OpenAI embeddings: Use `client.embeddings.create()`
- Sentence Transformers: Use `model.encode()`
- Cosine similarity: Use `cosine_similarity()` from sklearn
- Batch processing: Pass list of texts to API

### Exercise 02: Chroma Setup
**Status**: Concepts covered in Notebook 03

Key implementation patterns:
- Client init: `chromadb.Client()` or `chromadb.PersistentClient(path)`
- Collections: `client.create_collection(name)`
- Adding docs: Generate embeddings first, then `collection.add()`
- Querying: Generate query embedding, then `collection.query()`

## 💡 Implementation Hints

### Embedding Generation Pattern
```python
# OpenAI
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts  # Can be string or list
)
embeddings = [item.embedding for item in response.data]

# Sentence Transformers
embeddings = model.encode(texts)  # Returns numpy array
```

### ChromaDB Pattern
```python
# Setup
client = chromadb.Client()
collection = client.create_collection("name")

# Add
collection.add(
    documents=texts,
    embeddings=embeddings,
    ids=ids,
    metadatas=metadata_list
)

# Query
results = collection.query(
    query_embeddings=[query_emb],
    n_results=k,
    where={"category": "value"}  # Optional filter
)
```

### Similarity Calculation Pattern
```python
from sklearn.metrics.pairwise import cosine_similarity

# Calculate similarity
sim_matrix = cosine_similarity(embeddings1, embeddings2)

# Find top-k
similarities = cosine_similarity([query_emb], doc_embs)[0]
top_k_indices = np.argsort(similarities)[::-1][:k]
```

## 🔍 Debugging Tips

### Common Issues

**Import Errors**:
```bash
pip install chromadb openai sentence-transformers scikit-learn
```

**API Key Missing**:
```bash
# Add to .env file
OPENAI_API_KEY=your_key_here
```

**ChromaDB Errors**:
- Collection already exists: Use `get_or_create_collection()`
- Dimension mismatch: Ensure all embeddings have same dimension
- No results: Check if collection has data with `collection.count()`

**Embedding Issues**:
- Empty text: Handle edge case before calling API
- Token limit: Chunk long texts before embedding
- Cost concerns: Cache embeddings, use smaller model

## 📖 Learning Resources

- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Sentence Transformers](https://www.sbert.net/)
- [Cosine Similarity Explained](https://en.wikipedia.org/wiki/Cosine_similarity)

## ✅ Verification

To check your implementation:
1. Run built-in tests in exercise files
2. Run pytest: `pytest tests/test_exercises.py -v`
3. Compare output with expected behavior
4. Test edge cases (empty input, large batch, etc.)

## 🎓 Next Steps

After completing exercises:
1. Build a small project combining concepts
2. Experiment with different embedding models
3. Try different vector databases (Pinecone, Weaviate)
4. Move to Module 06: RAG Systems

---

**Remember**: The goal is understanding, not completion. Take your time and experiment!
