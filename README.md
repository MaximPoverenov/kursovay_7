Это бэкенд-часть для трекера полезных привычек, реализованного с использованием Django и Django REST Framework (DRF). Проект создан как часть курсовой работы по разработке SPA веб-приложения для отслеживания привычек.
Установка

Клонируйте репозиторий:

git clone https://github.com/ваш_аккаунт/habit_tracker.git

Установите зависимости с помощью Poetry: poetry install

Создайте файл .env для переменных окружения см. файл .env.sample

Выполните миграции базы данных: poetry run python manage.py migrate

Создайте суперпользователя: poetry run python manage.py createsuperuser

Запуск проекта

Запустите сервер разработки Django: poetry run python manage.py runserver

Запустите Celery для выполнения отложенных задач: poetry run celery -A config worker --loglevel=INFO

Запустите Celery Beat для периодических задач: poetry run celery -A config beat --loglevel=INFO

Тестирование Проект покрыт тестами. Для запуска тестов выполните команду: poetry run python manage.py test

Также в проекте настроена проверка покрытия тестами с использованием coverage. Для запуска покрытия тестов выполните: poetry run coverage run --source='.' manage.py test poetry run coverage report