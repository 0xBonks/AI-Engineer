# Module 06: RAG Systems

## Overview

Build production-ready Retrieval-Augmented Generation (RAG) systems that combine vector search with LLMs to create AI applications that answer questions using your own documents. Learn chunking strategies, retrieval optimization, and how to use LangChain and LlamaIndex frameworks.

## Learning Objectives

By completing this module, you will be able to:

- Explain RAG vs fine-tuning tradeoffs and when to use each approach
- Implement document chunking strategies optimized for retrieval quality
- Build complete RAG pipeline (chunk → embed → store → retrieve → generate)
- Use LangChain and LlamaIndex frameworks for RAG implementation
- Evaluate RAG system performance and optimize retrieval relevance

## Prerequisites

- **Completed**: Module 05 (Embeddings & Vector Databases)
- **Required**: Understanding of embeddings, vector search, and LLM APIs
- **Recommended**: Experience with async Python

## Estimated Time

**15-18 hours** to complete all exercises and demos

## Key Concepts

### 1. RAG Fundamentals
- What is Retrieval-Augmented Generation?
- RAG vs fine-tuning comparison
- When to use RAG vs fine-tuning vs both
- RAG architecture components
- Common RAG patterns
- Limitations and challenges

### 2. Document Processing Pipeline
- Ingestion: Loading various formats (PDF, DOCX, HTML)
- Chunking strategies for optimal retrieval
- Metadata extraction and enrichment
- Preprocessing and cleaning
- Handling code, tables, and images
- Update and deletion patterns

### 3. Retrieval Strategies
- Semantic search basics
- Hybrid search (semantic + keyword)
- Metadata filtering
- Reranking techniques
- Contextual compression
- Multi-query retrieval

### 4. Generation with Context
- Prompt construction for RAG
- Context window management
- Citation and source attribution
- Handling insufficient context
- Multi-document synthesis
- Streaming responses with sources

### 5. RAG Frameworks
- LangChain: Chains, retrievers, and agents
- LlamaIndex: Indices, query engines, and routers
- Framework comparison and selection
- Custom vs framework implementations
- Integration patterns

### 6. Evaluation & Optimization
- Retrieval metrics (precision, recall, MRR)
- Generation quality assessment
- End-to-end RAG evaluation
- A/B testing strategies
- Performance optimization
- Cost optimization

## Structure

```
06-rag-systems/
├── README.md                                      # This file
├── notebooks/                                     # Interactive tutorials
│   ├── 01-rag-fundamentals.ipynb
│   ├── 02-document-processing.ipynb
│   ├── 03-retrieval-strategies.ipynb
│   ├── 04-generation-context.ipynb
│   ├── 05-langchain-rag.ipynb
│   ├── 06-llamaindex-rag.ipynb
│   └── 07-evaluation.ipynb
├── exercises/                                     # Hands-on challenges
│   ├── 01-basic-rag.py
│   ├── 02-document-pipeline.py
│   ├── 03-hybrid-search.py
│   ├── 04-citation-rag.py
│   ├── 05-langchain-implementation.py
│   ├── 06-llamaindex-implementation.py
│   └── 07-production-rag.py
├── tests/                                         # Automated validation
│   └── test_exercises.py
└── solutions/                                     # Reference implementations
    └── solutions/
```

## Topics Covered

### RAG vs Fine-Tuning
- **RAG**: Better for knowledge that changes, lower cost, explainable
- **Fine-tuning**: Better for style/format, reasoning patterns
- **Example**: Use RAG for company docs, fine-tune for brand voice

### Document Chunking for RAG
- **Concept**: Split docs to fit context window and optimize retrieval
- **Strategies**: Fixed size, semantic, hierarchical
- **Example**: 500-word chunks with 50-word overlap

### Hybrid Search
- **Concept**: Combine semantic and keyword search
- **Use Case**: Better precision for technical terms
- **Example**: "API error 404" needs keyword matching

### LangChain for RAG
- **Concept**: Framework for chaining LLM operations
- **Components**: Loaders, splitters, retrievers, chains
- **Example**: Build chatbot with document knowledge

### LlamaIndex for RAG
- **Concept**: Framework optimized for data ingestion
- **Components**: Indices, query engines, data connectors
- **Example**: Connect to SQL, APIs, and files

## Exercises

### Exercise 1: Basic RAG
**File**: `exercises/01-basic-rag.py`

Build a simple RAG system from scratch without frameworks.

**Success Criteria**:
- Load and chunk documents
- Store in vector database
- Retrieve relevant chunks for query
- Generate answer with LLM

### Exercise 2: Document Pipeline
**File**: `exercises/02-document-pipeline.py`

Create a robust document processing pipeline.

**Success Criteria**:
- Support multiple file formats
- Extract metadata
- Handle errors gracefully
- Implement update/delete

### Exercise 3: Hybrid Search
**File**: `exercises/03-hybrid-search.py`

Implement hybrid search combining semantic and keyword matching.

**Success Criteria**:
- Use vector search + BM25
- Combine scores intelligently
- Compare with semantic-only

### Exercise 4: Citation RAG
**File**: `exercises/04-citation-rag.py`

