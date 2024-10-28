from aiogram import F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from loader import dp, db
from data.config import ADMINS

class HomeworkState(StatesGroup):
    waiting_for_id = State()
    waiting_for_lessons = State()
    waiting_for_deadline = State()
    waiting_for_description = State()
    waiting_for_format = State()
    waiting_for_image_date = State()

@dp.message(Command("add"))
async def cmd_add(message: Message):
    if message.from_user.id in ADMINS:
        await message.answer('Добро пожаловать, по какому предмету желаешь добавить дз?', reply_markup=butt_admin())
    else:
        await message.answer('Куда лезешь без админки?)')

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

def butt_cancel():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Отмена", callback_data='cancel')]
    ])

# '''Функционал каждой кнопки'''
@dp.callback_query(F.data.endswith('_f_a'))
async def subjects(call: CallbackQuery, state: FSMContext):
    subject = call.data.split('_f_a')[0]
    await call.answer('Я думаю)')
    await state.update_data(lessons=subject)
    await state.set_state(HomeworkState.waiting_for_lessons)

@dp.message(HomeworkState.waiting_for_lessons)
async def process_id(message: Message, state: FSMContext):
    try:
        db.cur.execute('SELECT MAX(all_homework_id) FROM all_homework')
        max_id = db.cur.fetchone()[0]
        if max_id is None:
            max_id = 0
        new_id = max_id + 1
        await state.update_data(id=new_id)
        await state.set_state(HomeworkState.waiting_for_id)
    except Exception as e:
        await message.answer(f'Ошибка при получении id: {e}')

@dp.message(HomeworkState.waiting_for_id)
async def process_deadline(message: Message, state: FSMContext):
    await message.answer('Какой дедлайн?')
    await state.update_data(deadline=message.text)
    await state.set_state(HomeworkState.waiting_for_deadline)

@dp.message(HomeworkState.waiting_for_deadline)
async def process_description(message: Message, state: FSMContext):
    await message.answer('Пиши описание задания')
    await state.update_data(description=message.text)
    await state.set_state(HomeworkState.waiting_for_description)

@dp.message(HomeworkState.waiting_for_description)
async def process_format(message: Message, state: FSMContext):
    await message.answer('Пиши формат выполнения задания')
    await state.update_data(format=message.text)
    await state.set_state(HomeworkState.waiting_for_format)

@dp.message(HomeworkState.waiting_for_image_date, F.content_type.in_({'photo'}))
async def process_image_date(message: Message, state: FSMContext):
    await message.answer('Отправь изображение')
    await state.update_data(image_date=message.photo[-1].file_id)
    data = await state.get_data()
    save_homework(data)
    await message.answer('Задание добавлено')
    await state.clear()

def save_homework(data):
    try:
        db.cur.execute('''
        INSERT INTO all_homework (all_homework_id, lessons, description, deadline, format, image_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        ''', (data['id'], data['lessons'], data['description'], data['deadline'], data['format'], data['image_date']))
        db.conn.commit()
    except Exception as e:
        print(f'Ошибка при сохранении задания: {e}')