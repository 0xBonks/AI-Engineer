# Environment Setup Guide

## Overview

This guide walks you through setting up your environment for the AI Engineer Learning Repository, including obtaining API keys, configuring environment variables, and verifying your setup.

## Prerequisites

- Python 3.11 or higher installed
- Git installed
- Text editor or IDE
- Terminal/command line access

## Step 1: Repository Setup

### Clone the Repository

```bash
git clone <repository-url>
cd AI-Engineer
```

### Create Virtual Environment

**Linux/macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install core dependencies
pip install -r requirements.txt

# Install development dependencies (optional)
pip install -r requirements-dev.txt
```

## Step 2: API Key Setup

### OpenAI API Key (Required)

OpenAI is the primary API used throughout the curriculum.

**Get Your Key:**

1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to [API Keys](https://platform.openai.com/api-keys)
4. Click "Create new secret key"
5. Copy the key (you won't see it again!)
6. Store it securely

**Set Usage Limits (Highly Recommended):**

1. Go to [Billing Settings](https://platform.openai.com/account/billing/limits)
2. Set a monthly budget limit (e.g., $50-100)
3. Enable email alerts for usage thresholds

**Pricing Reference:**
- GPT-4: ~$0.03/1K tokens input, ~$0.06/1K tokens output
- GPT-3.5-turbo: ~$0.0005/1K tokens input, ~$0.0015/1K tokens output
- Embeddings (text-embedding-3-small): ~$0.00002/1K tokens

**Estimated Repository Costs:** $50-150 total (varies by usage)

### Anthropic API Key (Optional)

For Claude model comparisons in advanced modules.

**Get Your Key:**

1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create new key
5. Copy and store securely

**Note:** Free tier available; not required for core curriculum.

### Google Generative AI (Gemini) Key (Optional)

For Gemini model comparisons.

**Get Your Key:**

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with Google account
3. Create API key
4. Copy and store securely

**Note:** Free tier available; not required for core curriculum.

### Hugging Face Token (Optional)

Required for downloading gated models and using Inference API.

**Get Your Token:**

1. Visit [Hugging Face](https://huggingface.co/)
2. Sign up or log in
3. Go to [Settings > Access Tokens](https://huggingface.co/settings/tokens)
4. Create new token (read access sufficient for most use cases)
5. Copy and store securely

**When You Need It:**
- Downloading certain models (e.g., Llama 2)
- Using Hugging Face Inference API
- Module 03: Open Source AI

### Pinecone API Key (Optional)

Used in advanced vector database modules.

**Get Your Key:**

1. Visit [Pinecone](https://app.pinecone.io/)
2. Sign up (free tier available)
3. Create new project
4. Copy API key and environment name
5. Store securely

**When You Need It:**
- Module 04: Embeddings & Vector Databases (alternatives section)
- Module 08: Advanced RAG & Optimization

### Weaviate Credentials (Optional)

Alternative vector database option.

**Get Your Credentials:**

1. Visit [Weaviate Cloud](https://console.weaviate.cloud/)
2. Sign up (free sandbox available)
3. Create cluster
4. Copy cluster URL and API key
5. Store securely

**When You Need It:**
- Module 04: Embeddings & Vector Databases (alternatives section)

## Step 3: Environment Configuration

### Create .env File

```bash
# Copy the template
cp .env.example .env
```

### Edit .env File

Open `.env` in your text editor and add your API keys:

```bash
# Required
OPENAI_API_KEY=sk-your-actual-openai-key-here

# Optional (add as needed)
# ANTHROPIC_API_KEY=sk-ant-your-actual-anthropic-key
# GOOGLE_API_KEY=your-actual-google-key
# HUGGINGFACE_API_KEY=hf_your-actual-token
```

### Configuration Options

**Recommended Settings for Learning:**

```bash
# Use cheaper models by default
DEFAULT_CHAT_MODEL=gpt-3.5-turbo
DEFAULT_EMBEDDING_MODEL=text-embedding-3-small

# Enable cost tracking
COST_TRACKING_ENABLED=true
COST_WARNING_THRESHOLD=10.0  # Warn at $10
COST_MAX_THRESHOLD=50.0      # Block at $50

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=text

# Rate limiting
MAX_REQUESTS_PER_MINUTE=60
MAX_CONCURRENT_REQUESTS=5
```

## Step 4: Verify Installation

### Run Environment Validation

```bash
python validate_env.py
```

**Expected Output:**
```
✓ Python version: 3.11.x
✓ All required dependencies installed
✓ OpenAI API key configured
✓ OpenAI API connectivity: OK
✓ Chroma vector database: Ready
✓ Environment validation: PASSED
```

**If validation fails:**
1. Check error messages for specific issues
2. Verify API keys are correct (no extra spaces/quotes)
3. Ensure all dependencies installed correctly
4. See [Troubleshooting](#troubleshooting) below

### Test OpenAI API

```python
# test_openai.py
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say 'API test successful!'"}],
    max_tokens=10
)

print(response.choices[0].message.content)
```

Run the test:
```bash
python test_openai.py
```

Expected output: `API test successful!`

## Step 5: Start Learning

### Launch Jupyter Lab

```bash
jupyter lab
```

This will open JupyterLab in your browser (usually `http://localhost:8888`).

