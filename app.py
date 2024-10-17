from aiogram import types
from aiogram import F, Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
import asyncio
from loader import dp, bot
start_router = Router()

# from handlers.user.menu import admin_menu, user_menu
user_message = "Челик"
admin_message = "БОГ!"

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

def main_kb(user_telegram_id: int):
    kb_list = [
        [KeyboardButton(text="ОРГ"), KeyboardButton(text="ОДК")],
        [KeyboardButton(text="ИНФА,"), KeyboardButton(text="АНГЛ1")],
        [KeyboardButton(text="ИНИТ,"), KeyboardButton(text="АНГЛ2")],
        [KeyboardButton(text="МАТАН"), KeyboardButton(text="ВВП")],
        [KeyboardButton(text="ИР"), KeyboardButton(text="ФИЗРА")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard

def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="ОДК", url='https://habr.com/ru/users/yakvenalex/')],
        [InlineKeyboardButton(text="Мой Telegram", url='tg://resolve?domain=yakvenalexx')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

@dp.message(Command("menu"))
async def cmd_start(message: types.Message):

    await message.answer('''Выбери предмет, сучка)''', reply_markup=ease_link_kb())

@dp.message(Command("sos"))
async def cmd_start(message: types.Message):

    await message.answer('''Обращайтесь к ебейшему @cristalical
                            и его рабу @neveroyatneyshee!!!''')

async def main():
    await dp.start_polling(bot)

@dp.message(F.text == 'ОДК')
async def cmd_start(message: types.Message):
    await message.answer('''ТЫ ДАУН АХАХАХАХХА''', reply_markup=types.ReplyKeyboardRemove())



if __name__ == "__main__":
    asyncio.run(main())