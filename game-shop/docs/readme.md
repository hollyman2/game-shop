# Инструкция по конфигурированию проекта.
## Установка переменных окружения.
Файл с переменными .env можно скачать [здесь](https://disk.yandex.ru/d/XbhFPkqi64jjEA).
pipenv загрузит его автоматически.
## Запуск проекта.
Предполагается, что проект будет запускаться через терминал. Для этого нужно ввести.
~pipenv shell~
Для запуска сервера разработки:
~python manage.py runserver~
или
~pipenv run python manage.py runserver~