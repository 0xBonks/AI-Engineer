# Troubleshooting Guide

## Quick Diagnosis

Run this first to identify issues:

```bash
python validate_env.py
```

## Common Issues by Category

### Installation & Setup

#### Python Version Issues

**Problem:** "Python 3.11+ required"

**Cause:** Using older Python version

**Solutions:**

1. **Check your Python version:**
   ```bash
   python --version
   python3 --version
   python3.11 --version
   ```

2. **Install Python 3.11+:**
   - **macOS**: `brew install python@3.11`
   - **Ubuntu/Debian**: `sudo apt install python3.11`
   - **Windows**: Download from [python.org](https://www.python.org/downloads/)

3. **Use specific Python version:**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   which python  # Should show venv path
   python --version  # Should show 3.11+
   ```

4. **Update pyenv (if using):**
   ```bash
   pyenv install 3.11.7
   pyenv local 3.11.7
   ```

#### Virtual Environment Issues

**Problem:** Virtual environment not activating or wrong Python

**Solutions:**

1. **Recreate virtual environment:**
   ```bash
   rm -rf venv
   python3.11 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. **Verify activation:**
   ```bash
   which python  # Should show venv path
   pip list      # Should show installed packages
   ```

3. **Windows activation issues:**
   ```powershell
   # If permission denied:
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   venv\Scripts\activate
   ```

#### Dependency Installation Failures

**Problem:** `pip install -r requirements.txt` fails

**Common errors:**

**Error: "Could not find a version that satisfies the requirement"**

Solutions:
```bash
# Update pip
pip install --upgrade pip setuptools wheel

# Try with verbose output
pip install -r requirements.txt -v

# Use specific index
pip install -r requirements.txt -i https://pypi.org/simple
```

**Error: "No matching distribution found"**

Solutions:
```bash
# Check package name spelling
cat requirements.txt | grep <package-name>

# Try installing individually
pip install <package-name>
```

**Error: "Microsoft Visual C++ 14.0 or greater is required" (Windows)**

Solution:
1. Install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. Or use pre-built wheels: `pip install <package> --only-binary :all:`

**Error: Building wheels for packages taking forever**

Solutions:
```bash
# Install from wheels only (faster)
pip install --prefer-binary -r requirements.txt

# Or use conda (alternative package manager)
conda install -c conda-forge <package-name>
```

### Environment Configuration

#### .env File Issues

**Problem:** "API key not found" or "Environment variable not set"

**Solutions:**

1. **Verify .env file exists:**
   ```bash
   ls -la .env  # Should exist, not .env.example
   ```

2. **Create .env if missing:**
   ```bash
   cp .env.example .env
   ```

3. **Check .env format:**
   ```bash
   cat .env
   ```
   
   Correct format:
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```
   
   **Wrong** formats:
   ```
   OPENAI_API_KEY = sk-key-here  # Extra spaces
   OPENAI_API_KEY="sk-key-here"  # Quotes
   OPENAI_API_KEY=                # Empty value
   ```

4. **Verify Python loads .env:**
   ```python
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   print(os.getenv("OPENAI_API_KEY"))  # Should print your key
   ```

5. **Check file location:**
   - `.env` must be in repository root
   - Not in subdirectories

#### API Key Issues

**Problem:** "Invalid API key" or "Incorrect API key provided"

**Solutions:**

1. **Verify key format:**
   - OpenAI keys start with `sk-`
   - No spaces before/after
   - Complete key (usually 51 characters)

2. **Test key directly:**
   ```bash
   curl https://api.openai.com/v1/models \
     -H "Authorization: Bearer sk-your-key-here"
   ```

3. **Generate new key:**
   - Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
   - Revoke old key
   - Create new key
   - Update .env file

4. **Check key permissions:**
   - Ensure key has necessary permissions
   - Check if key is for correct organization

**Problem:** "You exceeded your current quota"

**Solutions:**

1. **Check billing:**
   - Go to [OpenAI Billing](https://platform.openai.com/account/billing)
   - Add payment method
   - Set usage limits

2. **Use free tier alternatives:**
   - Hugging Face Inference API
   - Local models with Ollama
   - Free tier of other providers

### API Connectivity

#### Connection Errors

**Problem:** "Connection error" or "Timeout"

**Solutions:**

1. **Check internet connection:**
   ```bash
   ping api.openai.com
   curl -I https://api.openai.com
   ```

2. **Check firewall/proxy:**
   - Disable VPN temporarily
   - Check corporate firewall settings
   - Configure proxy if needed:
     ```bash
     export HTTP_PROXY=http://proxy:port
     export HTTPS_PROXY=https://proxy:port
     ```

3. **Try different network:**
   - Switch to mobile hotspot
   - Use different WiFi
   - Check if IP is blocked

4. **Verify API status:**
   - Check [OpenAI Status](https://status.openai.com/)
   - Wait if service is down

#### Rate Limiting

**Problem:** "Rate limit exceeded" or "Too many requests"

**Solutions:**

1. **Implement rate limiting:**
   ```python
   from utils.api_helpers import RateLimiter
   
   rate_limiter = RateLimiter(max_requests=60, time_window=60)
   with rate_limiter:
       response = client.chat.completions.create(...)
   ```

2. **Add delays between calls:**
   ```python
   import time
   time.sleep(1)  # Wait 1 second between calls
   ```

3. **Use retry logic:**
   ```python
   from utils.api_helpers import retry_with_backoff
   
   @retry_with_backoff(max_retries=3)
   def call_api():
       return client.chat.completions.create(...)
   ```

4. **Check tier limits:**
   - Free tier: Lower limits
   - Paid tier: Higher limits
   - Upgrade if needed

### Docker Issues

#### Docker Won't Start

**Problem:** Docker container immediately exits

**Solutions:**

1. **Check logs:**
   ```bash
   docker-compose logs jupyter
   ```

2. **Verify Docker running:**
   ```bash
   docker info  # Should show system info, not error
   ```

3. **Start Docker Desktop:**
   - Windows/Mac: Open Docker Desktop application
   - Linux: `sudo systemctl start docker`

4. **Rebuild without cache:**
   ```bash
   docker-compose down
   docker-compose build --no-cache
   docker-compose up -d
   ```

#### Port Already in Use

**Problem:** "Error: bind: address already in use"

**Solutions:**

1. **Find process using port:**
   ```bash
   # macOS/Linux
   lsof -i :8888
   
   # Windows
   netstat -ano | findstr :8888
   ```

2. **Kill the process:**
   ```bash
   # macOS/Linux
   kill -9 <PID>
   
   # Windows
   taskkill /PID <PID> /F
   ```

3. **Change port:**
   Edit `.env`:
   ```
   DOCKER_PORT=9999
   ```
   
   Restart:
   ```bash
   docker-compose down
   docker-compose up -d
   ```

#### Can't Access JupyterLab

**Problem:** Browser can't connect to localhost:8888

**Solutions:**

1. **Verify container running:**
   ```bash
   docker-compose ps  # Should show "Up"
   ```

2. **Check port mapping:**
   ```bash
   docker-compose port jupyter 8888
   ```

3. **Try different URLs:**
   - `http://localhost:8888`
   - `http://127.0.0.1:8888`
   - `http://0.0.0.0:8888`

4. **Check firewall:**
   - Temporarily disable firewall
   - Add exception for port 8888

5. **Restart Docker:**
   ```bash
   docker-compose restart
   ```

#### GPU Not Detected in Docker

**Problem:** `nvidia-smi` fails or CUDA unavailable in container

**Solutions:**

1. **Verify GPU on host:**
   ```bash
   nvidia-smi  # Should show GPU info
   ```

2. **Install NVIDIA Container Toolkit:**
   ```bash
   # Ubuntu/Debian
   distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
   curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
   curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
     sudo tee /etc/apt/sources.list.d/nvidia-docker.list
   sudo apt-get update
   sudo apt-get install -y nvidia-docker2
   sudo systemctl restart docker
   ```

3. **Enable GPU in docker-compose.yml:**
   ```yaml
   services:
     jupyter:
       runtime: nvidia
       environment:
         - NVIDIA_VISIBLE_DEVICES=all
   ```

4. **Test GPU access:**
   ```bash
   docker run --rm --gpus all nvidia/cuda:11.8.0-base-ubuntu22.04 nvidia-smi
   ```

### Testing & Validation

#### Tests Failing

**Problem:** pytest tests failing

**Solutions:**

1. **Run with verbose output:**
   ```bash
   pytest -v
   ```

2. **Run specific test:**
   ```bash
   pytest tests/test_specific.py::test_function
   ```

3. **Check dependencies:**
   ```bash
   pip install pytest pytest-asyncio pytest-cov
   ```

4. **Clear pytest cache:**
   ```bash
   pytest --cache-clear
   rm -rf .pytest_cache __pycache__
   ```

#### Import Errors

**Problem:** "ModuleNotFoundError: No module named 'xxx'"

**Solutions:**

1. **Verify virtual environment activated:**
   ```bash
   which python  # Should show venv path
   ```

2. **Reinstall package:**
   ```bash
   pip install <package-name>
   ```

3. **Check PYTHONPATH:**
   ```bash
   export PYTHONPATH="${PYTHONPATH}:$(pwd)"
   ```

4. **Reinstall all dependencies:**
   ```bash
   pip install --force-reinstall -r requirements.txt
   ```

### Performance Issues

#### Slow Installation

**Problem:** pip install taking forever

**Solutions:**

1. **Use cached wheels:**
   ```bash
   pip install --cache-dir ~/.pip-cache -r requirements.txt
   ```

2. **Use CDN mirror:**
   ```bash
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
   ```

3. **Install pre-built binaries:**
   ```bash
   pip install --only-binary :all: -r requirements.txt
   ```

#### Slow API Calls

**Problem:** API calls taking too long

**Solutions:**

1. **Check latency:**
   ```python
   import time
   start = time.time()
   response = client.chat.completions.create(...)
   print(f"Latency: {time.time() - start:.2f}s")
   ```

2. **Use faster model:**
   - GPT-3.5-turbo instead of GPT-4
   - Reduce max_tokens

3. **Enable streaming:**
   ```python
   for chunk in client.chat.completions.create(..., stream=True):
       print(chunk)
   ```

4. **Check network:**
   - Use faster internet connection
   - Disable VPN
   - Check for bandwidth throttling

### Jupyter Issues

#### Jupyter Won't Start

**Problem:** jupyter lab command fails

**Solutions:**

1. **Reinstall Jupyter:**
   ```bash
   pip install --force-reinstall jupyter jupyterlab
   ```

2. **Clear Jupyter config:**
   ```bash
   jupyter lab --generate-config
   ```

3. **Try specific port:**
   ```bash
   jupyter lab --port=9999
   ```

4. **Check for conflicts:**
   ```bash
   jupyter lab paths
   jupyter troubleshoot
   ```

#### Kernel Issues

**Problem:** "Kernel died" or "Kernel not found"

**Solutions:**

1. **Restart kernel:**
   - In Jupyter: Kernel → Restart Kernel

2. **Install ipykernel:**
   ```bash
   pip install ipykernel
   python -m ipykernel install --user --name=venv
   ```

3. **Clear kernel caches:**
   ```bash
   rm -rf ~/.local/share/jupyter/runtime/*
   ```

4. **Check kernel list:**
   ```bash
   jupyter kernelspec list
   ```

## Getting More Help

### Before Asking for Help

1. **Check this guide** for your specific issue
2. **Run validation:**
   ```bash
   python validate_env.py
   ```
3. **Check error messages** carefully
4. **Search existing issues** on GitHub
5. **Try debugging steps** above

### How to Report Issues

When creating a GitHub issue, include:

1. **Clear title:** Describe the problem concisely

2. **Environment info:**
   ```bash
   python --version
   pip list
   uname -a  # or systeminfo on Windows
   ```

3. **Steps to reproduce:**
   - What you did
   - What happened
   - What you expected

4. **Error messages:**
   - Full error output
   - Relevant logs
   - Screenshots if helpful

5. **What you've tried:**
   - List debugging steps attempted
   - What worked/didn't work

### Resources

- [Documentation Index](../README.md#documentation)
- [Setup Guide](SETUP_GUIDE.md)
- [Environment Setup](../ENV_SETUP.md)
- [Docker Setup](DOCKER_SETUP.md)
- [GitHub Issues](https://github.com/your-repo/issues)
- [GitHub Discussions](https://github.com/your-repo/discussions)

## Still Stuck?

If you've tried everything:

1. **Create GitHub Issue** with details above
2. **Join community discussions**
3. **Check OpenAI Community** for API-specific issues
4. **Review official docs** for tools you're using

---

**Last Updated:** 2026-02-10

**Note:** This guide is continuously updated. If you find a solution not listed here, please contribute!
