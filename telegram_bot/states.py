from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    waiting_for_file = State()