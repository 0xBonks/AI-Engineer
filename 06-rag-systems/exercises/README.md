# Module 06 - Exercises

## Overview

Hands-on exercises for building production RAG systems.

## Exercise Guide

### Core Exercises

All key RAG concepts are covered in **Notebooks 01-02** with complete working implementations:

#### ✅ From Notebook 01:
- **Basic RAG System**: Complete `SimpleRAG` class with retrieve + generate
- **Improved RAG**: Enhanced with better prompting and citations
- **End-to-end demo**: Full working example with knowledge base

#### ✅ From Notebook 02:
- **Document Loading**: Multi-format support (PDF, DOCX, HTML, TXT)
- **Smart Chunking**: Recursive splitting with overlap
- **Metadata Extraction**: Auto-extract emails, URLs, dates
- **Complete Pipeline**: Load → Clean → Chunk → Embed → Store

### Recommended Practice Exercises

Students should implement:

1. **Basic RAG** - Build from scratch following Notebook 01
2. **Document Pipeline** - Create ingestion system from Notebook 02  
3. **Hybrid Search** - Combine semantic + keyword (Module 05 patterns)
4. **Citation RAG** - Add source attribution
5. **LangChain Implementation** - Use LangChain RetrievalQA
6. **LlamaIndex Implementation** - Use LlamaIndex VectorStoreIndex
7. **Production RAG** - Add monitoring, caching, error handling

## Getting Started

```bash
# Setup
source ../../.venv/bin/activate

# Work through notebooks first
cd ../notebooks
jupyter lab

# Then implement your own RAG system
cd ../exercises
python your_rag_implementation.py
```

## Implementation Patterns

### Pattern 1: Simple RAG
```python
class SimpleRAG:
    def add_documents(docs):
        # Embed and store
    def retrieve(query, k=3):
        # Vector search
    def generate(query, context):
        # LLM with context
    def query(question):
        # Retrieve + Generate
```

### Pattern 2: Document Pipeline
```python
def process_document(filepath):
    docs = load_file(filepath)          # 1. Load
    docs = enrich_metadata(docs)        # 2. Enrich
    chunks = chunk_documents(docs)      # 3. Chunk
    embeddings = embed(chunks)          # 4. Embed
    store(chunks, embeddings)           # 5. Store
```

### Pattern 3: LangChain RAG
```python
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma

vectorstore = Chroma(...)
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=vectorstore.as_retriever()
)
answer = qa.run("question")
```

## Resources

### Framework Documentation:
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [LlamaIndex Quickstart](https://docs.llamaindex.ai/en/stable/getting_started/starter_example.html)
- [ChromaDB Docs](https://docs.trychroma.com/)

### RAG Patterns:
- [Advanced RAG Techniques](https://www.pinecone.io/learn/advanced-rag/)
- [RAG Evaluation](https://www.trulens.org/trulens_eval/getting_started/core_concepts/)

## Success Criteria

After completing exercises, you should be able to:
- ✅ Build RAG systems from scratch
- ✅ Process multi-format documents
- ✅ Use LangChain and LlamaIndex
- ✅ Evaluate and optimize RAG quality
- ✅ Deploy production RAG applications

## Testing Your Implementation

```python
# Test your RAG system
rag = YourRAGImplementation()
rag.add_documents([...])

test_questions = [
    "Question in knowledge base",
    "Question outside knowledge base",
    "Ambiguous question"
]

for q in test_questions:
    result = rag.query(q)
    print(f"Q: {q}")
    print(f"A: {result['answer']}")
    assert 'sources' in result
```

---

**Module Status**: ✅ Core concepts complete, ready for practice

**Next**: Module 07 - AI Agents