### Navigate to Module 01

1. In JupyterLab, open the file browser
2. Navigate to `01-python-fundamentals/`
3. Open `README.md` to read module overview
4. Open `notebooks/` to start with interactive demos

### Run Your First Exercise

```bash
cd 01-python-fundamentals/exercises
python 01-async-basics.py

# Run tests to verify
pytest ../tests/test_async_basics.py
```

## Security Best Practices

### Protecting Your API Keys

1. **Never commit .env file** to version control (already in .gitignore)
2. **Never share your API keys** publicly
3. **Use separate keys** for different projects/environments
4. **Rotate keys regularly** (every 90 days recommended)
5. **Monitor API usage** for unexpected activity
6. **Set spending limits** in provider dashboards

### If Your Key Is Compromised

1. **Immediately revoke** the key in your provider dashboard
2. **Generate a new key**
3. **Update your .env file**
4. **Review recent API usage** logs
5. **Report** to your API provider if suspicious activity detected

### Additional Security Measures

- Use environment-specific keys (dev/staging/production)
- Implement least privilege (minimal required permissions)
- Enable two-factor authentication on provider accounts
- Use API key management tools for teams
- Regularly audit API access logs

## Troubleshooting

### Python Version Issues

**Error:** `Python 3.11+ required`

**Solution:**
```bash
# Check Python version
python --version

# Install Python 3.11+ from python.org
# Or use pyenv:
pyenv install 3.11.7
pyenv local 3.11.7
```

### Dependency Installation Failures

**Error:** `Could not find a version that satisfies the requirement`

**Solutions:**
```bash
# Update pip
pip install --upgrade pip

# Clear cache
pip cache purge

# Install with verbose output
pip install -r requirements.txt -v

# Try specific index
pip install -r requirements.txt -i https://pypi.org/simple
```

### API Key Not Found

**Error:** `OpenAI API key not found`

**Solutions:**
1. Verify `.env` file exists (not `.env.example`)
2. Check key format: `OPENAI_API_KEY=sk-...` (no spaces, no quotes)
3. Ensure `.env` is in repository root
4. Try loading explicitly:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

### API Connection Errors

**Error:** `Connection error` or `API key invalid`

**Solutions:**
1. **Check internet connection**
2. **Verify API key** is correct (copy-paste again)
3. **Check API key status** in provider dashboard
4. **Try curl test:**
   ```bash
   curl https://api.openai.com/v1/models \
     -H "Authorization: Bearer $OPENAI_API_KEY"
   ```

### Import Errors

**Error:** `ModuleNotFoundError: No module named 'xxx'`

**Solutions:**
```bash
# Verify virtual environment is activated
which python  # Should show venv path

# Reinstall dependencies
pip install -r requirements.txt

# Check specific package
pip show package-name
```

### Permission Errors (Windows)

**Error:** `Access denied` during installation

**Solutions:**
1. **Run as administrator**
2. **Use user installation:**
   ```bash
   pip install --user -r requirements.txt
   ```
3. **Check antivirus** isn't blocking Python

### GPU/CUDA Issues

**Error:** GPU not detected

**Solutions:**
1. **Check GPU availability:**
   ```python
   import torch
   print(torch.cuda.is_available())
   ```
2. **Install CUDA toolkit** from NVIDIA
3. **Install PyTorch with CUDA:**
   ```bash
   pip install torch --index-url https://download.pytorch.org/whl/cu118
   ```
4. **Verify CUDA version** matches PyTorch:
   ```bash
   nvidia-smi
   ```

## Alternative Setups

### Using Docker

See [DOCKER_SETUP.md](DOCKER_SETUP.md) for containerized environment.

**Quick start:**
```bash
./start.sh
# Access JupyterLab at http://localhost:8888
```

### Using Cloud Environments

**Google Colab:**
1. Upload notebooks to Google Drive
2. Open with Google Colab
3. Add API keys to Colab secrets
4. Install dependencies in notebook cell

**GitHub Codespaces:**
1. Open repository in Codespaces
2. Configure .env file
3. Dependencies auto-install from requirements.txt

**Replit:**
1. Import repository to Replit
2. Configure secrets (API keys)
3. Run from Replit shell

## Getting Help

If you encounter issues not covered here:

1. **Check documentation:**
   - [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Comprehensive troubleshooting
   - [DEPENDENCIES.md](DEPENDENCIES.md) - Dependency issues
   - [DOCKER_SETUP.md](DOCKER_SETUP.md) - Docker-specific issues

2. **Search existing issues:**
   - GitHub Issues for this repository

3. **Create new issue:**
   - Include Python version, OS, error messages
   - Provide steps to reproduce
   - Share relevant configuration (without API keys!)

4. **Community support:**
   - GitHub Discussions
   - Project Discord/Slack (if available)

## Next Steps

✓ Environment configured and validated  
✓ API keys working  
✓ Ready to start learning  

**Begin your journey:**
→ [Module 01: Python Fundamentals](../01-python-fundamentals/README.md)

---

**Last Updated:** 2026-02-10  
**Version:** 1.0
