from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

UZBEK = "🇺🇿 O'zbekcha"
RUSSIAN = '🇷🇺 Ruscha'
ENGLISH = '🏴󠁧󠁢󠁥󠁮󠁧󠁿 English'


def language_button():
    keyboard = InlineKeyboardMarkup(row_width=2)
    UZBEK_BUTTON = InlineKeyboardButton(text=UZBEK, callback_data='uzbek')
    RUSSIAN_BUTTON = InlineKeyboardButton(text=RUSSIAN, callback_data='russian')
    ENGLISH_BUTTON = InlineKeyboardButton(text=ENGLISH, callback_data='english')
    keyboard.add(UZBEK_BUTTON, RUSSIAN_BUTTON, ENGLISH_BUTTON)
    return keyboard
