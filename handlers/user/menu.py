from mimetypes import inited

from aiogram.types import Message, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser

basics_of_business_communications = "ОДК"
basics_of_Russian_government = "ОРГ"
history_of_science_and_technology = "ИНИТ"
history_of_Russia = "История России"
infomatics = "Информатика"
mathmatics = "Высшая математика"
introduction_to_the_profession = "Введение в профессию"
physical_education = "Физра, да..."
english = "Английский язык"

@dp.message_handler(IsAdmin(), commands='menu')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add("Hello")


    await message.answer('Меню', reply_markup=markup)


@dp.message_handler(IsUser(), commands='menu')
async def user_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add("Hello, Cristalical!")

    await message.answer('Меню', reply_markup=markup)
