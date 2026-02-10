#!/bin/bash
# ==============================================================================
# AI Engineer Learning Repository - Startup Script
# ==============================================================================
#
# This script provides one-command setup for the development environment.
# It handles Docker Compose orchestration and initial validation.
#
# ==============================================================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print colored output
print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

# Print banner
echo ""
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║   AI Engineer Learning Repository - Environment Setup     ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Check if Docker is installed
print_info "Checking Docker installation..."
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed!"
    echo ""
    echo "Please install Docker:"
    echo "  - Linux: https://docs.docker.com/engine/install/"
    echo "  - macOS: https://docs.docker.com/desktop/mac/install/"
    echo "  - Windows: https://docs.docker.com/desktop/windows/install/"
    echo ""
    exit 1
fi
print_success "Docker is installed ($(docker --version))"

# Check if Docker Compose is installed
print_info "Checking Docker Compose installation..."
if ! command -v docker-compose &> /dev/null; then
    print_error "Docker Compose is not installed!"
    echo ""
    echo "Please install Docker Compose:"
    echo "  https://docs.docker.com/compose/install/"
    echo ""
    exit 1
fi
print_success "Docker Compose is installed ($(docker-compose --version))"

# Check if Docker daemon is running
print_info "Checking Docker daemon..."
if ! docker info &> /dev/null; then
    print_error "Docker daemon is not running!"
    echo ""
    echo "Please start Docker Desktop or the Docker daemon."
    echo ""
    exit 1
fi
print_success "Docker daemon is running"

# Check if .env file exists
print_info "Checking environment configuration..."
if [ ! -f .env ]; then
    print_warning ".env file not found"
    print_info "Creating .env from .env.example..."
    cp .env.example .env
    print_warning "Please edit .env file and add your API keys!"
    echo ""
    echo "Required: OPENAI_API_KEY"
    echo "Optional: ANTHROPIC_API_KEY, HUGGINGFACE_API_KEY, etc."
    echo ""
    read -p "Press Enter after you've configured your .env file..."
fi
print_success "Environment configuration found"

# Check if data directories exist
print_info "Creating data directories..."
mkdir -p data models .cache .jupyter
print_success "Data directories created"

# Pull latest images (if any updates)
print_info "Checking for Docker image updates..."
docker-compose pull

# Build Docker image
print_info "Building Docker image (this may take a few minutes on first run)..."
docker-compose build

# Start services
print_info "Starting services..."
docker-compose up -d

# Wait for services to be healthy
print_info "Waiting for services to start..."
sleep 5

# Check if container is running
if docker-compose ps | grep -q "Up"; then
    print_success "Container is running"
else
    print_error "Container failed to start"
    echo ""
    echo "View logs:"
    echo "  docker-compose logs jupyter"
    echo ""
    exit 1
fi

# Run environment validation inside container
print_info "Running environment validation..."
if docker-compose exec -T jupyter python validate_env.py; then
    print_success "Environment validation passed"
else
    print_warning "Environment validation found issues (see output above)"
fi

# Print success message and instructions
echo ""
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                   Setup Complete! 🎉                      ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
print_success "Development environment is ready!"
echo ""
echo "📚 Access JupyterLab:"
echo "   http://localhost:8888"
echo ""
echo "🔧 Useful commands:"
echo "   View logs:        docker-compose logs -f jupyter"
echo "   Stop services:    docker-compose down"
echo "   Restart:          docker-compose restart"
echo "   Shell access:     docker-compose exec jupyter bash"
echo ""
echo "📖 Next steps:"
echo "   1. Open http://localhost:8888 in your browser"
echo "   2. Navigate to 01-python-fundamentals/"
echo "   3. Start with the README.md"
echo ""
echo "💡 Need help? Check docs/DOCKER_SETUP.md"
echo ""
