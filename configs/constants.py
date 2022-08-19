from environs import Env
from os.path import join as path_join
from pathlib import Path

BASE_URL = Path(__file__).parent.parent
env = Env()
env.read_env()
BOT_TOKEN = env.str('BOT_TOKEN')
STORAGE_PATH = path_join(BASE_URL, 'configs', 'mystate.json')
DB_PATH = path_join(BASE_URL, 'db', 'db.sqlite')
