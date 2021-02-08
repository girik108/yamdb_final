![Yamdb-app_workflow](https://github.com/girik108/yamdb_final/workflows/.github/workflows/yamdb.yaml/badge.sv)

# API_YamDB

REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке.

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Произведению может быть присвоен жанр. Новые жанры может создавать только администратор.
Читатели оставляют к произведениям текстовые отзывы и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти).
Из множества оценок автоматически высчитывается средняя оценка произведения.

Аутентификация по JWT-токену

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON

Cоздан в команде из трёх человек с использованим Git в рамках учебного курса Яндекс.Практикум.

## Стек технологий
- проект написан на Python с использованием Django REST Framework
- библиотека Simple JWT - работа с JWT-токеном
- библиотека django-filter - фильтрация запросов
- база данных PostgreSQL
- автоматическое развертывание проекта - Docker, docker-compose
- система управления версиями - git

## Как запустить проект, используя Docker (база данных PostgreSQL):
1) Клонируйте репозитроий с проектом:
```
git clone https://github.com/girik108/infra_sp2.git
```
2) В директории проекта создайте файл .env.db, в котором пропишите следующие переменные окружения :
 - POSTGRES_PASSWORD=DBpassword
 - SQL_ENGINE=django.db.backends.postgresql
 - SQL_DATABASE=yamdb
 - SQL_USER=yamdb_user
 - SQL_PASSWORD=YAMDBpassword
 - SQL_HOST=db
 - SQL_PORT=5432
 
3) С помощью Dockerfile и docker-compose.yaml разверните проект:
```
docker-compose up --build
```
4) В новом окне терминала узнайте id контейнера yamdb_web и войдите в контейнер:
```
docker container ls
```
```
docker exec -it <CONTAINER_ID> bash
```
5) В контейнере выполните миграции, создайте суперпользователя и заполните базу начальными данными:
```
python manage.py migrate

python manage.py createsuperuser

python manage.py loaddata fixtures.json
```
_________________________________
Ваш проект запустился на http://0.0.0.0:8000/

Полная документация доступна по адресу http://0.0.0.0:8000/redoc/

Вы можете запустить тесты и проверить работу модулей:
```
docker exec -ti <container_id> pytest
```

## Алгоритм регистрации пользователей
- Пользователь отправляет запрос с параметрами *email* и *username* на */auth/email/*.
- YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес *email* .
- Пользователь отправляет запрос с параметрами *email* и *confirmation_code* на */auth/token/*, в ответе на запрос ему приходит token (JWT-токен).

## Ресурсы API YaMDb

- Ресурс AUTH: аутентификация.
- Ресурс USERS: пользователи.
- Ресурс TITLES: произведения, к которым пишут отзывы (определённый фильм, книга или песня).
- Ресурс CATEGORIES: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- Ресурс GENRES: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- Ресурс REVIEWS: отзывы на произведения. Отзыв привязан к определённому произведению.
- Ресурс COMMENTS: комментарии к отзывам. Комментарий привязан к определённому отзыву.
______________________________________________________________________
### Пример http-запроса (POST) для создания нового комментария к отзыву:
```
url = 'http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/'
data = {'text': 'Your comment'}
headers = {'Authorization': 'Bearer your_token'}
request = requests.post(url, data=data, headers=headers)
```
### Ответ API_YamDB:
```
Статус- код 200

{
 "id": 0,
 "text": "string",
 "author": "string",
 "pub_date": "2021-01-25T15:45:00Z"
}
```
## Автор

**Гиматов Ирек**

* [github.com/girik108](https://github.com/girik108)
* [email](mailto:gimatovig@yandex.ru)
