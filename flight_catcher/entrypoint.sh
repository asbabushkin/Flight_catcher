#! /bin/bash

python manage.py makemigrations --no-input
python manage.py migrate --no-input

python manage.py collectstatic --no-input

#python manage.py runserver 127.0.0.1:8000
exec gunicorn flight_catcher.wsgi:application -b 0.0.0.0:8000 --reload