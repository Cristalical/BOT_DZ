from aiogram import F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command

from loader import dp


# '''Ответ на команду menu'''
@dp.message(Command("menu"))
async def cmd_menu(message: Message):
    await message.answer('''Выбери предмет, сучка))''', reply_markup=butt())

# '''Создание инлайн кнопок'''
def butt():
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

# '''Функционал каждой кнопки'''
@dp.callback_query(F.data == 'odk_f')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это тип ОДК, выбери дату сучка''')

@dp.callback_query(F.data == 'org_f')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это тип ОРГ, выбери дату сучка''')

@dp.callback_query(F.data == 'init_f')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это тип ИНИТ, выбери дату сучка''')

@dp.callback_query(F.data == 'inf_f')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это тип инфа, выбери дату сучка''')

@dp.callback_query(F.data == 'math_f')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это тип матан, выбери дату сучка''')

@dp.callback_query(F.data == 'ir_f')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это тип история России, выбери дату сучка''')

@dp.callback_query(F.data == 'eng_kr_f')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это тип английский красавчиков, выбери дату сучка''')

@dp.callback_query(F.data == 'eng_ym_f')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это тип английский умничек, выбери дату сучка''')

@dp.callback_query(F.data == 'vvp_f')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это тип введение в профессию, выбери дату сучка''')

@dp.callback_query(F.data == 'phys_f')
async def subjects(call: CallbackQuery):
    await call.answer('Я думаю)')
    await call.message.answer('''Это тип физра, выбери дату сучка''')

# '''Реакция на sos'''
@dp.message(Command("sos"))
async def cmd_sos(message: Message):
    await message.answer('''Обращайтесь к ебейшему @cristalical и его помощнику @neveroyatneyshee!!!''')