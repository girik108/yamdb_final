# pull official base image
FROM python:3.8 AS builder
RUN apt-get update && apt-get install -y netcat

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


FROM builder AS python_yamdb

RUN adduser --disabled-password worker
USER worker
WORKDIR /home/worker
#Create STATIC dir. Without it Permission denied
RUN mkdir static

# copy project
COPY --chown=worker:worker . .

# run app
#CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000 
ENTRYPOINT ["/home/worker/entrypoint.sh"]