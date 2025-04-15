import os
from aiogram import Bot
from dotenv import load_dotenv


load_dotenv()


bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))