from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Фильмы')],
                                   [KeyboardButton(text='Сериалы')]
], resize_keyboard=True, input_field_placeholder='Выбирай')

film_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Звездные войны')],
    [KeyboardButton(text='Дополнится')]
],
    resize_keyboard=True, input_field_placeholder='Выбирай')

starwars_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Звездные Войны. Эпизод I')],
    [KeyboardButton(text='Звездные Войны. Эпизод II')]
],  resize_keyboard=True, input_field_placeholder='Выбирай')

seral_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отбросы')],
    [KeyboardButton(text='Дополнится')]
],
    resize_keyboard=True, input_field_placeholder='Выбирай')