Build RAG system that cites sources for answers.

**Success Criteria**:
- Track source documents
- Include citations in response
- Allow source verification

### Exercise 5: LangChain Implementation
**File**: `exercises/05-langchain-implementation.py`

Use LangChain to build a production RAG system.

**Success Criteria**:
- Use LangChain loaders and splitters
- Implement conversational retrieval
- Add memory for multi-turn

### Exercise 6: LlamaIndex Implementation
**File**: `exercises/06-llamaindex-implementation.py`

Use LlamaIndex to build a document query system.

**Success Criteria**:
- Create VectorStoreIndex
- Implement query engine
- Add filtering and metadata

### Exercise 7: Production RAG
**File**: `exercises/07-production-rag.py`

Build a production-ready RAG system with all best practices.

**Success Criteria**:
- Implement caching
- Add error handling
- Include logging and monitoring
- Optimize for cost and latency

## Resources

### Official Documentation
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [LlamaIndex Guides](https://docs.llamaindex.ai/en/stable/)
- [OpenAI RAG Best Practices](https://platform.openai.com/docs/guides/retrieval-augmented-generation)

### Frameworks
- [LangChain](https://github.com/langchain-ai/langchain)
- [LlamaIndex](https://github.com/run-llama/llama_index)
- [Haystack](https://haystack.deepset.ai/)

### Recommended Reading
- [RAG Paper (Original)](https://arxiv.org/abs/2005.11401)
- [RAG Survey 2024](https://arxiv.org/abs/2312.10997)
- [Advanced RAG Techniques](https://towardsdatascience.com/advanced-rag-techniques-an-illustrated-overview-04d193d8fec6)

## Next Steps

After completing this module:

1. ✅ Build RAG system for your own documents
2. ✅ Evaluate and optimize retrieval quality
3. ➡️ **Choose Your Path**:
   - Module 07: AI Agents (build on RAG knowledge)
   - Module 08: Multimodal AI (parallel track)

## Code Patterns

### Basic RAG Pattern
```python
def rag_pipeline(query: str, collection) -> str:
    """Complete RAG pipeline."""
    
    # 1. Retrieve relevant documents
    query_embedding = create_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )
    
    # 2. Construct prompt with context
    context = "\n\n".join(results["documents"][0])
    prompt = f"""Answer the question based on the context below.
    
Context:
{context}

Question: {query}

Answer:"""
    
    # 3. Generate response
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content
```

### LangChain RAG Pattern
```python
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

# Setup
embeddings = OpenAIEmbeddings()
vectorstore = Chroma(
    collection_name="docs",
    embedding_function=embeddings
)

# Create retrieval chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4"),
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    return_source_documents=True
)

# Query
result = qa_chain({"query": "What is the refund policy?"})
answer = result["result"]
sources = result["source_documents"]
```

### LlamaIndex RAG Pattern
```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Load and index documents
documents = SimpleDirectoryReader("./docs").load_data()
index = VectorStoreIndex.from_documents(documents)

# Query
query_engine = index.as_query_engine()
response = query_engine.query("What is the refund policy?")

print(response.response)
print(response.source_nodes)  # Citations
```

## RAG vs Fine-Tuning Decision Matrix

| Factor | Use RAG | Use Fine-Tuning |
|--------|---------|-----------------|
| Knowledge changes frequently | ✓ | ✗ |
| Need citations/sources | ✓ | ✗ |
| Private/sensitive data | ✓ | ? |
| Style/tone adaptation | ✗ | ✓ |
| Reasoning patterns | ✗ | ✓ |
| Budget < $1000 | ✓ | ✗ |
| Need explainability | ✓ | ✗ |

## Common Issues

### Poor Retrieval Quality
- Optimize chunk size (try 300-800 words)
- Add metadata filtering
- Use hybrid search
- Implement reranking

### Context Window Exceeded
- Reduce number of retrieved chunks
- Implement contextual compression
- Use longer-context models (32k, 128k)

### Slow Response Time
- Cache embeddings
- Use async retrieval
- Implement query optimization
- Consider managed vector DB

### High Costs
- Use GPT-3.5 for simple queries
- Cache frequent queries
- Optimize chunk overlap
- Batch embed operations

## Evaluation Metrics

### Retrieval Metrics
- **Precision@K**: % of retrieved docs that are relevant
- **Recall@K**: % of relevant docs that are retrieved
- **MRR**: Mean Reciprocal Rank

### Generation Metrics
- **Faithfulness**: Answer supported by context
- **Relevance**: Answer addresses the question
- **Coherence**: Answer is well-formed

### End-to-End
- **Answer Correctness**: Compare to ground truth
- **User Satisfaction**: Thumbs up/down
- **Latency**: Time to first token

## Notes

- **Production Ready**: This module teaches production RAG patterns
- **Framework Choice**: LangChain for flexibility, LlamaIndex for simplicity
- **Evaluation Critical**: Always measure retrieval and generation quality
- **Portfolio**: Build a RAG system for your portfolio project

---

**Module Status**: 🚧 Content Development | ⬅️ Prev: Embeddings & Vector Databases | ⏭️ Next: AI Agents
