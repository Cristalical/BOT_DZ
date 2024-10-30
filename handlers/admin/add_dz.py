from aiogram import F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ContentType
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from loader import dp, db, bot
from data.config import ADMINS

# Определяем состояния для FSM
class HomeworkState(StatesGroup):
    waiting_for_deadline = State()
    waiting_for_description = State()
    waiting_for_format = State()
    waiting_for_image_date = State()

# Обработчик команды /add
@dp.message(Command("add"))
async def cmd_add(message: Message):
    if message.from_user.id in ADMINS:
        await message.answer('Добро пожаловать, по какому предмету желаешь добавить дз?', reply_markup=butt_admin())
    else:
        await message.answer('Куда лезешь без админки?)')

# Функция для создания клавиатуры с предметами
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

# Функция для создания клавиатуры с кнопкой отмены
def butt_cancel():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Отмена", callback_data='cancel')]
    ])

# Обработчик для выбора предмета
@dp.callback_query(F.data.endswith('_f_a'))
async def subjects(call: CallbackQuery, state: FSMContext):
    subject = call.data.split('_f_a')[0]
    await state.update_data(lessons=subject)

    # Получаем максимальный ID из базы данных и увеличиваем его на 1
    try:
        db.cur.execute('SELECT MAX(all_homework_id) FROM all_homework')
        max_id = db.cur.fetchone()[0]
        if max_id is None:
            max_id = 0
        new_id = max_id + 1
        await state.update_data(id=new_id)
    except Exception as e:
        await call.message.answer(f'Ошибка при получении id: {e}')
        return

    await call.message.answer('Какой дедлайн?', reply_markup=butt_cancel())
    await state.set_state(HomeworkState.waiting_for_deadline)

# Обработчик для ввода дедлайна
@dp.message(HomeworkState.waiting_for_deadline)
async def process_deadline(message: Message, state: FSMContext):
    await state.update_data(deadline=message.text)
    await message.answer('Пиши описание задания', reply_markup=butt_cancel())
    await state.set_state(HomeworkState.waiting_for_description)

# Обработчик для ввода описания задания
@dp.message(HomeworkState.waiting_for_description)
async def process_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer('Пиши формат выполнения задания', reply_markup=butt_cancel())
    await state.set_state(HomeworkState.waiting_for_format)

# Обработчик для ввода формата выполнения задания
@dp.message(HomeworkState.waiting_for_format)
async def process_format(message: Message, state: FSMContext):
    await state.update_data(format=message.text)
    await message.answer('Отправь изображение', reply_markup=butt_cancel())
    await state.set_state(HomeworkState.waiting_for_image_date)

# Обработчик для отправки изображения
@dp.message(StateFilter(HomeworkState.waiting_for_image_date), F.content_type == ContentType.PHOTO)
async def process_image_date(message: Message, state: FSMContext):
    file_id = message.photo[-1].file_id  # Получаем file_id изображения
    file = await bot.get_file(file_id)
    file_path = file.file_path
    destination = f"C:/bot/{file_id}.jpg"
    await bot.download_file(file_path, destination)
    await state.update_data(image_date=destination)
    data = await state.get_data()
    save_homework(data)
    await message.answer('Домашнее задание успешно добавлено!')
    await state.clear()


# Функция для сохранения данных в базу данных
def save_homework(data):
    try:
        print(data)
        db.cur.execute('''
        INSERT INTO all_homework (all_homework_id, lessons, description, deadline, format, image_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        ''', (data['id'], data['lessons'], data['description'], data['deadline'], data['format'], data['image_date']))
        db.conn.commit()
    except Exception as e:
        print(f'Ошибка при сохранении задания: {e}')

# Обработчик для отмены операции
@dp.callback_query(F.data == 'cancel')
async def cancel_operation(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer('Операция отменена.')
