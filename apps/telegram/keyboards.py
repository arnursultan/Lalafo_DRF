from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons = [
    InlineKeyboardButton("Принять", callback_data='accept'),
    InlineKeyboardButton("Отказать", callback_data='refuse')
]

inline = InlineKeyboardMarkup().add(*buttons)