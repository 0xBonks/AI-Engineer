# Data Handling Solutions

## Document Chunking

```python
from typing import List

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Chunk text with overlap."""
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    
    return chunks
```

## Best Practices

1. Use pathlib for path handling
2. Always use context managers for files
3. Handle encoding explicitly
4. Stream large files
5. Validate JSON schema
