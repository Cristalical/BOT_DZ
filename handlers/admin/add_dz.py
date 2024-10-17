from aiogram import F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command

from loader import dp
from data.config import ADMINS

@dp.message(Command("add"))
async def cmd_add(message: Message):
    if message.from_user.id in ADMINS:
        await message.answer('''Добро пожаловать, по какому предмету желаете добавить дз?''', reply_markup=butt_admin())
    else:
        await message.answer('''Я сорри, ты не админ, ты сучка)))''')

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

# '''Функционал каждой кнопки'''
@dp.callback_query(F.data == 'odk_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это ОДК''')

@dp.callback_query(F.data == 'org_f_A')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это ОРГ''')

@dp.callback_query(F.data == 'init_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это ИНИТ''')

@dp.callback_query(F.data == 'inf_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это инфа''')

@dp.callback_query(F.data == 'math_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это матан''')

@dp.callback_query(F.data == 'ir_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это история России''')

@dp.callback_query(F.data == 'eng_kr_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это английский красавчиков''')

@dp.callback_query(F.data == 'eng_ym_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это английский умничек''')

@dp.callback_query(F.data == 'vvp_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это введение в профессию''')

@dp.callback_query(F.data == 'phys_f_a')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это физра''')