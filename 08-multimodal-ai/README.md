# Module 08: Multimodal AI

## Overview

Expand beyond text to integrate vision, audio, and speech capabilities into your AI applications. Learn to generate and understand images with DALL-E and Vision API, process audio with Whisper, implement text-to-speech, and build complete multimodal applications.

## Learning Objectives

By completing this module, you will be able to:

- Generate images using DALL-E API with prompt engineering for visual outputs
- Implement image understanding using Vision API for analysis tasks
- Process audio with text-to-speech and speech-to-text (Whisper API)
- Understand video understanding basics and multimodal data processing
- Build multimodal applications using LangChain integrations

## Prerequisites

- **Completed**: Module 03 (AI Fundamentals & OpenAI API)
- **Required**: Understanding of API calls and prompt engineering
- **Optional**: Modules 06-07 for advanced applications

## Estimated Time

**10-12 hours** to complete all exercises and demos

## Key Concepts

### 1. Image Generation (DALL-E)
- DALL-E 3 capabilities and limitations
- Prompt engineering for images
- Style and quality parameters
- Image sizes and formats
- Cost optimization
- Use cases and applications

### 2. Image Understanding (Vision API)
- GPT-4 Vision capabilities
- Image analysis and description
- OCR and text extraction
- Object detection and counting
- Document understanding
- Multi-image reasoning

### 3. Speech-to-Text (Whisper)
- Whisper model capabilities
- Transcription vs translation
- Supported languages and formats
- Timestamp and speaker detection
- Handling audio quality issues
- Real-time vs batch processing

### 4. Text-to-Speech (TTS)
- OpenAI TTS API
- Voice options and quality
- Streaming audio
- Speech synthesis use cases
- Cost and latency considerations
- Accessibility applications

### 5. Video Understanding
- Video as sequence of frames
- Extracting frames for analysis
- Audio track processing
- Combining vision + audio insights
- Limitations and workarounds
- Future directions

### 6. Multimodal Applications
- Combining text, image, audio
- Cross-modal reasoning
- Accessibility tools
- Content moderation
- Creative applications
- Production patterns

## Structure

```
08-multimodal-ai/
├── README.md                              # This file
├── notebooks/                             # Interactive tutorials
│   ├── 01-image-generation.ipynb
│   ├── 02-image-understanding.ipynb
│   ├── 03-speech-to-text.ipynb
│   ├── 04-text-to-speech.ipynb
│   ├── 05-video-processing.ipynb
│   └── 06-multimodal-apps.ipynb
├── exercises/                             # Hands-on challenges
│   ├── 01-dalle-images.py
│   ├── 02-vision-analysis.py
│   ├── 03-whisper-transcription.py
│   ├── 04-tts-generation.py
│   ├── 05-document-ocr.py
│   ├── 06-multimodal-rag.py
│   └── 07-accessibility-app.py
├── tests/                                 # Automated validation
│   └── test_exercises.py
└── solutions/                             # Reference implementations
    └── solutions/
```

## Topics Covered

### Image Generation
- **Concept**: Text description → Image
- **Use Case**: Content creation, prototyping, illustration
- **Example**: "A futuristic city at sunset, cyberpunk style"

### Image Understanding
- **Concept**: Image → Text description/analysis
- **Use Case**: Accessibility, content moderation, document processing
- **Example**: Describe chart, extract data from invoice

### Speech-to-Text
- **Concept**: Audio → Text transcript
- **Use Case**: Meeting transcription, voice interfaces, accessibility
- **Example**: Transcribe podcast to text with timestamps

### Text-to-Speech
- **Concept**: Text → Natural speech audio
- **Use Case**: Audiobooks, voice assistants, accessibility
- **Example**: Convert article to spoken audio

### Multimodal RAG
- **Concept**: Combine text, images, audio in retrieval
- **Use Case**: Search across media types, comprehensive Q&A
- **Example**: "Find the slide where revenue is discussed"

## Exercises

### Exercise 1: DALL-E Image Generation
**File**: `exercises/01-dalle-images.py`

Generate images using DALL-E 3 with effective prompts.

**Success Criteria**:
- Generate images from text prompts
- Experiment with styles and parameters
- Download and save images

### Exercise 2: Vision Analysis
**File**: `exercises/02-vision-analysis.py`

Analyze images using GPT-4 Vision.

**Success Criteria**:
- Upload and analyze images
- Extract information from images
- Compare multiple images

### Exercise 3: Whisper Transcription
**File**: `exercises/03-whisper-transcription.py`

Transcribe audio files using Whisper API.

**Success Criteria**:
- Transcribe audio files
- Get timestamps
- Handle multiple languages

### Exercise 4: TTS Generation
**File**: `exercises/04-tts-generation.py`

Generate speech from text using TTS API.

**Success Criteria**:
- Convert text to speech
- Try different voices
- Stream audio output

### Exercise 5: Document OCR
**File**: `exercises/05-document-ocr.py`

Extract text and data from document images.

