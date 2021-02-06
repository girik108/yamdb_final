FROM nginx:1.18

RUN apt-get update && apt-get install -y netcat

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY wait-for-web.sh wait-for-web.sh

RUN mkdir /var/yamdb/

