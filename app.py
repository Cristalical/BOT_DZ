from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
from loader import dp, bot

import handlers.admin.add_dz
import handlers.user.menu

@dp.message(Command("start", "s"))
async def cmd_start(message: Message):
    await message.answer('''Даров! 👋
    🤖 Это бот создан для работы с домашним заданием.
    Чтобы перейти в меню, напиши команду /menu,
    а чтобы добавить дз /add.
    Если есть вопросы или предложения, то напиши команду
    /sos и свяжись с админами.''')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())