from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from date.config import BOT_TOKEN
from utils.db.storage import DatebaseManager

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
# db = DatebaseManager('date/database.db')