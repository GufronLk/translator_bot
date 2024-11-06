from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from googletrans import LANGUAGES


def start_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
        KeyboardButton(text='Перевод'),
        KeyboardButton(text='История'),
        KeyboardButton(text='Избранное')
    )
    return kb


def lang_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = []
    for lang in LANGUAGES.values():
        buttons.append(KeyboardButton(lang))
    kb.add(*buttons)
    return kb


def continue_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(
        KeyboardButton('Да'),
        KeyboardButton('Нет')
    )
    return kb
