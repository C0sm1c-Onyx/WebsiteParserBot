# WebsiteParserBot

## Запуск проекта

### Настройка окружения

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
poetry install

poetry run python run_bot.py
```

3. 
```bash
docker-compose build

docker-compose up
```

### Ссылка на тг бота t.me/website_parse_bot
