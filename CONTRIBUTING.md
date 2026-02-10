# Contributing to AI Engineer Learning Repository

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Workflow](#development-workflow)
- [Style Guidelines](#style-guidelines)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project follows a Code of Conduct to ensure a welcoming environment:

- **Be respectful** and inclusive
- **Be collaborative** and constructive
- **Focus on learning** and teaching
- **Accept constructive criticism** gracefully
- **Report inappropriate behavior** to maintainers

## Getting Started

### Prerequisites

- Python 3.11+
- Git
- Docker (optional but recommended)
- Familiarity with AI/ML concepts

### Setup Development Environment

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub
   git clone https://github.com/YOUR_USERNAME/AI-Engineer.git
   cd AI-Engineer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

5. **Configure environment**
   ```bash
   cp .env.example .env
   # Add your API keys to .env
   ```

6. **Verify setup**
   ```bash
   python validate_env.py
   pytest
   ```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

1. **Bug Reports**
   - Found an issue? Report it!
   - Include steps to reproduce
   - Provide error messages and system info

2. **Feature Requests**
   - Suggest new exercises or modules
   - Propose improvements to existing content
   - Share ideas for better learning experience

3. **Documentation**
   - Fix typos and clarify explanations
   - Add examples and tutorials
   - Improve README files

4. **Code Contributions**
   - Fix bugs
   - Add new exercises
   - Improve utilities and helper functions
   - Add tests

5. **Content Contributions**
   - Create new Jupyter notebooks
   - Write exercise solutions
   - Add learning resources

## Development Workflow

### 1. Create an Issue

Before starting work:

1. Check if issue already exists
2. Create new issue describing:
   - What you want to do
   - Why it's needed
   - How you plan to implement it
3. Wait for maintainer feedback

### 2. Create a Branch

```bash
# Get latest code
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

Branch naming convention:
- `feature/` - New features or enhancements
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `test/` - Test additions or changes
- `refactor/` - Code refactoring

### 3. Make Changes

- Write clean, documented code
- Follow style guidelines
- Add tests for new functionality
- Update documentation

### 4. Commit Changes

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "feat: add new embedding exercise"
```

Commit message format:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Test changes
- `refactor:` - Code refactoring
- `chore:` - Maintenance tasks

### 5. Push and Create PR

```bash
# Push to your fork
git push origin feature/your-feature-name
```

Then create Pull Request on GitHub.

## Style Guidelines

### Python Code

Follow PEP 8 with these tools:

```bash
# Format code
black .

# Lint code
ruff check .

# Type checking
mypy utils/
```

**Key points:**
- Use type hints
- Write docstrings for functions/classes
- Keep functions focused and small
- Use meaningful variable names
- Add comments for complex logic

**Example:**

```python
def calculate_cost(
    prompt_tokens: int,
    completion_tokens: int,
    model: str = "gpt-3.5-turbo"
) -> float:
    """
    Calculate the cost of an API call.
    
    Args:
        prompt_tokens: Number of tokens in the prompt
        completion_tokens: Number of tokens in the completion
        model: The model name
    
    Returns:
        Cost in USD
    
    Example:
        >>> calculate_cost(100, 50, "gpt-3.5-turbo")
        0.000225
    """
    # Implementation here
    pass
```

### Jupyter Notebooks

- Clear markdown cells with explanations
- One concept per cell when possible
- Include outputs for reference
- Add comments in code cells
- Restart kernel and run all cells before committing

### Documentation

- Use clear, concise language
- Include code examples
- Add links to resources
- Keep formatting consistent
- Use proper markdown syntax

### Git Commits

- Write clear, descriptive messages
- Use conventional commit format
- Reference issues: `fixes #123`
- Keep commits focused and atomic

## Testing

### Writing Tests

Place tests in appropriate `tests/` directory:

```
module-name/
├── tests/
│   ├── test_feature.py
│   └── test_utils.py
```

**Test structure:**

```python
import pytest
from module import function_to_test


def test_function_basic():
    """Test basic functionality."""
    result = function_to_test(input_value)
    assert result == expected_value


def test_function_edge_case():
    """Test edge case."""
    with pytest.raises(ValueError):
        function_to_test(invalid_input)


@pytest.mark.asyncio
async def test_async_function():
    """Test async functionality."""
    result = await async_function()
    assert result is not None
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_feature.py

# Run with coverage
pytest --cov=utils --cov-report=term

# Run with verbose output
pytest -v

# Run specific test
pytest tests/test_feature.py::test_function_basic
```

### Test Requirements

- All new code must have tests
- Tests must pass before merging
- Aim for >80% code coverage
- Include edge cases and error handling

## Pull Request Process

### Before Submitting

**Checklist:**

- [ ] Code follows style guidelines
- [ ] All tests pass locally
- [ ] Added tests for new functionality
- [ ] Updated documentation
- [ ] Ran linting and formatting tools
- [ ] Committed with descriptive messages
- [ ] Rebased on latest main branch

```bash
# Final checks
black .
ruff check .
pytest
python validate_env.py
```

### Creating the PR

1. **Title**: Clear, descriptive summary
   - Good: `feat: add RAG evaluation metrics exercise`
   - Bad: `update stuff`

2. **Description**: Include:
   - What changes were made
   - Why changes were needed
   - How to test changes
   - Related issues (fixes #123)
   - Screenshots (if UI changes)

3. **Labels**: Add appropriate labels
   - enhancement, bug, documentation, etc.

**PR Template:**

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring

## Changes Made
- Added X
- Fixed Y
- Updated Z

## Testing
How to test these changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No breaking changes

## Related Issues
Closes #123
```

### Review Process

1. **Automated Checks**: CI/CD must pass
2. **Code Review**: Maintainer reviews code
3. **Feedback**: Address review comments
4. **Approval**: Maintainer approves
5. **Merge**: Maintainer merges PR

**Addressing Feedback:**

```bash
# Make changes based on feedback
git add .
git commit -m "refactor: address review comments"
git push origin feature-branch
```

### After Merge

1. **Delete branch**:
   ```bash
   git branch -d feature-branch
   git push origin --delete feature-branch
   ```

2. **Update local main**:
   ```bash
   git checkout main
   git pull upstream main
   ```

## Content Guidelines

### Creating Exercises

Good exercises should:

1. **Have clear learning objectives**
2. **Build on previous knowledge**
3. **Include starter code**
4. **Have automated tests**
5. **Include solutions with explanations**
6. **Estimate time to complete**
7. **Display cost estimates**

**Exercise Structure:**

```python
"""
Exercise: [Name]

Learning Objectives:
- Objective 1
- Objective 2

Prerequisites:
- Concept A
- Concept B

Estimated Time: 30 minutes
Estimated Cost: $0.05

Instructions:
1. Step 1
2. Step 2
...
"""

# Starter code here
def exercise_function():
    # TODO: Implement this
    pass


# Tests
def test_exercise():
    assert exercise_function() == expected_output
```

### Creating Notebooks

Good notebooks should:

1. **Start with overview and objectives**
2. **Progress from simple to complex**
3. **Include explanations between code cells**
4. **Show outputs**
5. **End with summary and next steps**

### Documentation Style

- **Be clear and concise**
- **Use examples**
- **Include links to resources**
- **Update table of contents**
- **Check spelling and grammar**

## Questions?

- **GitHub Discussions**: For general questions
- **GitHub Issues**: For bug reports and feature requests
- **Email**: [maintainer email if applicable]

## Recognition

Contributors will be recognized in:
- README Contributors section
- Release notes
- Special thanks in documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to AI Engineer Learning Repository!**

Last Updated: 2026-02-10
