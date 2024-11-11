from aiogram import F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ContentType
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from io import BytesIO
from datetime import datetime

from loader import dp, db, bot, less
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

def butt_cancel():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Отмена", callback_data='cancel')]
    ])

# Обработчик для выбора предмета
@dp.callback_query(F.data.endswith('_f_a'))
async def subjects(call: CallbackQuery, state: FSMContext):
    subject = call.data.split('_f_a')[0]
    await state.update_data(lessons=subject)

    await call.message.answer('Какой дедлайн?', reply_markup=butt_cancel())
    await state.set_state(HomeworkState.waiting_for_deadline)

# Обработчик для ввода дедлайна
@dp.message(HomeworkState.waiting_for_deadline)
async def process_deadline(message: Message, state: FSMContext):
    try:
        # Преобразуем строку даты в объект datetime
        deadline = datetime.strptime(message.text, '%d.%m.%Y')
        await state.update_data(deadline=deadline)
        await message.answer('Пиши описание задания', reply_markup=butt_cancel())
        await state.set_state(HomeworkState.waiting_for_description)
    except ValueError:
        await message.answer('Неверный формат даты. Пожалуйста, введите дату в формате ДД.ММ.ГГГГ.')

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
    await message.answer('Отправь изображение или напиши "пропустить", если не хочешь добавлять изображения')
    await state.set_state(HomeworkState.waiting_for_image_date)

# Обработчик для отправки изображения
@dp.message(F.content_type == ContentType.PHOTO, HomeworkState.waiting_for_image_date)
async def process_image_date(message: Message, state: FSMContext):
    file_id = message.photo[-1].file_id  # Получаем file_id изображения
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_info = await bot.download_file(file_path)

    # Читаем изображение в виде байтового массива
    image_data = BytesIO(file_info.read()).getvalue()

    # Сохраняем изображение в состояние
    await state.update_data(image=image_data)

    await message.answer('Изображение добавлено.')

    # Сохраняем домашнее задание в базу данных
    data = await state.get_data()
    save_homework(data)

    await message.answer(f"Домашнее задание по {less[data['lessons']]} успешно добавлено!")
    await state.clear()

# Обработчик для пропуска изображений
@dp.message(F.text.lower() == "пропустить", HomeworkState.waiting_for_image_date)
async def skip_images(message: Message, state: FSMContext):
    await state.update_data(image=None)
    await message.answer('Изображения пропущены.')

    # Сохраняем домашнее задание в базу данных
    data = await state.get_data()
    save_homework(data)

    await message.answer(f"Домашнее задание по {less[data['lessons']]} успешно добавлено!")
    await state.clear()

# Функция для сохранения домашнего задания в базу данных
def save_homework(data):
    lessons = data['lessons']
    description = data['description']
    deadline = data['deadline']
    format = data['format']
    image = data.get('image', None)

    try:
        db.cur.execute(
            "INSERT INTO all_homework (lessons, description, deadline, format, image_date) VALUES (%s, %s, %s, %s, %s)",
            (lessons, description, deadline, format, image)
        )
        db.conn.commit()
    except Exception as e:
        print(f"Ошибка при сохранении домашнего задания: {e}")
        db.conn.rollback()

# Обработчик для отмены операции
@dp.callback_query(F.data == 'cancel')
async def cancel_operation(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer('Операция отменена.')