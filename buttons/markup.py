from typing import List

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

REGISTER = "® Register"

REGISTER_BUTTON_TEXT = KeyboardButton(text=REGISTER)
PHONE_NUMBER = "📱 Telefon"
PHONE_NUMBER_BUTTON_TEXT = KeyboardButton(text=PHONE_NUMBER, request_contact=True)

LOCATION_USER = "📍 Lokatsiya"
LOCATION_USER_BUTTON_TEXT = KeyboardButton(text=LOCATION_USER, request_location=True)

def location_user():
    row2 = [LOCATION_USER_BUTTON_TEXT]
    key = [row2]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=key)

def phone_number():
    row1 = [PHONE_NUMBER_BUTTON_TEXT]
    keyboard = [row1]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


def force_register_button():
    row1: List = [REGISTER_BUTTON_TEXT]
    keyboard = [row1]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)
