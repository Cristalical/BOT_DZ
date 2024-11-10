from aiogram import F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, FSInputFile, InputFile, BufferedInputFile
from aiogram.filters.callback_data import CallbackData
from aiogram.filters import Command
from io import BytesIO

from loader import dp, db

# '''Ответ на команду dz'''
@dp.message(Command("dz"))
async def cmd_dz(message: Message):
    await message.answer('''Выбери предмет из списка''', reply_markup=butt_subjects())

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
    await inp(callback_query, date, subj)
    await callback_query.answer()

# Функция для извлечения данных из базы данных и отправки их пользователю
async def inp(callback_query: CallbackQuery, date: str, subj: str):
    try:
        # Запрос данных из базы данных
        row = db.fetchone(
            "SELECT lessons, description, deadline, format, image_date FROM all_homework WHERE lessons = %s AND deadline = %s",
            (subj, date)
        )

        if row:
            lessons, description, deadline, format, image_data = row

            # Преобразование даты в нужный формат
            deadline_str = deadline.strftime("%d.%m.%Y")

            # Создание сообщения
            message_text = f"Предмет: {lessons}\nДата сдачи: {deadline_str}\nОписание: {description}\nФормат: {format}"

            # Отправка изображения с текстом
            if image_data:
                image_file = BytesIO(image_data)
                image_file.name = f"{lessons}_{deadline_str}.png"
                await callback_query.message.answer_photo(
                    BufferedInputFile(image_file.getvalue(), filename=image_file.name),
                    caption=message_text
                )
            else:
                await callback_query.message.answer(message_text)
        else:
            await callback_query.message.answer("Данные не найдены.")

    except Exception as e:
        await callback_query.message.answer(f"Произошла ошибка: {e}")

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
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="@cristalical", url="https://t.me/cristalical")],
        [InlineKeyboardButton(text="@neveroyatneyshee", url="https://t.me/neveroyatneyshee")]
    ])
    await message.answer('''Обращайтесь к @cristalical и @neveroyatneyshee!!!''', reply_markup=inline_kb)