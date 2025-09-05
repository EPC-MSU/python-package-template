# python-package-template

Простой пример-шаблон проекта python-пакета с проверкой стилей, тестами и разными стандартными файлами\папками  
Все новые python-пакеты на github.com/EPC-MSU нужно создавать из этого шаблона

Запустить этот проект (из корня):
```bash
python3 -m hello_world
```
Запустить тесты (из корня):
```bash
python3 -m unittest discover tests
```
Установить этот проект (из корня):
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
После установки им можно пользоваться:
```python
import hello_world
hello_world.say_hello()
```

Пишите unit-тесты к своим пакетам в tests/

Не забудьте актуализировать информацию о пакете в pyproject.toml: имя проекта, версия, зависимости и пр.

Создан в рамках https://ximc.ru/issues/44427
