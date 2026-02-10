# ==============================================================================
# Dockerfile for AI Engineer Learning Repository
# ==============================================================================
# 
# This Dockerfile creates a complete development environment with:
# - Python 3.11
# - JupyterLab for interactive development
# - All AI/ML dependencies
# - Optional GPU support (CUDA)
# - Development tools
#
# ==============================================================================

# Use official Python 3.11 slim image as base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    # Build essentials
    build-essential \
    gcc \
    g++ \
    make \
    # Git for version control
    git \
    # Utilities
    curl \
    wget \
    vim \
    nano \
    # Clean up
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip setuptools wheel

# Copy requirements files
COPY requirements.txt requirements-dev.txt ./

# Install Python dependencies
RUN pip install -r requirements.txt && \
    pip install -r requirements-dev.txt

# Optional: Install PyTorch with CPU support (uncomment for GPU, see below)
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Create directories for data, models, and cache
RUN mkdir -p /workspace/data \
    /workspace/models \
    /workspace/.cache \
    /workspace/.jupyter

# Configure JupyterLab
RUN jupyter lab --generate-config && \
    echo "c.ServerApp.ip = '0.0.0.0'" >> /root/.jupyter/jupyter_lab_config.py && \
    echo "c.ServerApp.port = 8888" >> /root/.jupyter/jupyter_lab_config.py && \
    echo "c.ServerApp.open_browser = False" >> /root/.jupyter/jupyter_lab_config.py && \
    echo "c.ServerApp.allow_root = True" >> /root/.jupyter/jupyter_lab_config.py && \
    echo "c.ServerApp.token = ''" >> /root/.jupyter/jupyter_lab_config.py && \
    echo "c.ServerApp.password = ''" >> /root/.jupyter/jupyter_lab_config.py

# Expose JupyterLab port
EXPOSE 8888

# Set default command to start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

# ==============================================================================
# GPU Support (NVIDIA CUDA)
# ==============================================================================
# For GPU support, use nvidia/cuda base image instead:
#
# FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04
# 
# Then install Python 3.11:
# RUN apt-get update && apt-get install -y \
#     python3.11 \
#     python3.11-dev \
#     python3-pip
#
# And install PyTorch with CUDA:
# RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
#
# ==============================================================================
# Build Instructions:
# ==============================================================================
# Build image:
#   docker build -t ai-engineer-learning .
#
# Run container:
#   docker run -p 8888:8888 -v $(pwd):/workspace ai-engineer-learning
#
# Or use docker-compose (recommended):
#   docker-compose up
# ==============================================================================
