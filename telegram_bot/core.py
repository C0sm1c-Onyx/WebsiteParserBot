import asyncio
from aiogram import Dispatcher

from telegram_bot.handlers import router
from telegram_bot.bot import bot


async def main():
    dp = Dispatcher(bot=bot)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())