# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python package template project (`hello_world`) that serves as a standard template for creating new Python packages. The project follows a simple structure for a basic Python package with versioning, testing, linting, and Github CI.

This project uses tools:
* bump2version to synchronize version across different files
* tox to test across different python versions
* pyproject.toml for package information
* unittesting for tests

## Common Commands

### Running the Project
```bash
python3 -m hello_world
```

### Testing
```bash
# Run all tests using unittest
python3 -m unittest discover tests

# Testing using tox
tox
```

### Linting
```bash
# Create virtual environment and install dev dependencies
python3 -m venv venv && source venv/bin/activate && pip install -e .[dev]

# Run flake8 linter
python3 -m flake8 .
```

### Building
```bash
# Build wheel package
python3 -m build --wheel
```

### Releasing and versioning
```bash
# Create virtual environment and install dev dependencies
python3 -m venv venv && source venv/bin/activate && pip install -e .[dev]

# Bump version automatically (creates commit and tag)
bump2version patch   # for bug fixes
bump2version minor   # for new features
bump2version major   # for breaking changes

python3 -m build --wheel
# git tags in semver format are considered package releases
```

### Releases automated publishing
```bash
# The release publishing is automated via GitHub Actions:
# 1. Make a local release with a new version
# 2. Push the changes with 'git push'
# 3. GitHub Actions automatically:
#    - Builds wheel and source distributions
#    - Creates GitHub release
#    - Attaches build artifacts
#    - Generates release notes
```

## Project Structure

- `hello_world/` - Main package directory
  - `__init__.py` - Package initialization, exports `say_hello` function
  - `hello.py` - Core module with `say_hello()` function
  - `__main__.py` - Module entry point for `python -m` execution
- `tests/` - Unit tests using Python's unittest framework
- `pyproject.toml` - Modern package configuration and dependencies
- `.flake8` - Flake8 linting configuration (max line length: 120, complexity: 14)
- `tox.ini` - Tox configuration for testing across Python versions
- `.github/workflows/` - CI/CD workflows for testing, linting, releasing

## Key Configuration

- **Python Version**: Requires Python 3.8+
- **Flake8 Settings**: Max line length 120, max complexity 14, double quotes preferred
- **Test Framework**: Standard Python unittest
- **CI/CD**: GitHub Actions for automated testing, linting and release publishing on main and dev-** branches

## Architecture Notes

Follow the project structure to place new code, tests, rules, documentation.

## Workflow rules for Claude and other AI agents

After making changes to the code you should run tests and run linter. Then check for errors and fix issues until your task does not produce errors.