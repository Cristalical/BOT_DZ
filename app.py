from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.filters import Command
import asyncio
from loader import dp, bot

user_message = "Челик"
admin_message = "БОГ!"

@dp.message(Command("start"))
async def cmd_start(message: types.Message):

    await message.answer('''Даров! 👋
    🤖 Это бот создан для работы с домашним заданием.
    Чтобы перейти в меню, напиши команду /menu.
    Если есть вопросы или предложения, то напиши команду
    /sos и свяжись с админами.''')


# async def on_startup(dp):
#     basicConfig(level=INFO)
#     db.create_tables()
@dp.message(Command("menu"))
async def cmd_start(message: types.Message):

    await message.answer('''tut budet menu ya tebe otvechayu''')

@dp.message(Command("sos"))
async def cmd_start(message: types.Message):

    await message.answer('''s o s нам нужна помощь здесь она пиздец s e x пррыгай на мой шест пройди этот тест''')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())