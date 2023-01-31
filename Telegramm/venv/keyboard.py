from aiogram import types


def get_start_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Установить начальное количество конфет")
    keyboard.add(button_1)
    return keyboard


def restart_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Начать заново")
    keyboard.add(button_1)
    return keyboard
