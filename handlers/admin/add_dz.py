from aiogram import F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command

from loader import dp
from data.config import ADMINS

@dp.message(Command("add"))
async def cmd_add(message: Message):
    if message.from_user.id in ADMINS:
        await message.answer('''Добро пожаловать, по какому предмету желаешь добавить дз?''', reply_markup=butt_admin())
    else:
        await message.answer('''Куда лезешь без админки?)''')

def butt_admin():
    inline_kb_list = [
        [InlineKeyboardButton(text="ОДК", callback_data='odk_f_a')],
        [InlineKeyboardButton(text="ОРГ", callback_data='org_f_a')],
        [InlineKeyboardButton(text="ИНИТ", callback_data='init_f_a')],
        [InlineKeyboardButton(text="ИНФА", callback_data='inf_f_a')],
        [InlineKeyboardButton(text="МАТАН", callback_data='math_f_a')],
        [InlineKeyboardButton(text="ИР", callback_data='ir_f_a')],
        [InlineKeyboardButton(text="АНГЛ_Красавчики", callback_data='eng_kr_f_a')],
        [InlineKeyboardButton(text="АНГЛ_Умники", callback_data='eng_ym_f_a')],
        [InlineKeyboardButton(text="ВВП", callback_data='vvp_f_a')],
        [InlineKeyboardButton(text="ФИЗРА", callback_data='phys_f_a')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def butt(subj):
    date_table = db.fetchall(f"SELECT deadline FROM all_homework WHERE lessons = \'{subj}\'")
    inline_kb_list = []
    for element in date_table:
        date = str(element)[15:27].split(", ")
        date_str = f"{date[2]}.{date[1]}.{date[0]}"
        inline_kb_list.append([InlineKeyboardButton(text=date_str, callback_data=DateCallbackData(date=date_str, subj=subj).pack())])
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# '''Функционал каждой кнопки'''
@dp.callback_query(F.data == 'odk_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Пиши задание''', reply_markup=butt("odk"))


@dp.callback_query(F.data == 'org_f_A')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Пиши задание''', reply_markup=butt("org"))

@dp.callback_query(F.data == 'init_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Пиши задание''', reply_markup=butt("init"))

@dp.callback_query(F.data == 'inf_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Пиши задание''', reply_markup=butt("inf"))

@dp.callback_query(F.data == 'math_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Пиши задание''', reply_markup=butt("math"))

@dp.callback_query(F.data == 'ir_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Пиши задание''', reply_markup=butt("ir"))

@dp.callback_query(F.data == 'eng_kr_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Пиши задание''', reply_markup=butt("eng_kr"))

@dp.callback_query(F.data == 'eng_ym_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Пиши задание''', reply_markup=butt("eng_ym"))

@dp.callback_query(F.data == 'vvp_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Пиши задание''', reply_markup=butt("vvp"))

@dp.callback_query(F.data == 'phys_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Пиши задание''', reply_markup=butt("phys"))