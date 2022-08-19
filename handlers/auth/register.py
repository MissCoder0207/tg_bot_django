from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from buttons.inline import language_button
from buttons.markup import phone_number, location_user
from dispatch import dp
from states import RegisterState


@dp.message_handler(state=RegisterState.begin)
async def name_handler(message: types.Message):
    text = "Iltimos ismingizni kiriting"
    await RegisterState.next()
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=RegisterState.name)
async def name_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    text = "Familya kiriting"
    await RegisterState.surname.set()
    await message.answer(text=text)


@dp.message_handler(state=RegisterState.surname)
async def surname_handlers(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    text = "Iltimos tilni tanlang"
    await message.answer(text=text, reply_markup=language_button())
    await RegisterState.language.set()


@dp.callback_query_handler(state=RegisterState.language)
async def language_button_handlers(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['language'] = query.data
    text = "Telefon nomerni kiriting"
    await RegisterState.phone.set()
    await query.bot.send_message(text=text, reply_markup=phone_number(), chat_id=query.message.chat.id)


@dp.message_handler(content_types=types.ContentType.CONTACT, state=RegisterState.phone)
async def phone_number_handlers(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = dict(message.contact)
        text = "Locatsiyani jo\'nating!"
        await RegisterState.location.set()
        await message.bot.send_message(text=text, reply_markup=location_user(), chat_id=message.chat.id)

@dp.message_handler(content_types=types.ContentType.LOCATION, state=RegisterState.location)
async def location_user_handlers(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['location'] = dict(message.location)

