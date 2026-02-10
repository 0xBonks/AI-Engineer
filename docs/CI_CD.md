# CI/CD Pipeline Documentation

## Overview

This repository uses GitHub Actions for continuous integration and deployment. The CI/CD pipeline ensures code quality, security, and reliability through automated testing and checks.

## Workflows

### 1. CI - Tests and Quality Checks (`.github/workflows/ci.yml`)

**Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

**Jobs:**

#### Test Job
- **Purpose**: Run automated tests across multiple Python versions
- **Python Versions**: 3.11, 3.12
- **Steps**:
  1. Checkout code
  2. Set up Python environment with caching
  3. Install dependencies
  4. Run environment validation
  5. Run pytest with coverage
  6. Upload coverage to Codecov

#### Quality Job
- **Purpose**: Enforce code quality standards
- **Checks**:
  - **Black**: Code formatting
  - **Ruff**: Fast Python linting
  - **Mypy**: Static type checking

#### Security Job
- **Purpose**: Scan for security vulnerabilities
- **Tools**:
  - **pip-audit**: Check for known vulnerabilities in dependencies
  - **Bandit**: Security linter for Python code

#### Docker Job
- **Purpose**: Verify Docker image builds correctly
- **Steps**:
  1. Build Docker image with caching
  2. Test image runs Python correctly

### 2. Dependency Security Check (`.github/workflows/dependency-check.yml`)

**Triggers:**
- Weekly schedule (Mondays at 9am UTC)
- Manual workflow dispatch
- Changes to requirements files

**Jobs:**

#### Security Scan Job
- **Purpose**: Regular security audits of dependencies
- **Steps**:
  1. Run pip-audit for vulnerability scanning
  2. Run Safety check for security advisories
  3. Generate security reports (JSON format)
  4. Upload reports as artifacts
  5. Create GitHub issue if vulnerabilities found

#### Check Outdated Job
- **Purpose**: Monitor for outdated dependencies
- **Steps**:
  1. List outdated packages
  2. Generate update report
  3. Upload report as artifact

## Secrets Required

Configure these secrets in your GitHub repository settings:

| Secret Name | Required | Purpose |
|-------------|----------|---------|
| `OPENAI_API_KEY` | No | For API connectivity tests (optional) |

**Note**: Most CI checks don't require API keys. The validation script will skip API tests if keys are not provided.

## Branch Protection Rules

### Recommended Settings for `main` Branch

1. **Require pull request reviews**
   - Required approving reviews: 1
   - Dismiss stale reviews: Yes

2. **Require status checks to pass**
   - Required checks:
     - `test (Python 3.11)`
     - `test (Python 3.12)`
     - `quality`
     - `security`
     - `docker`

3. **Require branches to be up to date**
   - Yes (ensures changes are tested against latest code)

4. **Require signed commits** (optional but recommended)

5. **Include administrators** in restrictions

### Setup Instructions

1. Go to Repository Settings → Branches
2. Add branch protection rule for `main`
3. Enable settings above
4. Save changes

## Running Checks Locally

Before pushing code, run checks locally to catch issues early:

### All Quality Checks

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Format code
black .

# Lint code
ruff check .

# Type check
mypy utils/

# Run tests
pytest --cov=utils

# Security scan
pip-audit
bandit -r utils/ -ll
```

### Pre-commit Hooks

Automate local checks with pre-commit:

```bash
# Install pre-commit
pip install pre-commit

# Set up hooks
pre-commit install

# Run manually on all files
pre-commit run --all-files
```

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.1.1
    hooks:
      - id: black
  
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.15
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
  
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]
  
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.6
    hooks:
      - id: bandit
        args: [-ll]
```

## Workflow Artifacts

### Generated Artifacts

Each workflow run may produce artifacts:

1. **Coverage Reports** (CI workflow)
   - `coverage.xml` - Coverage data for Codecov
   - Viewable in pull request checks

2. **Security Reports** (Dependency Check workflow)
   - `pip-audit-report.json` - Vulnerability scan results
   - `safety-report.json` - Safety check results
   - Download from Actions tab → Workflow run → Artifacts

