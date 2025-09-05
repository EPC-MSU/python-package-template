# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python package template project (`hello_world`) that serves as a standard template for creating new Python packages. The project is primarily in Russian and follows a simple structure for a basic Python package with testing and linting setup.

## Common Commands

### Running the Project
```bash
python -m hello_world
```

### Testing
```bash
# Run all tests using unittest
python -m unittest discover tests

# Using tox (supports py34, py36)
tox
```

### Linting
```bash
# Run flake8 linter
python -m flake8 .
```

### Installation
```bash
# Modern approach with pip (recommended)
pip install .

# For development (editable install)
pip install -e .

# Legacy approach (shows deprecation warnings)
python setup.py install
```

## Project Structure

- `hello_world/` - Main package directory
  - `__init__.py` - Package initialization, exports `say_hello` function
  - `hello.py` - Core module with `say_hello()` function
  - `__main__.py` - Module entry point for `python -m` execution
- `tests/` - Unit tests using Python's unittest framework
- `setup.py` - Package configuration and dependencies
- `.flake8` - Flake8 linting configuration (max line length: 120, complexity: 14)
- `tox.ini` - Tox configuration for testing across Python versions
- `.github/workflows/` - CI/CD workflows for testing and linting

## Key Configuration

- **Python Version**: Requires Python 3.6+
- **Flake8 Settings**: Max line length 120, max complexity 14, double quotes preferred
- **Test Framework**: Standard Python unittest
- **CI/CD**: GitHub Actions for automated testing and linting on main and dev-** branches

## Architecture Notes

This is a minimal Python package template with a single module (`hello_world.hello`) containing one function (`say_hello()`). The project follows standard Python packaging conventions and is designed as a starting template for new packages rather than a complex application.