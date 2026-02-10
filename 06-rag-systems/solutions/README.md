# Module 06 - Solutions & Patterns

## RAG Implementation Guide

This guide provides reference patterns and solutions for building RAG systems.

## Core Patterns

### 1. Basic RAG Pattern (From Notebook 01)

Complete working implementation of SimpleRAG available in `notebooks/01-rag-fundamentals.ipynb`.

**Key Methods:**
- `add_documents()` - Embed and store
- `retrieve()` - Vector search
- `generate()` - LLM with context
- `query()` - End-to-end RAG

### 2. Document Processing Pattern (From Notebook 02)

Complete working pipeline in `notebooks/02-document-processing.ipynb`.

**Key Components:**
- DocumentLoader - Multi-format support
- MetadataExtractor - Auto-extract structured data
- IngestionPipeline - Complete load → store flow

## Framework Implementations

### LangChain RAG

```python
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 1. Load documents
from langchain.document_loaders import TextLoader
loader = TextLoader("document.txt")
docs = loader.load()

# 2. Chunk
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# 3. Create vector store
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=OpenAIEmbeddings()
)

# 4. Create RAG chain
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True
)

# 5. Query
result = qa({"query": "Your question"})
print(result["result"])
print(f"Sources: {len(result['source_documents'])}")
```

### LlamaIndex RAG

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI

# Configure
Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding()

# 1. Load documents
documents = SimpleDirectoryReader("./data").load_data()

# 2. Create index (automatically chunks and embeds)
index = VectorStoreIndex.from_documents(documents)

# 3. Create query engine
query_engine = index.as_query_engine(
    similarity_top_k=3,
    response_mode="compact"
)

# 4. Query
response = query_engine.query("Your question")
print(response.response)
print(f"Sources: {len(response.source_nodes)}")
```

## Advanced Patterns

### Hybrid Search RAG

Combine semantic and keyword search:

```python
from langchain.retrievers import EnsembleRetriever
from langchain.retrievers import BM25Retriever

# Semantic retriever
vector_retriever = vectorstore.as_retriever()

# Keyword retriever
bm25_retriever = BM25Retriever.from_documents(chunks)

# Ensemble (hybrid)
hybrid_retriever = EnsembleRetriever(
    retrievers=[vector_retriever, bm25_retriever],
    weights=[0.7, 0.3]  # 70% semantic, 30% keyword
)

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=hybrid_retriever
)
```

### RAG with Reranking

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

# Base retriever
base_retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

# Reranker
compressor = LLMChainExtractor.from_llm(ChatOpenAI())

# Compressed retriever (retrieves more, returns best)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=compression_retriever
)
```

### Conversational RAG with Memory

```python
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Create memory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Conversational RAG
qa = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(),
    retriever=vectorstore.as_retriever(),
    memory=memory
)

# Multi-turn conversation
qa({"question": "What is Python?"})
qa({"question": "When was it created?"})  # Maintains context
```

## Common Issues & Solutions

### Issue: Poor Retrieval Quality
**Solutions:**
- Optimize chunk size (test 200-1000 chars)
- Use better embeddings (text-embedding-3-large)
- Implement hybrid search
- Add reranking

### Issue: Hallucination
**Solutions:**
- Lower temperature (0.1-0.3)
- Strengthen system prompt
- Add "only use context" instruction
- Validate against sources

### Issue: Slow Performance
**Solutions:**
- Cache embeddings
- Use smaller embedding model
- Reduce chunk overlap
- Optimize chunk size
- Use streaming responses

### Issue: Context Too Large
**Solutions:**
- Reduce k (fewer retrieved docs)
- Use contextual compression
- Implement chunk summarization
- Use models with larger context windows

## Evaluation Metrics

### Retrieval Metrics:
```python
# Precision@K
relevant_retrieved = count_relevant(retrieved_docs[:k])
precision = relevant_retrieved / k

# Recall
recall = relevant_retrieved / total_relevant

# MRR (Mean Reciprocal Rank)
first_relevant_position = find_first_relevant(retrieved_docs)
mrr = 1 / first_relevant_position if first_relevant_position else 0
```

### Generation Metrics:
- Faithfulness: Answer supported by context?
- Relevance: Answer addresses question?
- Completeness: Answer is sufficient?

## Best Practices

1. **Start simple**: Get basic RAG working first
2. **Test thoroughly**: Use diverse questions
3. **Monitor quality**: Track metrics over time
4. **Optimize iteratively**: Improve based on failures
5. **Handle edge cases**: No context, contradictions, outdated info
6. **Cite sources**: Always provide citations
7. **Validate answers**: Check against ground truth when possible

## Additional Resources

- [LangChain Documentation](https://python.langchain.com/docs/)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [RAG Best Practices](https://www.anyscale.com/blog/a-comprehensive-guide-for-building-rag-based-llm-applications-part-1)

---

**All patterns demonstrated in notebooks 01-02!**

Check notebooks for complete working examples.