3. **Outdated Dependencies Report** (Dependency Check workflow)
   - `outdated-report.md` - List of packages with updates available

### Accessing Artifacts

1. Go to Actions tab in GitHub
2. Click on a workflow run
3. Scroll down to "Artifacts" section
4. Download artifact zip file

## Monitoring and Notifications

### CI/CD Status

View status in multiple locations:

1. **Pull Requests**: Check run summaries appear inline
2. **Commits**: Status badges show pass/fail
3. **Actions Tab**: Full workflow history and logs

### Notifications

Configure notifications in GitHub Settings → Notifications:

- **Workflow runs**: Get notified on failure
- **Pull requests**: Get notified on check status changes

### Email Notifications

By default, you'll receive emails for:
- Workflow failures on your commits
- Pull request check completions

## Troubleshooting

### Common CI Failures

#### Test Failures

**Problem**: Tests pass locally but fail in CI

**Solutions**:
1. Check Python version differences
2. Verify all dependencies in requirements.txt
3. Check for environment-specific issues
4. Review test logs in Actions tab

#### Formatting Failures

**Problem**: Black formatting check fails

**Solution**:
```bash
# Format code locally
black .

# Commit changes
git add .
git commit -m "style: apply black formatting"
git push
```

#### Linting Failures

**Problem**: Ruff linting check fails

**Solution**:
```bash
# Check issues
ruff check .

# Auto-fix what's possible
ruff check --fix .

# Review and fix remaining issues
# Commit changes
```

#### Security Scan Failures

**Problem**: pip-audit or Bandit finds issues

**Solutions**:

1. **For dependency vulnerabilities**:
   ```bash
   # Identify vulnerable packages
   pip-audit
   
   # Update affected packages
   pip install --upgrade package-name
   
   # Update requirements.txt
   pip freeze > requirements.txt
   ```

2. **For code security issues**:
   ```bash
   # Review Bandit report
   bandit -r utils/ -ll
   
   # Fix issues in code
   # Add # nosec comment if false positive
   ```

#### Docker Build Failures

**Problem**: Docker image fails to build

**Solutions**:
1. Test build locally:
   ```bash
   docker build -t test .
   ```
2. Check Dockerfile syntax
3. Verify base image availability
4. Review build logs in Actions

### Slow CI Runs

**Problem**: CI takes too long to run

**Solutions**:

1. **Enable dependency caching** (already configured)
2. **Parallelize tests**:
   ```bash
   pytest -n auto  # Requires pytest-xdist
   ```
3. **Skip optional checks** on drafts:
   ```yaml
   if: github.event.pull_request.draft == false
   ```

### Cache Issues

**Problem**: Stale cache causing issues

**Solution**:
1. Go to Actions → Caches
2. Delete caches manually
3. Rerun workflow

## Best Practices

1. **Run checks locally** before pushing
2. **Keep dependencies updated** (monthly reviews)
3. **Fix CI failures immediately** (don't merge broken PRs)
4. **Review security scan results** weekly
5. **Monitor workflow run times** for degradation
6. **Use draft PRs** for work in progress
7. **Write descriptive commit messages** for better CI logs

## Customization

### Adding New Checks

To add a new check to CI:

1. Edit `.github/workflows/ci.yml`
2. Add new step or job
3. Test in a branch
4. Update this documentation

Example:
```yaml
- name: Run custom check
  run: |
    python scripts/custom_check.py
```

### Adjusting Frequency

To change dependency check schedule:

1. Edit `.github/workflows/dependency-check.yml`
2. Modify cron expression:
   ```yaml
   schedule:
     - cron: '0 9 * * 1'  # Every Monday at 9am
   ```

Cron syntax: `minute hour day month weekday`

### Disabling Workflows

To temporarily disable a workflow:

1. Go to Actions tab
2. Click on workflow name
3. Click "..." menu
4. Select "Disable workflow"

## Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [pytest Documentation](https://docs.pytest.org/)
- [Black Documentation](https://black.readthedocs.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [pip-audit Documentation](https://github.com/pypa/pip-audit)

---

**Last Updated**: 2026-02-10  
**Maintained by**: Repository maintainers
