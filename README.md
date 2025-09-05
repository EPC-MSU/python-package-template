# python-package-template

This is a simple python package project template. It includes
* Flake8 code style rules, controlled with Linter
* Github actions CI tools
* Unit tests with a single example (add your new tests there)
* Preconfigured gitignore file for usual python environments
* pyproject.toml optional-dependencies for development tools
* TOX to test over different python versions
* pyproject.toml as the package description file for package build

Python packages on github.com/EPC-MSU must be build using this template as it is nonbinding at first stages of development and lays the way for more advanced approach on the next steps.

## Usage instructions

Note: instructions are for Linux/Mac. If you are using the Windows then change all ```python3``` commands to ```python```.

Run the software (from the root dir):
```bash
python3 -m hello_world
```
Run tests (from the root dir):
```bash
python3 -m unittest discover tests
```
Build wheel package (from the root dir):
```bash
python3 -m build --wheel
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
hello_world.say_hello()
```

Don't forget to update information in pyproject.toml to match your future project, based on this template: project name, version, dependencies, optional-dependencies for development tools, compatible python versions, etc.

Template was created due to https://ximc.ru/issues/44427
