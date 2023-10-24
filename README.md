ЗАПУСК:

Скрипты реализованы на языке программирования Python 3.9
Для работы скриптов в системе должен быть установлен Python 3 версии не ниже 3.9
Для запуска необходимо установить poetry:
curl -sSL https://install.python-poetry.org | python3 -
Добавить poetry в PATH.
Перейти в каталог проекта и выполнить:
poetry install
Для подробной информации смотрите документацию poetry по адресу https://python-poetry.org/docs/
Для запуска тестов из папки проекта в командной строке введите
poetry run python -m pytest
Если Вы запускаете с Mac OS, то команда:
poetry run python3 -m pytest