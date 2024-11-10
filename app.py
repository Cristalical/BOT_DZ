from aiogram import F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio

from loader import dp, bot
import handlers.user.menu
import handlers.admin.add_dz

@dp.message(Command("start"))
async def cmd_start(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Добавить ДЗ"), KeyboardButton(text="Смотреть ДЗ")],
            [KeyboardButton(text="Помощь")]
        ],
        resize_keyboard=True
    )
    await message.answer('''Даров! 👋
    🤖 Это бот создан для работы с домашним заданием.
    Чтобы перейти в меню с дз, напиши команду /dz,
    а для его добавления напиши /add. Выбери дату:
    Если есть вопросы или предложения, то напиши команду
    /sos и свяжись с админами. Также для упрощения можно
    пользоваться кнопками)''', reply_markup=keyboard)

@dp.message(F.text == "Добавить ДЗ")
async def process_add_dz(message: Message):
    await handlers.admin.add_dz.cmd_add(message)

@dp.message(F.text == "Смотреть ДЗ")
async def process_menu_dz(message: Message):
    await handlers.user.menu.cmd_dz(message)

@dp.message(F.text == "Помощь")
async def process_sos(message: Message):
    await handlers.user.menu.cmd_sos(message)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())