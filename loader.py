from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

from data.config import BOT_TOKEN
from utils.db.storage import DatebaseManager

# '''Тут я сделал так, чтобы бот мог работать с html кодом'''
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
db = DatebaseManager()
db.create_db()
db.create_table()
print(db.fetchall(f"SELECT deadline FROM all_homework WHERE lessons = \'init\'"))