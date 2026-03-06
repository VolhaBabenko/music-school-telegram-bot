from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    keyboard = [
        [KeyboardButton(text="Записаться на прослушивание")],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )


def audition_menu():
    keyboard = [
        [KeyboardButton(text="🎹 Фортепиано")],
        [KeyboardButton(text="🎸 Гитара")],
        [KeyboardButton(text="🎻 Скрипка")],
        [KeyboardButton(text="🥁 Ударные")],
        [KeyboardButton(text="⬅️ Назад в меню")],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
