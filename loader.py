from  aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from date.config import BOT_TOKEN
from utils.db.storage import DatebaseManager

from date import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemotyStorage()
dp = Dispatcher(bot, storage=storage)
db = DatebaseManager('date/database.db')