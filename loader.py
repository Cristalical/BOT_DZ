from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

from data.config import BOT_TOKEN
from utils.db.storage import DatabaseManager

# '''Тут я сделал так, чтобы бот мог работать с html кодом'''
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
db = DatabaseManager()
