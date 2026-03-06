from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from bot.keyboards.audition import audition_menu, instrument_menu

router = Router()

@router.callback_query(F.data == "main_menu")
async def back_to_main_menu(callback: CallbackQuery, state: FSMContext):
    """Возврат в главное меню"""
    await state.clear()
    await callback.message.edit_text(
        "🎼 **Музыкальная школа Меппел**\n\n"
        "📅 **Запись на ПРОСЛУШИВАНИЕ**\n\n"
        "Выберите действие:",
        reply_markup=audition_menu(),
        parse_mode="Markdown"
    )
    await callback.answer("🏠 Главное меню")

@router.callback_query(F.data == "choose_instrument")
async def back_to_instruments(callback: CallbackQuery, state: FSMContext):
    """Возврат к выбору инструмента"""
    await callback.message.edit_text(
        "🎼 **Запись на прослушивание**\n\n"
        "Выберите инструмент для ребёнка:",
        reply_markup=instrument_menu(),
        parse_mode="Markdown"
    )
    await callback.answer("🎵 Инструменты")
