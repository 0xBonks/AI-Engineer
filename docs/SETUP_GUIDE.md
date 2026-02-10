# Complete Setup Guide

## Welcome!

This guide will walk you through the complete setup process for the AI Engineer Learning Repository, from first clone to running your first exercise.

## Overview

Setup involves:
1. System prerequisites
2. Repository setup
3. Environment configuration
4. Validation
5. Your first exercise

**Estimated Time:** 30-45 minutes

## Step 1: System Prerequisites

### Python 3.11+

**Check current version:**
```bash
python --version
```

**If you need to install:**

- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **macOS**: 
  ```bash
  brew install python@3.11
  ```
- **Linux (Ubuntu/Debian)**:
  ```bash
  sudo apt update
  sudo apt install python3.11 python3.11-venv python3.11-dev
  ```

### Git

**Check if installed:**
```bash
git --version
```

**If you need to install:**

- **Windows**: Download from [git-scm.com](https://git-scm.com/download/win)
- **macOS**: `brew install git`
- **Linux**: `sudo apt install git`

### Docker (Optional but Recommended)

**Check if installed:**
```bash
docker --version
docker-compose --version
```

**If you need to install:**

- [Docker Desktop](https://www.docker.com/products/docker-desktop) (Mac/Windows)
- [Docker Engine](https://docs.docker.com/engine/install/) (Linux)

## Step 2: Repository Setup

### Clone Repository

```bash
# Clone the repository
git clone <repository-url>
cd AI-Engineer
```

### Choose Your Setup Path

You have 3 options:

**Option A: Docker (Recommended)** - Easiest, no environment issues
- One-command setup
- All dependencies included
- JupyterLab ready
- → Go to [Docker Setup](#option-a-docker-setup)

**Option B: Local Python** - More control, faster
- Uses your local Python
- Manage dependencies yourself
- → Go to [Local Setup](#option-b-local-python-setup)

**Option C: Cloud** - No local installation
- Google Colab, GitHub Codespaces
- → Go to [Cloud Setup](#option-c-cloud-setup)

## Option A: Docker Setup

### Quick Start

```bash
# Run the startup script
./start.sh
```

The script will:
- Check Docker installation
- Create `.env` file if needed
- Build Docker image
- Start services
- Validate environment

### Access JupyterLab

Open your browser to:
```
http://localhost:8888
```

### Configure API Keys

1. Edit `.env` file:
   ```bash
   nano .env  # or use your preferred editor
   ```

2. Add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   ```

3. Save and restart:
   ```bash
   docker-compose restart
   ```

### Verify

```bash
# Run validation inside container
docker-compose exec jupyter python validate_env.py
```

**Success!** You're ready to start learning.
→ Go to [Your First Exercise](#step-5-your-first-exercise)

### Docker Commands Reference

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f jupyter

# Shell access
docker-compose exec jupyter bash
```

**Need help?** See [Docker Setup Documentation](docs/DOCKER_SETUP.md)

## Option B: Local Python Setup

### Create Virtual Environment

**Linux/macOS:**
```bash
python3.11 -m venv venv
source venv/bin/activate
```

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

### Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Install development tools (optional)
pip install -r requirements-dev.txt
```

This will take 5-10 minutes to download and install all packages.

### Configure Environment

```bash
# Create .env file from template
cp .env.example .env
```

Edit `.env` file and add your API keys:
```bash
OPENAI_API_KEY=sk-your-actual-key-here
```

**Get OpenAI API Key:**
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Go to [API Keys](https://platform.openai.com/api-keys)
4. Create new secret key
5. Copy and paste into `.env`

### Verify Installation

```bash
# Run validation script
python validate_env.py
```

Expected output:
```
✓ Python version: 3.11.x
✓ All required dependencies installed
✓ OpenAI API key configured
✓ Environment validation: PASSED
```

### Start Jupyter Lab

```bash
jupyter lab
```

This opens JupyterLab in your browser (usually `http://localhost:8888`).

**Success!** You're ready to start learning.
→ Go to [Your First Exercise](#step-5-your-first-exercise)

## Option C: Cloud Setup

### Google Colab

1. **Upload notebooks** to Google Drive
2. **Open with Google Colab**
3. **Add API keys** to Colab Secrets:
   - Click 🔑 icon in left sidebar
   - Add `OPENAI_API_KEY`
4. **Install dependencies** in notebook:
   ```python
   !pip install openai tiktoken langchain chromadb
   ```

### GitHub Codespaces

1. **Open repository** in Codespaces
2. **Wait for environment** to build
3. **Create `.env` file** and add keys
4. **Run validation**:
   ```bash
   python validate_env.py
   ```

### Replit

1. **Import repository** to Replit
2. **Configure secrets** (API keys) in Replit
3. **Run from shell**:
   ```bash
   pip install -r requirements.txt
   python validate_env.py
   ```

## Step 3: API Key Setup

### OpenAI (Required)

**Get Your Key:**

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to [API Keys](https://platform.openai.com/api-keys)
4. Click "Create new secret key"
5. Copy the key (you won't see it again!)
6. Add to `.env`:
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```

**Set Usage Limits (Important!):**

1. Go to [Billing Settings](https://platform.openai.com/account/billing/limits)
2. Set monthly budget (recommend $50-100 for full course)
3. Enable email alerts

**Test Your Key:**

```bash
# Quick test
python -c "from openai import OpenAI; import os; client = OpenAI(api_key=os.getenv('OPENAI_API_KEY')); print('API key works!') if client.models.list() else None"
```

### Other APIs (Optional)

**Anthropic (Claude):**
- Get key: [console.anthropic.com](https://console.anthropic.com/)
- Add to `.env`: `ANTHROPIC_API_KEY=sk-ant-...`

**Hugging Face:**
- Get token: [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
- Add to `.env`: `HUGGINGFACE_API_KEY=hf_...`

## Step 4: Validation

### Run Complete Validation

```bash
python validate_env.py
```

### What's Being Checked

- ✓ Python version (3.11+)
- ✓ All dependencies installed
- ✓ Environment variables configured
- ✓ API connectivity
- ✓ Vector databases ready
- ✓ Disk space sufficient

### If Validation Fails

**Common issues:**

1. **Python version too old**
   - Install Python 3.11+
   - Use correct Python in virtual environment

2. **Dependencies missing**
   - Ensure virtual environment activated
   - Run `pip install -r requirements.txt` again

3. **API key not found**
   - Check `.env` file exists (not `.env.example`)
   - Verify no extra spaces or quotes around key
   - Ensure `.env` in repository root

4. **API connection failed**
   - Verify API key is correct
   - Check internet connection
   - Try key in OpenAI Playground to verify

**Still having issues?** See [Troubleshooting Guide](docs/TROUBLESHOOTING.md)

## Step 5: Your First Exercise

### Navigate to Module 01

**In JupyterLab:**
1. File browser on left
2. Double-click `01-python-fundamentals/`
3. Open `README.md` to read module overview

**In Terminal:**
```bash
cd 01-python-fundamentals
```

### Explore the Module

Each module has:
- `README.md` - Theory and learning objectives
- `notebooks/` - Interactive demos
- `exercises/` - Coding challenges
- `tests/` - Automated validation
- `solutions/` - Reference implementations

### Start with a Notebook

1. Open `notebooks/` (will be created in Phase 2)
2. Start with first notebook
3. Read cells and run code
4. Experiment with examples

### Try an Exercise

1. Open `exercises/` (will be created in Phase 2)
2. Read instructions
3. Implement solution
4. Run tests:
   ```bash
   pytest tests/test_exercise.py
   ```

### Track Your Progress

Mark completed items in main README:

```markdown
- [x] Module 01: Python Fundamentals
- [ ] Module 02: AI Fundamentals & OpenAI API
...
```

## Tips for Success

### Learning Strategy

1. **Follow sequential order** - Each module builds on previous
2. **Do all exercises** - Hands-on practice is key
3. **Read solutions** - Learn from reference implementations
4. **Experiment** - Modify examples and explore
5. **Take notes** - Document your learning journey

### Cost Management

```python
# Always estimate costs first
from utils.cost_tracker import estimate_cost

cost = estimate_cost(prompt="Your prompt", model="gpt-3.5-turbo")
print(f"Estimated cost: ${cost:.4f}")
```

**Tips:**
- Use GPT-3.5-turbo for learning (cheaper)
- Enable cost tracking in `.env`
- Set cost limits
- Use local models (Ollama) for experimentation

### Getting Help

1. **Check documentation** in `docs/`
2. **Search GitHub Issues**
3. **Read module README files**
4. **Review error messages carefully**
5. **Create GitHub Issue** if stuck

### Staying Organized

```bash
# Create learning journal
mkdir my-notes
echo "# Learning Journal" > my-notes/README.md

# Track experiments
mkdir experiments
```

## Next Steps

Now that you're set up:

1. ✅ **Explore Module 01** - Python Fundamentals
2. 📚 **Read documentation** - Review key docs
3. 💻 **Complete exercises** - Start building skills
4. 🎯 **Track progress** - Mark completed items
5. 🚀 **Build projects** - Apply your knowledge

## Quick Reference

### Essential Commands

```bash
# Activate environment (local setup)
source venv/bin/activate

# Start Jupyter
jupyter lab

# Run tests
pytest

# Validate environment
python validate_env.py

# Docker commands
docker-compose up -d    # Start
docker-compose down     # Stop
docker-compose logs -f  # View logs
```

### Important Files

- `.env` - API keys and configuration
- `requirements.txt` - Python dependencies
- `validate_env.py` - Environment validation
- `README.md` - Repository overview
- `CONTRIBUTING.md` - Contribution guidelines

### Documentation

- [Environment Setup](ENV_SETUP.md) - Detailed setup instructions
- [Docker Setup](docs/DOCKER_SETUP.md) - Docker-specific guide
- [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues
- [Cost Tracking](docs/COST_TRACKING.md) - Manage API costs
- [CI/CD](docs/CI_CD.md) - Testing and quality

## Congratulations!

You've successfully set up your AI Engineer learning environment! 🎉

**Ready to start learning?**

→ [Begin Module 01: Python Fundamentals](01-python-fundamentals/README.md)

---

**Questions?** Open a GitHub Issue or Discussion.

**Last Updated:** 2026-02-10
