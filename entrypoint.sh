#!/bin/sh

set -e
#Wait Postgresql
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

#Collect static and make migrations
python3 manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

#Create super user
if [ "$DJANGO_SUPERUSER_EMAIL" ]
then
    python manage.py createsuperuser \
        --noinput \
        --email $DJANGO_SUPERUSER_EMAIL
fi
#Load DUMP file
DUMP_FILE="fixtures.json"

if test -f "$DUMP_FILE"; then
    echo "Load data"
    python3 manage.py loaddata fixtures.json
fi

#RUN Gunicorn
gunicorn --bind 0.0.0.0:8000 api_yamdb.wsgi

exec "$@"
