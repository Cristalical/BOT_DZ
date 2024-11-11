from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

from data.config import BOT_TOKEN
from utils.db.storage import DatabaseManager

# Создание всего
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
db = DatabaseManager()

# Словарь предметов, чтобы был нормальный вывод
less = {"odk": "ОДК",
        "org": "ОРГ",
        "init": "ИНИТ",
        "inf": "ИНФА",
        "math": "Матан",
        "ir": "ИР",
        "eng_kr": "Английский красавчиков",
        "eng_ym": "Английский умничек",
        "vvp": "Введение в профессию",
        "phys": "Физра"}