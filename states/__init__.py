from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    begin = State()
    name = State()
    surname = State()
    language = State()
    phone = State()
    location = State()
