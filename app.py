from aiogram import types
from  aiogram.types import ReplyKeyboardMarkup
from logging import basicConfig, INFO

from date.config import admins
from loader import dp, db, bot

from aiogram.types import ReplyKeyboardRemove
from date.config import ADMINS

user_message = "Челик"
admin_message = "БОГ!"

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    # Тут реализуем то самое разделение на наших админов и на обычных пользователей
    markup.row(user_message, admin_message)

    await message.answer('''Даров! 👋
    🤖 Это бот создан для работы с домашним заданием.
    Чтобы перейти в меню, нипиши команду /menu.
    Если есть вопросы или предложения, то напиши команду
    /sos и свяжись с админами.''', reply_markup==markup)


async def on_startup(dp):
    basicConfig(level=INFO)
    db.create_tables()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())