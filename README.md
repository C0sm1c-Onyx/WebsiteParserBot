# WebsiteParserBot


### Настройка окружения и запуск проекта

1. Клонируйте репозиторий:
```bash
git clone https://github.com/C0sm1c-Onyx/WebsiteParserBot.git
```

2. Отредактируйте три переменные в файле .env в корневой директории проекта:
```env
POSTGRES_DB_NAME=your_db_name
POSTGRES_USER_NAME=your_db_user
POSTGRES_PASSWORD=your_db_password
```

Запустить проект можно двумя способами:

1.
[!] В .env файле должно быть прописано POSTGRES_HOST=localhost
```bash
cd WebsiteParserBot
```
```bash
poetry install
```

```bash
poetry run alembic upgrade head
```
```bash
poetry run python run_bot.py
```


2. 
[!] В .env файле должно быть прописано POSTGRES_HOST=postgres
```bash
cd WebsiteParserBot
```
```bash
docker-compose build
```
```bash
docker-compose up
```

### тг бот - [t.me/website_parse_bot](t.me/website_parse_bot)
