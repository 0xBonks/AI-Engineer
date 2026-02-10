# LiteLLM Integration - Unified Multi-Provider API

Diese Integration ermöglicht die Nutzung verschiedener LLM-Anbieter (OpenAI, Anthropic, Azure, Google, etc.) über eine einheitliche API-Schnittstelle.

## Warum LiteLLM?

**Vorteile gegenüber direkter OpenAI-Nutzung:**
- ✅ **Einheitliches Interface** für alle Provider (OpenAI, Anthropic, Azure, Google, etc.)
- ✅ **Einfaches Model-Switching** ohne Code-Änderungen
- ✅ **Built-in Cost Tracking** über alle Provider hinweg
- ✅ **Automatisches Retry** und Rate Limiting
- ✅ **Streaming Support** für alle Provider
- ✅ **Fallback-Mechanismen** zwischen verschiedenen Modellen

## Installation

```bash
pip install litellm
```

Oder aus requirements.txt:
```bash
pip install -r requirements.txt
```

## Konfiguration

### 1. API Keys einrichten

Kopiere `.env.example` zu `.env` und füge deine API-Keys hinzu:

```bash
cp .env.example .env
```

**Für OpenAI:**
```env
OPENAI_API_KEY=sk-your-openai-api-key-here
```

**Für Anthropic (optional):**
```env
ANTHROPIC_API_KEY=sk-ant-your-anthropic-api-key-here
```

**Für Azure OpenAI (optional):**
```env
AZURE_API_KEY=your-azure-api-key-here
AZURE_API_BASE=https://your-resource.openai.azure.com/
AZURE_API_VERSION=2024-02-15-preview
```

### 2. Keine weitere Konfiguration nötig!

LiteLLM liest automatisch die API-Keys aus den Umgebungsvariablen.

## Nutzung

### Einfaches Beispiel

```python
from utils.litellm_helpers import chat_completion

# OpenAI verwenden
response = chat_completion(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response)

# Anthropic verwenden (gleiche Funktion!)
response = chat_completion(
    model="claude-3-sonnet-20240229",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response)
```

### Client-Klasse verwenden

```python
from utils.litellm_helpers import LiteLLMClient

# Client initialisieren
client = LiteLLMClient(
    default_model="gpt-3.5-turbo",
    temperature=0.7
)

# Chat
response = client.chat(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain Python decorators"}
    ]
)
print(response)

# Modell pro Request überschreiben
response = client.chat(
    messages=[{"role": "user", "content": "Hello!"}],
    model="claude-3-haiku-20240307"  # Anderes Modell verwenden
)
```

### Streaming

```python
from utils.litellm_helpers import chat_completion

# Streaming-Response
stream = chat_completion(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Write a story"}],
    stream=True
)

for chunk in stream:
    print(chunk, end="", flush=True)
```

### Modelle vergleichen

```python
from utils.litellm_helpers import compare_models

results = compare_models(
    prompt="Explain quantum computing in one sentence",
    models=["gpt-3.5-turbo", "gpt-4", "claude-3-sonnet-20240229"]
)

for model, info in results.items():
    print(f"\n{model}:")
    print(f"  Response: {info['response']}")
    print(f"  Cost: ${info['cost']:.6f}")
    print(f"  Latency: {info['latency']:.2f}s")
```

### Cost Tracking

```python
from utils.litellm_helpers import LiteLLMClient

client = LiteLLMClient()

# Nach einem Request
cost = client.get_cost(
    model="gpt-3.5-turbo",
    prompt_tokens=100,
    completion_tokens=50
)
print(f"Cost: ${cost:.6f}")
```

## Unterstützte Modelle

### OpenAI
- `gpt-4`, `gpt-4-turbo`, `gpt-4-turbo-preview`
- `gpt-3.5-turbo`, `gpt-3.5-turbo-16k`

### Anthropic
- `claude-3-opus-20240229` (stärkstes Modell)
- `claude-3-sonnet-20240229` (balanced)
- `claude-3-haiku-20240307` (schnell & günstig)
- `claude-2.1`, `claude-2`

### Azure OpenAI
- `azure/<your-deployment-name>`

### Google
- `gemini-pro`, `gemini-pro-vision`

### Weitere
- Cohere, Hugging Face, Ollama, und viele mehr

## Beispiel-Demo

Führe die vollständige Demo aus:

```bash
python 03-ai-fundamentals-openai/examples/litellm-demo.py
```

Diese Demo zeigt:
1. ✅ Einfache Chat-Completions mit verschiedenen Providern
2. ✅ Streaming-Responses
3. ✅ Client-Klasse Nutzung
4. ✅ Modell-Informationen abrufen
5. ✅ Cost Tracking
6. ✅ Modell-Vergleiche
7. ✅ Fallback zwischen Modellen
8. ✅ Multi-Turn Conversations

