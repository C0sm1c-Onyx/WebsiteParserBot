import os
import pandas as pd
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from telegram_bot.keyboards import main_kb
from telegram_bot.states import Form
from telegram_bot.bot import bot
from parsing.url_parsers import website_parsing_by_xpath
from parsing.database import save_data_on_db


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        '''Привет! 👋\n\nЯ ваш помощник по парсингу сайтов. 📊✨\n\nС помощью меня вы сможете легко извлекать цену товара с различных веб-страниц с сохранением в базу данных. Чтобы начать, просто загрузите ваш Excel файл со столбцами title, url, xpath, и я помогу вам получить цену товара со средней стоимостью в зависимости от прайсов указанных на сайтах, ссылки на которые вы оставили в файле.\n\nДавайте начнем! 🚀''',
        reply_markup=main_kb
    )


@router.message(F.text == 'Загрузить exel файл')
async def wait_for_file(message: Message, state: FSMContext):
    await message.answer("Пожалуйста, прикрепите ваш Excel файл.")
    await state.set_state(Form.waiting_for_file)


@router.message(Form.waiting_for_file)
async def parse_file(message: Message):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)

    file_path = os.path.join(
        os.path.dirname(os.path.abspath(os.path.dirname(__file__))),
        "data/exel_files",
        message.document.file_name
    )

    await bot.download_file(file.file_path, file_path)
    await message.answer("Файл успешно сохранен! Произвожу парсинг данных с сайта.")

    data = pd.read_excel(file_path)
    df = pd.DataFrame(data, columns=['title', 'url', 'xpath'])

    total_cost, i, fail, answer_text = 0, 0, 0, ""
    for title, url, xpath in zip(df["title"], df["url"], df["xpath"]):
        print(title, url, xpath, i)
        parsed_data = await website_parsing_by_xpath(url, xpath)

        total_cost += float(parsed_data) if parsed_data else 0

        if parsed_data is None:
            parsed_data = 'Не удалось распарсить цену'
            fail += 1

        answer_text += f'{i+1}. Название - {title}\nСсылка - {url}\nXPATH - {xpath}\nЦена - {parsed_data}\n\n'
        i += 1

        await save_data_on_db(title, url, xpath, parsed_data)

    try:
        await message.answer(
            f"{answer_text}Средняя стоимость товара: {round(total_cost/(i - fail), 2)}"
        )
    except ZeroDivisionError:
        await message.answer(
            answer_text
        )