
# Django Telegram Messenger

Это приложение на Django и DRF позволяет пользователям регистрироваться, авторизоваться и отправлять текстовые сообщения. 
Сообщения сохраняются в базе данных и отправляются в Telegram, если имя пользователя в приложении совпадает с именем пользователя в Telegram.

## Начало работы

1. Клонируйте репозиторий:
```
git clone https://github.com/dichenk/django-telegram-api
```

2. Установите необходимые зависимости:
```
pip install -r requirements.txt
```

3. Укажите токен вашего бота Telegram в файле `.env.development`:
```
TELEGRAM_TOKEN=YOUR_TOKEN_HERE
```

4. Запустите приложение:
```
python manage.py runserver
```

## Использование

### Регистрация:

Отправьте POST-запрос на `/user/register` с следующим форматом:

```json
{
    "username": "your_telegram_username",
    "password": "your_password"
}
```

**Примечание:** `username` должен совпадать с вашим именем пользователя в Telegram.

### Авторизация:

Отправьте POST-запрос на `/user/token`:

```json
{
    "username": "your_telegram_username",
    "password": "your_password"
}
```

В ответ вы получите токен. Добавьте его в заголовки запроса:

```
Authorization: Bearer YOUR_TOKEN
```

### Отправка сообщений:

Отправьте POST-запрос на `/messages/send` с текстом сообщения. Сообщение будет сохранено в базе данных и отправлено в Telegram.

### Получение сообщений:

Отправьте GET-запрос на `/messages/get`, чтобы получить все ваши сообщения.

## Вклад в проект

Если у вас есть предложения или вы нашли ошибку, создайте Issue или Pull Request.