**Success Criteria**:
- Extract text from scanned docs
- Parse structured data (tables, forms)
- Handle poor quality images

### Exercise 6: Multimodal RAG
**File**: `exercises/06-multimodal-rag.py`

Build RAG system that works with text and images.

**Success Criteria**:
- Index documents with images
- Retrieve based on text or image queries
- Generate answers using both modalities

### Exercise 7: Accessibility Application
**File**: `exercises/07-accessibility-app.py`

Build an accessibility tool using multimodal AI.

**Success Criteria**:
- Describe images for screen readers
- Transcribe audio content
- Generate audio from text

## Resources

### Official Documentation
- [DALL-E API](https://platform.openai.com/docs/guides/images)
- [Vision API](https://platform.openai.com/docs/guides/vision)
- [Whisper API](https://platform.openai.com/docs/guides/speech-to-text)
- [TTS API](https://platform.openai.com/docs/guides/text-to-speech)

### Tools & Libraries
- [PIL/Pillow](https://pillow.readthedocs.io/) - Image processing
- [moviepy](https://zulko.github.io/moviepy/) - Video processing
- [pydub](https://github.com/jiaaro/pydub) - Audio processing

### Recommended Reading
- [Multimodal Chain of Thought](https://arxiv.org/abs/2302.00923)
- [Vision LLMs Survey](https://arxiv.org/abs/2305.11175)
- [LangChain Multimodal Guide](https://python.langchain.com/docs/use_cases/multimodal/)

## Next Steps

After completing this module:

1. ✅ Build a multimodal application
2. ✅ Combine with RAG or Agents from previous modules
3. ➡️ Proceed to **Module 09: Testing & Validation**

## Code Patterns

### Image Generation
```python
from openai import OpenAI

client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="A serene landscape with mountains and a lake at sunset",
    size="1024x1024",
    quality="standard",
    n=1
)

image_url = response.data[0].url
```

### Image Understanding
```python
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": image_url}
                }
            ]
        }
    ]
)

description = response.choices[0].message.content
```

### Speech-to-Text
```python
audio_file = open("audio.mp3", "rb")

transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="verbose_json",
    timestamp_granularities=["word"]
)

print(transcript.text)
```

### Text-to-Speech
```python
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello! This is a test of text to speech."
)

response.stream_to_file("output.mp3")
```

### Multimodal RAG
```python
def multimodal_rag(query: str, query_image=None):
    """RAG that works with text and images."""
    
    # Create query embedding (text)
    query_embedding = create_embedding(query)
    
    # Retrieve relevant chunks
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )
    
    # If image provided, analyze it
    image_context = ""
    if query_image:
        image_analysis = analyze_image(query_image)
        image_context = f"\n\nImage context: {image_analysis}"
    
    # Generate response with both contexts
    prompt = f"""Context: {results['documents'][0]}{image_context}
    
Question: {query}

Answer:"""
    
    return llm_call(prompt)
```

## API Costs

| API | Cost | Notes |
|-----|------|-------|
| DALL-E 3 (standard) | $0.040/image | 1024x1024 |
| DALL-E 3 (HD) | $0.080/image | Higher quality |
| GPT-4 Vision | ~$0.01/image | Varies by detail |
| Whisper | $0.006/minute | Audio transcription |
| TTS | $0.015/1K chars | ~$15 per 1M chars |

## Image Prompt Engineering Tips

1. **Be Specific**: "Victorian mansion" > "house"
2. **Add Style**: "in the style of Van Gogh"
3. **Set Mood**: "dramatic lighting", "peaceful atmosphere"
4. **Specify Details**: Camera angle, time of day, weather
5. **Use Examples**: Reference known artworks or photos

## Common Issues

### Image Generation Quality
- Refine prompts with more details
- Use DALL-E 3 HD for better quality
- Try multiple variations
- Study successful prompts

### Vision API Limitations
- Max image size: 20MB
- Works best with clear, well-lit images
- May struggle with very small text
- Limited understanding of abstract concepts

### Whisper Transcription Errors
- Improve audio quality (reduce noise)
- Use supported formats (MP3, WAV, etc.)
- Split long audio files
- Provide context in language parameter

### TTS Voice Selection
- Try all voices for your use case
- Consider audience and content type
- Balance quality vs cost (tts-1 vs tts-1-hd)
- Test with actual content

## Accessibility Applications

1. **Screen Reader Enhancement**: Describe images for visually impaired
2. **Audio Transcription**: Captions for hearing impaired
3. **Text-to-Speech**: Convert text to audio
4. **Sign Language**: Future: Analyze sign language videos
5. **Document Understanding**: Make scanned documents searchable

## Notes

- **Costs Higher**: Multimodal APIs more expensive than text-only
- **Quality Varies**: Test with real data, not just examples
- **Privacy**: Be careful with user-uploaded images/audio
- **Moderation**: Always moderate generated content
- **Portfolio**: Multimodal apps impressive for job applications

---

**Module Status**: 🚧 Content Development | ⬅️ Prev: AI Agents | ⏭️ Next: Testing & Validation
