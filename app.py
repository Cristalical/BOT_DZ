from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio
from loader import dp, bot
# from handlers.user.menu import admin_menu, user_menu
user_message = "Челик"
admin_message = "БОГ!"

def main_kb(user_telegram_id: int):
    kb_list = [
        [KeyboardButton(text="я как"), KeyboardButton(text="носок -")],
        [KeyboardButton(text="одинок,"), KeyboardButton(text="но не")],
        [KeyboardButton(text="дырявый")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list)
    return keyboard

@dp.message(Command("start", "s"))
async def cmd_start(message: types.Message):
    await message.answer('''Даров! 👋
    🤖 Это бот создан для работы с домашним заданием.
    Чтобы перейти в меню, напиши команду /menu.
    Если есть вопросы или предложения, то напиши команду
    /sos и свяжись с админами.''', reply_markup=main_kb(message.from_user.id))#, reply_markup=markup)

    # markup.row(user_menu, admin_menu)
# async def on_startup(dp):
#     basicConfig(level=INFO)
#     db.create_tables()

@dp.message(Command("menu"))
async def cmd_start(message: types.Message):

    await message.answer('''hule tut tak malo''')

@dp.message(Command("sos"))
async def cmd_start(message: types.Message):

    await message.answer('''/нам нужна помощь здесь она пиздец 
    /s e x пррыгай на мой шест пройди этот тест''')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())