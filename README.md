# python-package-template

This is a simple python package project template. It includes
* Flake8 code style rules, controlled with Linter.
* Github actions CI tools
* Unit tests with a single example (add your new tests there)
* Preconfigured gitignore file for usual python environments
* requirements.ini to store the package names we depend on
* TOX to test over different python versions
* pyproject.toml as the package description file for package build

Python packages on github.com/EPC-MSU must be build using this template as it is nonbinding at first stages of development and lays the way for more advanced approach on the next steps.

## Usage instructions

Run the software (from the root dir):
```bash
python3 -m hello_world
```
Run tests (from the root dir):
```bash
python3 -m unittest discover tests
```
Install this package (from the root dir):
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -r requirements.txt

# Install the package
pip install .

# For development (editable install)
pip install -e .

# Alternative: Install with --user flag (not recommended for development)
pip install . --user
```
After the installation you can use the package in python:
```python
import hello_world
hello_world.say_hello()
```

Don't forget to update information in pyproject.toml to match your future project, based on this template: project name, version, dependencies, compatible python versions, etc.

Template was created due to https://ximc.ru/issues/44427
