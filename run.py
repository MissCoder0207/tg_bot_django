from aiogram.utils import executor
import handlers
from dispatch import dp

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
