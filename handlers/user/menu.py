from datetime import datetime

from aiogram import F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters.callback_data import CallbackData
from aiogram.filters import Command

from loader import dp, db

# '''Ответ на команду menu'''
@dp.message(Command("menu"))
async def cmd_menu(message: Message):
    await message.answer('''Выбери предмет''', reply_markup=butt_subjects())

# '''Создание инлайн кнопок, возможно вынести в файл'''
def butt_subjects():
    inline_kb_list = [
        [InlineKeyboardButton(text="ОДК", callback_data='odk_f')],
        [InlineKeyboardButton(text="ОРГ", callback_data='org_f')],
        [InlineKeyboardButton(text="ИНИТ", callback_data='init_f')],
        [InlineKeyboardButton(text="ИНФА", callback_data='inf_f')],
        [InlineKeyboardButton(text="МАТАН", callback_data='math_f')],
        [InlineKeyboardButton(text="ИР", callback_data='ir_f')],
        [InlineKeyboardButton(text="АНГЛ_Красавчики", callback_data='eng_kr_f')],
        [InlineKeyboardButton(text="АНГЛ_Умники", callback_data='eng_ym_f')],
        [InlineKeyboardButton(text="ВВП", callback_data='vvp_f')],
        [InlineKeyboardButton(text="ФИЗРА", callback_data='phys_f')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# Создаем класс для callback_data
class DateCallbackData(CallbackData, prefix="date"):
    date: str
    subj: str

# Создание кнопок с датами
def butt(subj):
    date_table = db.fetchall(f"SELECT deadline FROM all_homework WHERE lessons = \'{subj}\'")
    inline_kb_list = []
    for element in date_table:
        date = str(element)[15:27].split(", ")
        date_str = f"{date[2]}.{date[1]}.{date[0]}"
        inline_kb_list.append([InlineKeyboardButton(text=date_str, callback_data=DateCallbackData(date=date_str, subj=subj).pack())])
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# Функция для обработки callback_data
@dp.callback_query(DateCallbackData.filter())
async def process_callback(callback_query: CallbackQuery, callback_data: DateCallbackData):
    date = callback_data.date
    subj = callback_data.subj
    await vvp_f(callback_query, date, subj)
    await callback_query.answer()

# Функция vvp_f
async def vvp_f(callback_query: CallbackQuery, date: str, subj: str):
    list_date = date.split(".")
    day = list_date[0]
    month = list_date[1]
    year = list_date[2]
    d_mess = db.fetchall(f"SELECT * FROM all_homework WHERE lessons = \'{subj}\' AND deadline = \'{f"{year}-{month}-{day}"}\'")
    print(d_mess)
    await callback_query.answer(f"Вы выбрали дату: {date}")

# '''Функционал каждой кнопки'''
@dp.callback_query(F.data == 'odk_f')
async def subjects(call: CallbackQuery):
    await call.answer('Сколько перья не цепляй цыпленком не станешь')
    await call.message.answer('''Выбери дату:''', reply_markup=butt("odk"))

@dp.callback_query(F.data == 'org_f')
async def subjects(call: CallbackQuery):
    await call.answer('Мужчина без жены как рыба без велосипеда')
    await call.message.answer('''Выбери дату:''', reply_markup=butt("org"))

@dp.callback_query(F.data == 'init_f')
async def subjects(call: CallbackQuery):
    await call.answer('Нет ничего невозможного если ты пиздабол')
    await call.message.answer('''Выбери дату:''', reply_markup=butt("init"))

@dp.callback_query(F.data == 'inf_f')
async def subjects(call: CallbackQuery):
    await call.answer('Читай коран еби баран')
    await call.message.answer('''Выбери дату:''', reply_markup=butt("inf"))

@dp.callback_query(F.data == 'math_f')
async def subjects(call: CallbackQuery):
    await call.answer('Если пьянка неизбежна-пить надо первым')
    await call.message.answer('''Выбери дату:''', reply_markup=butt("math"))

@dp.callback_query(F.data == 'ir_f')
async def subjects(call: CallbackQuery):
    await call.answer('Я как носок-одинок, но не дырявый')
    await call.message.answer('''Выбери дату:''', reply_markup=butt("ir"))

@dp.callback_query(F.data == 'eng_kr_f')
async def subjects(call: CallbackQuery):
    await call.answer('$$$')
    await call.message.answer('''Выбери дату:''', reply_markup=butt("eng_kr"))

@dp.callback_query(F.data == 'eng_ym_f')
async def subjects(call: CallbackQuery):
    await call.answer('В пиве мало витаминов поэтому его надо пить больше')
    await call.message.answer('''Выбери дату:''', reply_markup=butt("eng_ym"))

@dp.callback_query(F.data == 'vvp_f')
async def subjects(call: CallbackQuery):
    await call.answer('^__^ ;D :3')
    await call.message.answer('''Выбери дату:''', reply_markup=butt("vvp"))

@dp.callback_query(F.data == 'phys_f')
async def subjects(call: CallbackQuery):
    await call.answer('Пиво водка турничок через годик я качок')
    await call.message.answer('''Выбери дату:''', reply_markup=butt("phys"))

# '''Реакция на sos'''
@dp.message(Command("sos"))
async def cmd_sos(message: Message):
    await message.answer('''Обращайтесь к ебейшему @cristalical и его помощнику @neveroyatneyshee!!!''')