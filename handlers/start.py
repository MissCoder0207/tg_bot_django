from aiogram import types

from buttons.markup import force_register_button
from dispatch import dp
from states import RegisterState


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    text_body = "Assalomu Alaykum bizning botga xush kelibsiz"
    await RegisterState.begin.set()
    await message.answer(text=text_body, reply_markup=force_register_button())
