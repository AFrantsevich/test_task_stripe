#!/bin/bash
if [ "$DEBUG"==True ]; then
    python manage.py makemigrations
    python manage.py migrate
    python manage.py load_data 15 3433 52321
    python manage.py create_superuser
    python manage.py collectstatic --no-input
fi

gunicorn stripe_test.wsgi:application --bind 0:8000