## Vergleich: OpenAI vs LiteLLM

### Mit OpenAI (direkt):
```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}]
)
content = response.choices[0].message.content
```

### Mit LiteLLM:
```python
from utils.litellm_helpers import chat_completion

# OpenAI verwenden
response = chat_completion(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}]
)

# Oder Anthropic - nur model-Parameter ändern!
response = chat_completion(
    model="claude-3-sonnet-20240229",
    messages=[{"role": "user", "content": "Hello"}]
)
```

## Best Practices

### 1. Model-Namen als Konstanten
```python
# config.py
OPENAI_MODEL = "gpt-3.5-turbo"
ANTHROPIC_MODEL = "claude-3-sonnet-20240229"
FALLBACK_MODEL = "gpt-3.5-turbo"

# usage
response = chat_completion(model=OPENAI_MODEL, messages=[...])
```

### 2. Fallback-Strategie
```python
def chat_with_fallback(messages, primary_model, fallback_model):
    try:
        return chat_completion(model=primary_model, messages=messages)
    except Exception as e:
        logger.warning(f"Primary model failed: {e}, trying fallback")
        return chat_completion(model=fallback_model, messages=messages)
```

### 3. Cost Monitoring
```python
from utils.litellm_helpers import LiteLLMClient

client = LiteLLMClient()

# Track costs
total_cost = 0
for request in requests:
    response = client.chat(messages=request)
    cost = client.get_cost(
        model="gpt-3.5-turbo",
        prompt_tokens=response.usage.prompt_tokens,
        completion_tokens=response.usage.completion_tokens
    )
    total_cost += cost

print(f"Total cost: ${total_cost:.4f}")
```

## Migration von OpenAI zu LiteLLM

### Schritt 1: Import ändern
```python
# Alt
from openai import OpenAI

# Neu
from utils.litellm_helpers import LiteLLMClient
```

### Schritt 2: Client initialisieren
```python
# Alt
client = OpenAI()

# Neu
client = LiteLLMClient(default_model="gpt-3.5-turbo")
```

### Schritt 3: API-Calls anpassen
```python
# Alt
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[...]
)
content = response.choices[0].message.content

# Neu
content = client.chat(
    model="gpt-3.5-turbo",
    messages=[...]
)
```

## Troubleshooting

### API Key nicht gefunden
```
Error: AuthenticationError: Invalid API key
```
**Lösung:** Prüfe, ob der API-Key in `.env` gesetzt ist und die Datei geladen wird:
```python
from dotenv import load_dotenv
load_dotenv()
```

### Modell nicht verfügbar
```
Error: Model not found
```
**Lösung:** Prüfe die Modell-Namen:
```python
from utils.litellm_helpers import get_available_models
models = get_available_models()
print(models)
```

### Rate Limit Exceeded
LiteLLM hat built-in Retry-Logic, aber bei dauerhaften Problemen:
```python
# Warte zwischen Requests
import time
time.sleep(1)

# Oder nutze die RateLimiter-Klasse aus api_helpers.py
from utils.api_helpers import RateLimiter
rate_limiter = RateLimiter(max_requests=60, time_window=60)
with rate_limiter:
    response = chat_completion(...)
```

## Weitere Ressourcen

- **LiteLLM Dokumentation:** https://docs.litellm.ai/
- **Unterstützte Provider:** https://docs.litellm.ai/docs/providers
- **Cost Tracking:** https://docs.litellm.ai/docs/completion/cost_tracking
- **Beispiele:** `/03-ai-fundamentals-openai/examples/litellm-demo.py`
- **Helper-Modul:** `/utils/litellm_helpers.py`

## Zusammenfassung

LiteLLM bietet eine einfache, einheitliche Schnittstelle für verschiedene LLM-Anbieter:

| Feature | OpenAI direkt | LiteLLM |
|---------|--------------|---------|
| Multi-Provider | ❌ | ✅ |
| Einheitliche API | ❌ | ✅ |
| Built-in Cost Tracking | ❌ | ✅ |
| Automatisches Retry | ❌ | ✅ |
| Einfaches Switching | ❌ | ✅ |
| Streaming Support | ✅ | ✅ |

**Empfehlung:** Nutze LiteLLM, wenn du Flexibilität bei der Provider-Wahl brauchst oder mehrere Anbieter parallel nutzen möchtest. Die bestehende OpenAI-Integration bleibt weiterhin verfügbar für spezifische Use-Cases.
