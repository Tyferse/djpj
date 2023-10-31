#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


"""
django-admin startproject smuproj   создание проекта django в указанной директории
python manage.py startapp articles  создание приложение для проекта django в указанной директории

python manage,py runserver
запуск сервера (по умолчанию localhost (127.0.0.1:8000, но можно указать другой порт или IP))

python manage.py makemigrations articles
создаёт файл миграции базы данных models.py в папке migrations

python manage.py sqlmigrate articles 0001
возвращает sql код, который выполнится при выполнении миграции

python manage.py migrate    запускает миграцию базы данных

python manage.py shell
запускает интерактивную консоль для python и django кода

In [1]: from articles.models import Article, Comment

In [2]: Article.objects.all()
Out[2]: <QuerySet []>

In [3]: from django.utils import timezone

In [4]: a = Article(article_title="Почему ящеры проиграли войну древним русам?", article_text="Водицы Байкальской выпил
   ...: и и погнали.", pub=timezone.now())

In [5]: a.save()

In [6]: a.id
Out[6]: 1

In [7]: a.article_title
Out[7]: 'Почему ящеры проиграли войну древним русам?'

python manage.py createsuperuser    запускает процесс регистрации админов
"""


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smuproj.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you"
            " forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
