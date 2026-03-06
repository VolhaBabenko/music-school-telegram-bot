from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def audition_menu() -> InlineKeyboardMarkup:
    """Главное меню прослушиваний"""
    builder = InlineKeyboardBuilder()
    builder.button(text="🎼 Записаться на прослушивание", callback_data="audition_start")
    builder.button(text="📅 Доступные слоты", callback_data="slots_calendar")
    builder.button(text="ℹ️ Как проходит прослушивание", callback_data="info_audition")
    builder.button(text="📋 Мои заявки", callback_data="my_auditions")
    builder.adjust(1, 1)
    return builder.as_markup()

def instrument_menu() -> InlineKeyboardMarkup:
    """Выбор инструмента"""
    builder = InlineKeyboardBuilder()
    instruments = [
        ("🎹 Фортепиано", "piano"),
        ("🎸 Гитара", "guitar"), 
        ("🎤 Вокал", "vocal"),
        ("Скрипка", "violin"),
        ("Флейта", "flute"),
        ("Труба", "trumpet")
    ]
    for text, data in instruments:
        builder.button(text=text, callback_data=f"instrument_{data}")
    builder.button(text="⬅️ Назад в меню", callback_data="main_menu")
    builder.adjust(2)
    return builder.as_markup()

def time_slots_example() -> InlineKeyboardMarkup:
    """Пример слотов (mock)"""
    builder = InlineKeyboardBuilder()
    slots = [
        ("10:00 - 10:30", "slot_10_00"),
        ("11:00 - 11:30", "slot_11_00"),
        ("14:00 - 14:30", "slot_14_00"),
        ("15:00 - 15:30", "slot_15_00")
    ]
    for text, data in slots:
        builder.button(text=text, callback_data=data)
    builder.button(text="⬅️ Другой инструмент", callback_data="choose_instrument")
    builder.adjust(1)
    return builder.as_markup()
