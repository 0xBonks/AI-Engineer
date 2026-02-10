# Docker Setup Guide

## Overview

This guide provides comprehensive instructions for setting up and using the Docker development environment for the AI Engineer Learning Repository.

## Why Docker?

**Benefits:**
- **Zero environment issues** - Everything pre-configured and tested
- **Cross-platform** - Works on Linux, macOS, and Windows
- **Isolated** - Doesn't interfere with your system Python
- **Reproducible** - Identical environment for all learners
- **JupyterLab included** - Interactive development ready out-of-the-box

## Prerequisites

### Required

1. **Docker Desktop** (recommended) or Docker Engine
   - **macOS**: [Docker Desktop for Mac](https://docs.docker.com/desktop/mac/install/)
   - **Windows**: [Docker Desktop for Windows](https://docs.docker.com/desktop/windows/install/)
   - **Linux**: [Docker Engine](https://docs.docker.com/engine/install/)

2. **Docker Compose** (included with Docker Desktop)
   - Linux users may need to [install separately](https://docs.docker.com/compose/install/)

3. **System Requirements**:
   - CPU: 2+ cores recommended (4+ for GPU work)
   - RAM: 4GB minimum, 8GB+ recommended
   - Disk: 10GB free space (20GB+ for full course with models)

### Optional

- **NVIDIA GPU** for local model training/inference
- **NVIDIA Docker Runtime** for GPU support in containers

## Quick Start

### One-Command Setup

```bash
# Clone repository
git clone <repository-url>
cd AI-Engineer

# Run startup script
./start.sh
```

The startup script will:
1. Check Docker installation
2. Create `.env` file from template (if needed)
3. Build Docker image
4. Start services
5. Validate environment
6. Display access instructions

### Access JupyterLab

Open your browser to:
```
http://localhost:8888
```

No password required by default (development mode).

## Manual Setup

If you prefer manual control:

### Step 1: Create .env File

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```bash
OPENAI_API_KEY=sk-your-actual-key-here
```

### Step 2: Build Docker Image

```bash
docker-compose build
```

This may take 5-10 minutes on first run.

### Step 3: Start Services

```bash
docker-compose up -d
```

The `-d` flag runs in detached mode (background).

### Step 4: Verify

```bash
# Check container status
docker-compose ps

# View logs
docker-compose logs jupyter

# Run validation
docker-compose exec jupyter python validate_env.py
```

## Docker Commands Reference

### Service Management

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# Restart services
docker-compose restart

# View status
docker-compose ps

# View logs (follow mode)
docker-compose logs -f jupyter

# View logs (last 100 lines)
docker-compose logs --tail=100 jupyter
```

### Container Access

```bash
# Open bash shell in container
docker-compose exec jupyter bash

# Run Python script
docker-compose exec jupyter python script.py

# Run pytest
docker-compose exec jupyter pytest

# Install additional package
docker-compose exec jupyter pip install package-name
```

### Maintenance

```bash
# Rebuild after dependency changes
docker-compose up -d --build

# Remove container and volumes
docker-compose down -v

# View resource usage
docker stats

# Clean up Docker system
docker system prune -a
```

## GPU Support (NVIDIA)

### Prerequisites

1. **NVIDIA GPU** with CUDA support
2. **NVIDIA drivers** installed on host
3. **NVIDIA Container Toolkit** installed

### Install NVIDIA Container Toolkit

**Ubuntu/Debian:**
```bash
# Add repository
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list

# Install
sudo apt-get update
sudo apt-get install -y nvidia-docker2

# Restart Docker
sudo systemctl restart docker
```

**Other Linux distributions**: See [NVIDIA Container Toolkit Installation Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

### Enable GPU in Docker Compose

Edit `docker-compose.yml` and uncomment GPU-related sections:

```yaml
services:
  jupyter:
    # Uncomment these lines:
    runtime: nvidia
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
      - NVIDIA_DRIVER_CAPABILITIES=compute,utility
```

### Verify GPU Access

```bash
# Start container with GPU support
docker-compose up -d --build

# Check GPU availability
docker-compose exec jupyter nvidia-smi

# Test in Python
docker-compose exec jupyter python -c "import torch; print(torch.cuda.is_available())"
```

## Configuration

### Port Configuration

Default port: `8888`

To change:
1. Edit `.env`:
   ```bash
   DOCKER_PORT=9999
   ```
2. Restart services:
   ```bash
   docker-compose down
   docker-compose up -d
   ```

### Volume Mounts

The following directories are mounted from host to container:

| Host Path | Container Path | Purpose |
|-----------|---------------|---------|
| `.` (repository root) | `/workspace` | Code and notebooks |
| `./data` | `/workspace/data` | Vector databases, datasets |
| `./models` | `/workspace/models` | Downloaded model weights |
| `./.cache` | `/workspace/.cache` | Caching (transformers, etc.) |
| `./.jupyter` | `/root/.jupyter` | Jupyter configuration |

This means:
- Changes in container persist on host
- Files created in container appear on host
- Large files (models, data) stay on host

### Resource Limits

To limit container resources, edit `docker-compose.yml`:

```yaml
services:
  jupyter:
    deploy:
      resources:
        limits:
          cpus: '4'
          memory: 8G
        reservations:
          cpus: '2'
          memory: 4G
```

## Troubleshooting

### Container Won't Start

**Problem:** Container immediately exits

**Solutions:**

1. Check logs:
   ```bash
   docker-compose logs jupyter
   ```

2. Verify .env file exists and has valid format

3. Try rebuilding:
   ```bash
   docker-compose down
   docker-compose build --no-cache
   docker-compose up -d
   ```

### Port Already in Use

**Problem:** `Error: bind: address already in use`

**Solutions:**

1. **Option A**: Change port in `.env`:
   ```bash
   DOCKER_PORT=9999
   ```

2. **Option B**: Stop conflicting service:
   ```bash
   # Find process using port 8888
   lsof -i :8888  # macOS/Linux
   netstat -ano | findstr :8888  # Windows
   
   # Stop the process
   kill <PID>
   ```

### Can't Connect to JupyterLab

**Problem:** Browser can't reach `http://localhost:8888`

**Solutions:**

1. **Verify container is running:**
   ```bash
   docker-compose ps
   ```

2. **Check logs for errors:**
   ```bash
   docker-compose logs jupyter
   ```

3. **Try explicit IP:**
   ```
   http://127.0.0.1:8888
   ```

4. **Check firewall settings**

### Permission Errors

**Problem:** Permission denied errors in container

**Linux-specific solution:**

Files created in container may have root ownership. Fix:

```bash
# Run container with your user ID
docker-compose down
docker-compose run --user $(id -u):$(id -g) jupyter bash
```

Or add to `docker-compose.yml`:
```yaml
services:
  jupyter:
    user: "${UID}:${GID}"
```

### Out of Disk Space

**Problem:** Docker images consuming too much space

**Solutions:**

```bash
# Check Docker disk usage
docker system df

# Clean up unused resources
docker system prune -a

# Remove specific images
docker images
docker rmi <image-id>

# Remove all stopped containers
docker container prune
```

### Slow Performance

**Problem:** Container is slow

**Solutions:**

1. **Increase Docker resources** (Docker Desktop Settings)
   - More CPUs
   - More memory

2. **Check resource usage:**
   ```bash
   docker stats
   ```

3. **Close other applications**

4. **Use volume caching** (macOS):
   Edit `docker-compose.yml`:
   ```yaml
   volumes:
     - .:/workspace:cached
   ```

### GPU Not Detected

**Problem:** `nvidia-smi` fails or CUDA unavailable

**Solutions:**

1. **Verify NVIDIA drivers on host:**
   ```bash
   nvidia-smi
   ```

2. **Check NVIDIA Docker runtime:**
   ```bash
   docker run --rm --gpus all nvidia/cuda:11.8.0-base-ubuntu22.04 nvidia-smi
   ```

3. **Verify docker-compose.yml has GPU config**

4. **Restart Docker daemon:**
   ```bash
   sudo systemctl restart docker
   ```

## Alternative: Docker Desktop

If using Docker Desktop GUI:

1. **Open Docker Desktop**
2. **Import** `docker-compose.yml`
3. **Start** the stack
4. **View** containers and logs in GUI

## Alternative: Cloud Deployment

### AWS EC2

```bash
# Launch Ubuntu instance with Docker
# Install Docker and Docker Compose
# Clone repository
# Run setup

# Expose port 8888 in Security Group
# Access via public IP: http://<public-ip>:8888
```

**Security Note:** Use SSH tunneling for production:
```bash
ssh -L 8888:localhost:8888 user@remote-host
```

### Google Cloud Run / Azure Container Instances

Deploy Docker image to cloud:

```bash
# Build and push image
docker build -t gcr.io/your-project/ai-engineer .
docker push gcr.io/your-project/ai-engineer

# Deploy to Cloud Run
gcloud run deploy ai-engineer \
  --image gcr.io/your-project/ai-engineer \
  --platform managed
```

## Development Workflow

### Typical Workflow

1. **Start environment:**
   ```bash
   docker-compose up -d
   ```

2. **Open JupyterLab** in browser

3. **Work on notebooks/code**

4. **Run tests:**
   ```bash
   docker-compose exec jupyter pytest
   ```

5. **Stop when done:**
   ```bash
   docker-compose down
   ```

### Hot Reloading

Changes to files on host are immediately visible in container. No restart needed.

### Adding Dependencies

**Temporary** (lost on container restart):
```bash
docker-compose exec jupyter pip install package-name
```

**Permanent**:
1. Add to `requirements.txt`
2. Rebuild:
   ```bash
   docker-compose up -d --build
   ```

### Debugging

```bash
# Interactive shell
docker-compose exec jupyter bash

# Python shell
docker-compose exec jupyter python

# IPython shell
docker-compose exec jupyter ipython

# Run with debugger
docker-compose exec jupyter python -m pdb script.py
```

## Best Practices

1. **Always use `docker-compose`** (not raw `docker` commands)
2. **Keep `.env` out of version control** (in `.gitignore`)
3. **Commit `docker-compose.yml` and `Dockerfile`**
4. **Use volume mounts** for data persistence
5. **Stop containers when not in use** (saves resources)
6. **Regularly update base image** for security patches
7. **Use tags for production** (not `latest`)

## Comparison: Docker vs Local

| Aspect | Docker | Local Setup |
|--------|--------|-------------|
| Setup Time | 10-15 min | 30-60 min |
| Environment Issues | None | Common |
| Isolation | Complete | None |
| Resource Usage | Higher | Lower |
| GPU Support | Requires setup | Native |
| Portability | Excellent | Poor |

**Recommendation:** Use Docker for learning, local for production development.

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Best Practices for Writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/overview.html)

## Getting Help

If you encounter issues:

1. Check this guide's [Troubleshooting](#troubleshooting) section
2. Check [main TROUBLESHOOTING.md](TROUBLESHOOTING.md)
3. Search [GitHub Issues](https://github.com/your-repo/issues)
4. Create new issue with:
   - OS and Docker version
   - Error messages
   - Output of `docker-compose logs`

---

**Last Updated:** 2026-02-10  
**Docker Version:** 24.0+  
**Docker Compose Version:** 2.0+
