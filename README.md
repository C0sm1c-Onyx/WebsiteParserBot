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

В .env файле прописать POSTGRES_HOST=localhost

2. 
```bash
cd WebsiteParserBot
```
```bash
docker-compose build
```
```bash
docker-compose up
```

В .env файле прописать POSTGRES_HOST=postgres

### тг бот - [t.me/website_parse_bot](t.me/website_parse_bot)
