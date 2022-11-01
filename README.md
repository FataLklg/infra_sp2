### Проект API_YamDB.

YaMDb собирает отзывы (Review) пользователей на произведения (Titles) и выставляет средний бал на основе оценок. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором.

###### Проект написан на Python 3.7, БД - PostgreSQL(psycopg2-binary==2.8.6), разворачивается в Docker'e.
---

### Шаблон наполнения env-файла:

**SECRET_KEY**=<_секретный ключ_>

**DB_ENGINE**=<_БД, с которой работаем_>

**DB_NAME**=<_имя базы данных_>

**POSTGRES_USER**=<_логин для подключения к базе данных_>

**POSTGRES_PASSWORD**=<_пароль для подключения к БД_>

**DB_HOST**=<_название сервиса (контейнера)_>

**DB_PORT**=<_порт для подключения к БД_>

---

### Как запустить проект:

 Клонировать репозиторий и перейти в него в командной строке:
```python
git clone https://github.com/FataLklg/infra_sp2.git
```

Скачать и установить [Docker:](https://www.docker.com/products/docker-desktop "Docker-Desktop")

Перейти в каталог "_infra_":
```python
cd infra
```

Cобрать образ в Docker'е и запустить контейнеры:
```python
docker-compose up -d --build
```

Применить миграции:
```python
docker-compose exec web python manage.py migrate
```

Собрать статику:
```python
docker-compose exec web python manage.py collectstatic --no-input
```

##### Готово! Проект запущен и готов к работе по адресу: http://localhost/api/v1/

---

### Команды для заполнения базы данными:
```python
docker-compose cp fixtures.json web:/app                        # Копируем бэкап с данными БД в контейнер
docker-compose exec web python manage.py shell  
# выполнить в открывшемся терминале:
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()
docker-compose exec web python manage.py loaddata fixtures.json  # Импортируем данные из бэкапа в БД
```

---
### Список доступных адресов:

#### - Модуль AUTH:

Аутентификация пользователей реализована на основе JWT-токенов.

Регистрация нового пользователя POST `/auth/signup/`

Получение JWT-токена в обмен на username и confirmation code POST `/auth/token/`

#### - Модуль USERS:
Получение списка всех пользователей GET `/users/`

Добавление пользователя POST `/users/`

Получение пользователя по username GET `/users/{username}/`

Преобразование данных пользователя по username PATCH `/users/{username}/`

Удаление пользователя по username DELETE `/users/{username}/`

Получение данных своей учетной записи GET `/users/me/`

Преобразование данных своей учетной записи PATCH `/users/me/`

#### - Модуль CATEGORIES:
Получение списка всех категорий GET `/categories/`

Добавление новой категории POST `/categories/`

Удаление категории DELETE `/categories/{slug}/`

#### - Модуль GENRE:
Получение списка всех жанров GET `/genres/`

Добавление жанра POST `/genres/`

Удаление жанра DELETE `/genres/{slug}/`

#### - Модуль TITLES:
Получение списка всех произведений GET `/titles/`

Добавление произведения POST `/titles/`

Получение информации о произведении GET `/titles/{titles_id}/`

Частичное обновление информации о произведении PATCH `/titles/{titles_id}/`

Удаление произведения DELETE `/titles/{titles_id}/`

#### - Модуль REVIEWS:
Получение списка всех отзывов GET `/titles/{titles_id}/reviews/`

Добавление нового отзыва POST `/titles/{titles_id}/reviews/`

Получение отзыва по id GET `/titles/{titles_id}/reviews/{review_id}/`

Частичное обновление отзыва по id PATCH `/titles/{titles_id}/reviews/{review_id}/`

Удаление отзыва по id DELETE `/titles/{titles_id}/reviews/{review_id}/`

#### - Модуль COMMENTS:
Получение списка всех комментариев к отзыву GET `/titles/{titles_id}/reviews/{review_id}/comments/`

Добавление комментария к отзыву POST `/titles/{titles_id}/reviews/{review_id}/comments/`

Получение комментария к отзыву GET `/titles/{titles_id}/reviews/{review_id}/comments/{comment_id}/`

Частичное обновление комментария к отзыву PATCH `/titles/{titles_id}/reviews/{review_id}/comments/{comment_id}/`

Удаление комментария к отзыву DELETE `/titles/{titles_id}/reviews/{review_id}/comments/{comment_id}/`

---

### Авторы:

- ##### __Антон Жирков__
- ##### __Виктор Круглый__
- ##### __Антон Тарасов__
