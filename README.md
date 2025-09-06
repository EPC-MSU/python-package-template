# python-package-template

This is a simple python package project template. It includes
* **Flake8** code style rules
* **Semver** tag versioning with **bump2version**
* Support of get_version() to display the current version
* Unit tests with a single example (add your new tests there)
* main/dev branches workflow in CI
* Crossplatform testing meaning Win/Lin/Mac
* **TOX** to test over different python versions
* **pyproject.toml** as the package description file for package build
* Preconfigured **.gitignore** file for usual python environments
* Github actions CI tools
    * Run linter on main and dev branches
    * Run integrated tests on main and dev branches


Python packages on github.com/EPC-MSU must be build using this template as it is not very binding at first stages of development and lays the way for more advanced approaches on the next steps.

## Usage instructions

Note: instructions are for Linux/Mac. If you are using the Windows then change all ```python3``` commands to ```python```.

Run the python package (from the root dir):
```bash
python3 -m hello_world
```
Run tests (from the root dir):
```bash
python3 -m unittest discover tests
```
### Building and releasing

Build wheel package (from the root dir):
```bash
python3 -m build --wheel
```
Bump project version (requires venv since PEP 668):
```bash
# Create virtual environment and install dev dependencies
python3 -m venv venv && source venv/bin/activate && pip install -e .[dev]

# Bump version (patch: 0.0.1 → 0.0.2, minor: 0.0.1 → 0.1.0, major: 0.0.1 → 1.0.0)
bump2version patch   # for bug fixes
bump2version minor   # for new features  
bump2version major   # for breaking changes
```
Install this package (requires venv since PEP 668, run from the root dir):
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the package with development dependencies (editable)
pip install -e .[dev]

# Or install the package only
pip install .
```
After the installation you can use the package in python's venv:
```python
import hello_world

# Use the main function
hello_world.say_hello()

# Get package version
version = hello_world.get_version()
print(f"Package version: {version}")
```

Don't forget to update information in pyproject.toml to match your future project, based on this template: project name, version, dependencies, optional-dependencies for development tools, compatible python versions, etc.

Template was created due to https://ximc.ru/issues/44427
