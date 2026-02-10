"""
Environment validation utilities for AI Engineer Learning Repository.

This module provides comprehensive validation of the development environment including:
- Python version checks
- Dependency verification
- API connectivity tests
- GPU availability checks
- Environment variable validation
"""

import sys
import importlib
import os
from typing import Dict, List, Tuple, Optional
import subprocess


class Colors:
    """ANSI color codes for terminal output."""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'


def print_header(text: str) -> None:
    """Print formatted header."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'=' * 70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text:^70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'=' * 70}{Colors.END}\n")


def print_success(text: str) -> None:
    """Print success message."""
    print(f"{Colors.GREEN}✓{Colors.END} {text}")


def print_error(text: str) -> None:
    """Print error message."""
    print(f"{Colors.RED}✗{Colors.END} {text}")


def print_warning(text: str) -> None:
    """Print warning message."""
    print(f"{Colors.YELLOW}⚠{Colors.END} {text}")


def print_info(text: str) -> None:
    """Print info message."""
    print(f"{Colors.BLUE}ℹ{Colors.END} {text}")


def check_python_version() -> Tuple[bool, str]:
    """Check if Python version is 3.11 or higher."""
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    
    if version.major >= 3 and version.minor >= 11:
        return True, f"Python {version_str}"
    else:
        return False, f"Python {version_str} (3.11+ required)"


def check_package_installed(package_name: str, import_name: Optional[str] = None) -> Tuple[bool, str]:
    """Check if a Python package is installed."""
    import_name = import_name or package_name
    
    try:
        module = importlib.import_module(import_name)
        version = getattr(module, '__version__', 'unknown')
        return True, f"{package_name} {version}"
    except ImportError:
        return False, f"{package_name} not installed"


def check_required_dependencies() -> Dict[str, Tuple[bool, str]]:
    """Check all required dependencies."""
    dependencies = {
        'openai': ('openai', None),
        'tiktoken': ('tiktoken', None),
        'pydantic': ('pydantic', None),
        'python-dotenv': ('dotenv', None),
        'requests': ('requests', None),
        'httpx': ('httpx', None),
        'aiohttp': ('aiohttp', None),
        'numpy': ('numpy', None),
        'pandas': ('pandas', None),
        'langchain': ('langchain', None),
        'llama-index': ('llama_index', None),
        'chromadb': ('chromadb', None),
        'sentence-transformers': ('sentence_transformers', None),
        'transformers': ('transformers', None),
        'jupyter': ('jupyter', None),
        'pytest': ('pytest', None),
    }
    
    results = {}
    for package_name, (import_name, _) in dependencies.items():
        results[package_name] = check_package_installed(package_name, import_name)
    
    return results


def check_environment_variables() -> Dict[str, Tuple[bool, str]]:
    """Check required environment variables."""
    from dotenv import load_dotenv
    load_dotenv()
    
    variables = {
        'OPENAI_API_KEY': True,  # Required
        'ANTHROPIC_API_KEY': False,  # Optional
        'HUGGINGFACE_API_KEY': False,  # Optional
        'GOOGLE_API_KEY': False,  # Optional
    }
    
    results = {}
    for var_name, required in variables.items():
        value = os.getenv(var_name)
        
        if value:
            # Mask the key for display
            if len(value) > 8:
                masked_value = f"{value[:4]}...{value[-4:]}"
            else:
                masked_value = "***"
            results[var_name] = (True, f"Set ({masked_value})")
        else:
            if required:
                results[var_name] = (False, "Not set (required)")
            else:
                results[var_name] = (False, "Not set (optional)")
    
    return results


def check_openai_connectivity() -> Tuple[bool, str]:
    """Test OpenAI API connectivity."""
    try:
        from openai import OpenAI
        import os
        
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            return False, "API key not configured"
        
        client = OpenAI(api_key=api_key)
        
        # Simple API test - list models
        models = client.models.list()
        model_count = len(list(models))
        
        return True, f"Connected (found {model_count} models)"
    
    except Exception as e:
        return False, f"Connection failed: {str(e)}"


def check_gpu_availability() -> Tuple[bool, str]:
    """Check if GPU is available for PyTorch."""
    try:
        import torch
        
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            gpu_count = torch.cuda.device_count()
            return True, f"{gpu_count} GPU(s) available: {gpu_name}"
        else:
            return False, "No GPU detected (CPU only)"
    
    except ImportError:
        return False, "PyTorch not installed"
    except Exception as e:
        return False, f"GPU check failed: {str(e)}"


def check_vector_databases() -> Dict[str, Tuple[bool, str]]:
    """Check vector database availability."""
    results = {}
    
    # ChromaDB
    try:
        import chromadb
        client = chromadb.Client()
        results['ChromaDB'] = (True, f"Ready (version {chromadb.__version__})")
    except ImportError:
        results['ChromaDB'] = (False, "Not installed")
    except Exception as e:
        results['ChromaDB'] = (False, f"Error: {str(e)}")
    
    # Pinecone (optional)
    try:
        import pinecone
        results['Pinecone'] = (True, f"Installed (version {pinecone.__version__})")
    except ImportError:
        results['Pinecone'] = (False, "Not installed (optional)")
    
    # Weaviate (optional)
    try:
        import weaviate
        results['Weaviate'] = (True, f"Installed (version {weaviate.__version__})")
    except ImportError:
        results['Weaviate'] = (False, "Not installed (optional)")
    
    return results


def check_disk_space() -> Tuple[bool, str]:
    """Check available disk space."""
    try:
        import shutil
        
        total, used, free = shutil.disk_usage("/")
        free_gb = free // (2**30)  # Convert to GB
        
        if free_gb >= 10:
            return True, f"{free_gb} GB free"
        else:
            return False, f"{free_gb} GB free (10 GB+ recommended)"
    
    except Exception as e:
        return False, f"Could not check disk space: {str(e)}"


def run_validation() -> bool:
    """Run complete environment validation."""
    all_checks_passed = True
    
    # Header
    print_header("AI Engineer Learning Repository - Environment Validation")
    
    # Python version
    print(f"{Colors.BOLD}Python Version:{Colors.END}")
    success, message = check_python_version()
    if success:
        print_success(message)
    else:
        print_error(message)
        all_checks_passed = False
    
    # Dependencies
    print(f"\n{Colors.BOLD}Required Dependencies:{Colors.END}")
    deps = check_required_dependencies()
    
    failed_deps = []
    for package, (success, message) in deps.items():
        if success:
            print_success(message)
        else:
            print_error(message)
            failed_deps.append(package)
            all_checks_passed = False
    
    if failed_deps:
        print_warning(f"\nMissing dependencies: {', '.join(failed_deps)}")
        print_info("Install with: pip install -r requirements.txt")
    
    # Environment variables
    print(f"\n{Colors.BOLD}Environment Variables:{Colors.END}")
    env_vars = check_environment_variables()
    
    for var_name, (success, message) in env_vars.items():
        if success:
            print_success(f"{var_name}: {message}")
        elif "required" in message:
            print_error(f"{var_name}: {message}")
            all_checks_passed = False
        else:
            print_warning(f"{var_name}: {message}")
    
    # API Connectivity
    print(f"\n{Colors.BOLD}API Connectivity:{Colors.END}")
    success, message = check_openai_connectivity()
    if success:
        print_success(f"OpenAI API: {message}")
    else:
        print_error(f"OpenAI API: {message}")
        all_checks_passed = False
    
    # Vector Databases
    print(f"\n{Colors.BOLD}Vector Databases:{Colors.END}")
    vector_dbs = check_vector_databases()
    
    for db_name, (success, message) in vector_dbs.items():
        if success:
            print_success(f"{db_name}: {message}")
        elif "optional" in message:
            print_warning(f"{db_name}: {message}")
        else:
            print_error(f"{db_name}: {message}")
            if db_name == "ChromaDB":  # ChromaDB is required
                all_checks_passed = False
    
    # GPU (optional)
    print(f"\n{Colors.BOLD}Hardware:{Colors.END}")
    success, message = check_gpu_availability()
    if success:
        print_success(f"GPU: {message}")
    else:
        print_warning(f"GPU: {message}")
    
    # Disk space
    success, message = check_disk_space()
    if success:
        print_success(f"Disk Space: {message}")
    else:
        print_warning(f"Disk Space: {message}")
    
    # Summary
    print_header("Validation Summary")
    
    if all_checks_passed:
        print_success("All critical checks passed! ✓")
        print_info("\nYou're ready to start learning!")
        print_info("Next steps:")
        print_info("  1. cd 01-python-fundamentals")
        print_info("  2. jupyter lab")
        print_info("  3. Open notebooks/01-async-basics.ipynb")
        return True
    else:
        print_error("Some critical checks failed! ✗")
        print_info("\nPlease fix the errors above before proceeding.")
        print_info("See ENV_SETUP.md for detailed setup instructions.")
        return False


if __name__ == "__main__":
    success = run_validation()
    sys.exit(0 if success else 1)
