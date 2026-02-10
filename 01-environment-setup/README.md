# Module 01: Environment Setup & Infrastructure

## Overview

This module covers the foundational setup for your AI engineering journey. You'll learn how to configure a robust development environment, manage dependencies, track API costs, and use validation tools to ensure everything works correctly.

## Learning Objectives

By completing this module, you will be able to:

- Set up a Docker-based development environment with JupyterLab and GPU support
- Install and manage Python dependencies with version pinning
- Configure API keys securely using environment variables
- Use validation scripts to verify your environment setup
- Track API costs and optimize for budget efficiency
- Understand CI/CD basics for automated testing

## Prerequisites

- **Experience**: Intermediate programming skills in any language
- **System**: Python 3.11+ installed locally
- **Tools**: Docker and Docker Compose installed
- **Hardware**: Local machine (GPU optional but recommended for later modules)

## Estimated Time

**2-3 hours** to complete setup and exercises

## Key Concepts

### 1. Development Environment
- Docker containers for consistent environments
- JupyterLab for interactive development
- GPU support configuration (CUDA)
- Volume mounts and port mappings

### 2. Dependency Management
- Version pinning for stability
- requirements.txt vs requirements-dev.txt
- Dependency security and updates
- Virtual environments

### 3. Configuration Management
- Environment variables (.env files)
- Secure API key storage
- Configuration best practices
- .gitignore for sensitive files

### 4. Validation & Testing
- Environment validation scripts
- Automated dependency checks
- CI/CD pipeline basics
- Pre-commit hooks

### 5. Cost Tracking
- Token counting with tiktoken
- API cost calculation
- Budget monitoring and alerts
- Cost optimization strategies

## Structure

```
01-environment-setup/
├── README.md           # This file
├── notebooks/          # Interactive Jupyter demos
│   ├── 01-docker-setup.ipynb
│   ├── 02-env-validation.ipynb
│   └── 03-cost-tracking.ipynb
├── exercises/          # Hands-on practice
│   ├── 01-setup-environment.md
│   ├── 02-configure-apis.md
│   └── 03-track-costs.md
├── tests/              # Automated validation
│   └── test_environment.py
└── solutions/          # Reference implementations
    └── solutions.md
```

## Getting Started

### 1. Initial Setup

```bash
# Clone the repository (if not already done)
git clone <repository-url>
cd AI-Engineer

# Copy environment template
cp .env.example .env

# Edit .env and add your API keys
nano .env  # or use your preferred editor
```

### 2. Docker Setup (Recommended)

```bash
# Start the development environment
./start.sh

# This will:
# - Build the Docker image with all dependencies
# - Start JupyterLab on http://localhost:8888
# - Mount your code directory
# - Configure GPU support (if available)
```

### 3. Local Setup (Alternative)

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 4. Validate Your Setup

```bash
# Run validation script
./validate_env.py

# Expected output:
# ✓ Python 3.11+ detected
# ✓ All dependencies installed
# ✓ API keys configured
# ✓ API connectivity verified
```

## Exercises

### Exercise 1: Environment Setup
**File**: `exercises/01-setup-environment.md`

Set up your development environment using either Docker or local installation. Verify all components are working.

**Success Criteria**:
- Docker environment starts successfully OR local environment activated
- JupyterLab accessible at http://localhost:8888
- All dependencies installed without errors

### Exercise 2: API Configuration
**File**: `exercises/02-configure-apis.md`

Configure your API keys and test connectivity to OpenAI and other services.

**Success Criteria**:
- .env file contains all required keys
- Validation script confirms API connectivity
- No API keys committed to git

### Exercise 3: Cost Tracking
**File**: `exercises/03-track-costs.md`

Use the cost tracking utilities to monitor API usage and estimate costs.

**Success Criteria**:
- Successfully track tokens for a sample API call
- Calculate estimated cost
- Set up cost alerts

## Resources

### Official Documentation
- [Docker Documentation](https://docs.docker.com/)
- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [OpenAI API Keys](https://platform.openai.com/api-keys)

### Repository Documentation
- [SETUP_GUIDE.md](../docs/SETUP_GUIDE.md) - Complete setup walkthrough
- [DOCKER_SETUP.md](../docs/DOCKER_SETUP.md) - Docker-specific instructions
- [TROUBLESHOOTING.md](../docs/TROUBLESHOOTING.md) - Common issues and fixes
- [COST_TRACKING.md](../docs/COST_TRACKING.md) - Cost tracking guide

### Tools & Utilities
- **validate_env.py**: Environment validation script
- **utils/validation.py**: Validation helper functions
- **utils/cost_tracker.py**: Cost tracking utilities
- **utils/api_helpers.py**: API interaction helpers

## Next Steps

After completing this module:

1. ✅ Verify all exercises pass their tests
2. ✅ Ensure cost tracking is working
3. ➡️ Proceed to **Module 02: Python Fundamentals for AI**

## Common Issues

### Docker Won't Start
- Ensure Docker Desktop is running
- Check port 8888 is not already in use
- See [TROUBLESHOOTING.md](../docs/TROUBLESHOOTING.md#docker-issues)

### API Key Errors
- Verify keys are in .env file (not .env.example)
- Ensure no extra spaces or quotes around keys
- Check API key validity at provider dashboards

### Dependency Conflicts
- Use the exact versions in requirements.txt
- Clear pip cache: `pip cache purge`
- Rebuild Docker image: `docker-compose build --no-cache`

## Notes

- **API Costs**: Most exercises use minimal API calls ($0.01-0.10 total)
- **GPU Optional**: Not required for this module, but helpful later
- **Time Commitment**: Setup is frontloaded; later modules move faster
- **Help**: See main repository [CONTRIBUTING.md](../CONTRIBUTING.md) for support

---

**Module Status**: ✅ Infrastructure Complete | ⏭️ Next: Python Fundamentals
