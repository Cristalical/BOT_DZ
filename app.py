from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio
from loader import dp, bot
# from handlers.user.menu import admin_menu, user_menu
user_message = "Челик"
admin_message = "БОГ!"

@dp.message(Command("start", "s"))
async def cmd_start(message: types.Message):
    await message.answer('''Даров! 👋
    🤖 Это бот создан для работы с домашним заданием.
    Чтобы перейти в меню, напиши команду /menu.
    Если есть вопросы или предложения, то напиши команду
    /sos и свяжись с админами.''')#, reply_markup=markup)

    # markup.row(user_menu, admin_menu)
# async def on_startup(dp):
#     basicConfig(level=INFO)
#     db.create_tables()
def main_kb(user_telegram_id: int):
    kb_list = [
        [KeyboardButton(text="ОРГ"), KeyboardButton(text="ОДК")],
        [KeyboardButton(text="ИНФА"), KeyboardButton(text="АНГЛ1")],
        [KeyboardButton(text="АНГЛ2"), KeyboardButton(text="ИР")],
        [KeyboardButton(text="МАТАН"), KeyboardButton(text="ИНИТ")],
        [KeyboardButton(text="ВВП"), KeyboardButton(text="ФИЗРА")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard

@dp.message(Command("menu"))
async def cmd_start(message: types.Message):

    await message.answer('''тут должны быть кнопки''', reply_markup=main_kb(message.from_user.id))

@dp.message(Command("sos"))
async def cmd_start(message: types.Message):

    await message.answer('''тут два айдишника кристаликал и невероятнейше''')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())