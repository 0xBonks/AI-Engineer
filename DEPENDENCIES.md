# Dependency Management Strategy

## Overview

This document outlines the dependency management strategy for the AI Engineer Learning Repository, including version pinning policy, update procedures, and security considerations.

## Version Pinning Policy

### Core Principles

1. **All versions are pinned** (`==`) for reproducibility
2. **Monthly dependency reviews** to check for updates and security issues
3. **Test thoroughly** before updating pinned versions
4. **Document breaking changes** when updating dependencies

### Why Pin Versions?

- **Reproducibility**: Ensures all learners have identical environments
- **Stability**: Prevents unexpected breakage from automatic updates
- **Security**: Controlled updates with review process
- **Testing**: Known working versions that pass all tests

## Dependencies Categories

### Production Dependencies (requirements.txt)

**OpenAI SDK & AI APIs:**
- `openai` - OpenAI API client
- `anthropic` - Claude API client (optional)
- `google-generativeai` - Gemini API client

**Hugging Face Ecosystem:**
- `transformers` - NLP models and pipelines
- `huggingface-hub` - Model downloads and management
- `sentence-transformers` - Embedding generation
- `accelerate` - Model optimization

**Vector Databases:**
- `chromadb` - Primary vector database
- `pinecone-client` - Pinecone vector database
- `weaviate-client` - Weaviate vector database

**AI Frameworks:**
- `langchain` - LLM application framework
- `llama-index` - RAG-focused data framework

**Core Utilities:**
- `tiktoken` - Token counting
- `pydantic` - Data validation
- `python-dotenv` - Environment configuration

### Development Dependencies (requirements-dev.txt)

**Code Quality:**
- `black` - Code formatting
- `ruff` - Fast Python linting
- `mypy` - Static type checking

**Testing:**
- `pytest` - Testing framework
- `pytest-asyncio` - Async test support
- `pytest-cov` - Coverage reporting

**Security:**
- `pip-audit` - Vulnerability scanning
- `safety` - Security advisories
- `bandit` - Security linting

## Update Strategy

### Monthly Dependency Review

**Schedule:** First week of each month

**Process:**

1. **Check for updates:**
   ```bash
   pip list --outdated
   ```

2. **Review changelogs:**
   - Visit package repositories
   - Read CHANGELOG.md and release notes
   - Identify breaking changes

3. **Security scan:**
   ```bash
   pip-audit
   safety check
   ```

4. **Test updates in isolation:**
   ```bash
   # Create test environment
   python -m venv test-env
   source test-env/bin/activate
   
   # Install with updated version
   pip install package-name==X.Y.Z
   
   # Run full test suite
   pytest
   ```

5. **Update requirements files:**
   - Update version pins
   - Add comments for breaking changes
   - Document migration steps if needed

6. **Commit and CI/CD:**
   ```bash
   git add requirements*.txt
   git commit -m "chore: update dependencies (YYYY-MM)"
   git push
   # Verify CI/CD passes
   ```

### Emergency Security Updates

For critical security vulnerabilities:

1. **Immediate assessment** of vulnerability impact
2. **Create hotfix branch**
3. **Update affected package**
4. **Run targeted tests**
5. **Deploy immediately** if critical
6. **Document in SECURITY.md**

## Dependency Conflicts

### Resolution Strategy

1. **Identify conflict:**
   ```bash
   pip install -r requirements.txt 2>&1 | grep conflict
   ```

2. **Check dependency tree:**
   ```bash
   pip install pipdeptree
   pipdeptree --warn conflict
   ```

3. **Resolution options:**
   - Update conflicting packages together
   - Use compatible version ranges temporarily
   - Remove non-critical packages if necessary

4. **Test thoroughly:**
   - Run full test suite
   - Manual testing of affected modules

## Security Considerations

### Regular Security Scans

**Weekly automated scans** via CI/CD:

```yaml
# .github/workflows/security.yml
- name: Security scan
  run: |
    pip-audit
    safety check
```

### Vulnerability Response

**Severity Levels:**

- **Critical**: Immediate update required (< 24 hours)
- **High**: Update within 1 week
- **Medium**: Update in next monthly review
- **Low**: Update when convenient

### Security Best Practices

1. **Never commit `.env` files** with API keys
2. **Use environment variables** for all secrets
3. **Regularly rotate API keys**
4. **Monitor API usage** for anomalies
5. **Implement rate limiting** in production code

## Platform-Specific Dependencies

### PyTorch (Optional GPU Support)

Not included in base requirements due to:
- Large download size (2-5 GB)
- Platform-specific builds (CUDA, CPU, MPS)
- Not required for core learning path

**Installation when needed:**

```bash
# CUDA 11.8 (NVIDIA GPUs)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# CPU only
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# MPS (Apple Silicon)
pip install torch torchvision torchaudio
```

### Windows-Specific Notes

Some packages may require additional setup on Windows:
- Ensure Microsoft Visual C++ Build Tools installed
- Use `python -m pip` instead of `pip` if PATH issues
- Consider WSL2 for better compatibility

## Dependency Documentation

### Adding New Dependencies

When adding a new dependency:

1. **Justify the addition:**
   - What problem does it solve?
   - Why not use existing dependency?
   - Is it actively maintained?

2. **Add to requirements.txt with:**
   - Version pinning
   - Inline comment explaining purpose
   - Category grouping

3. **Update this document:**
   - Add to relevant category
   - Document any special considerations

4. **Test thoroughly:**
   - Ensure no conflicts
   - Verify all tests pass
   - Check install time impact

### Removing Dependencies

Before removing a dependency:

1. **Search codebase** for usage:
   ```bash
   rg "import package_name"
   ```

2. **Check transitive dependencies:**
   ```bash
   pipdeptree --packages package-name
   ```

3. **Update documentation**

4. **Run full test suite**

## Troubleshooting

### Common Issues

**Problem: Dependency conflict during install**
```bash
# Solution: Use constraint file
pip install -r requirements.txt --constraint constraints.txt
```

**Problem: Package not found**
```bash
# Solution: Check PyPI availability
pip index versions package-name
```

**Problem: Slow installation**
```bash
# Solution: Use pip cache
pip install -r requirements.txt --cache-dir ~/.pip-cache
```

### Getting Help

1. **Check documentation** in `docs/TROUBLESHOOTING.md`
2. **Search GitHub issues** in this repository
3. **Open new issue** with:
   - Python version
   - Operating system
   - Full error message
   - Steps to reproduce

## Tools

### Useful Commands

```bash
# List installed packages
pip list

# Show package details
pip show package-name

# Check for outdated packages
pip list --outdated

# Generate dependency tree
pip install pipdeptree && pipdeptree

# Export current environment
pip freeze > requirements-freeze.txt

# Install from requirements
pip install -r requirements.txt

# Install with hash checking (extra security)
pip install --require-hashes -r requirements.txt
```

### Automation Scripts

Located in `scripts/`:
- `check-deps.sh` - Check for outdated dependencies
- `security-scan.sh` - Run security scans
- `update-deps.sh` - Update dependencies safely

## References

- [pip User Guide](https://pip.pypa.io/en/stable/user_guide/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [pip-audit Documentation](https://github.com/pypa/pip-audit)
- [Safety Documentation](https://github.com/pyupio/safety)

---

**Last Updated:** 2026-02-10  
**Next Review:** 2026-03-01
