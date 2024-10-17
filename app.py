from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

from loader import dp, bot
import handlers.user.menu
import handlers.admin.add_dz

user_message = "Челик"
admin_message = "БОГ!"

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer('''Даров! 👋
    🤖 Это бот создан для работы с домашним заданием.
    Чтобы перейти в меню с дз, напиши команду /menu,
    а для его добавления напиши /add.
    Если есть вопросы или предложения, то напиши команду
    /sos и свяжись с админами.''')


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
'''Тут нужно реализовать работу с базой данных возможно'''
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())