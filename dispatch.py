from aiogram import Bot, Dispatcher
from configs.constants import BOT_TOKEN, STORAGE_PATH
from aiogram.contrib.fsm_storage.files import JSONStorage

storage = JSONStorage(STORAGE_PATH)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
