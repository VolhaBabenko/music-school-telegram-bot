from aiogram import Router, F
from aiogram.types import Message

from bot.keyboards.audition import main_menu, audition_menu

router = Router()


@router.message(F.text == "Записаться на прослушивание")
async def open_audition_menu(message: Message):
    await message.answer(
        "Выбери инструмент для прослушивания:",
        reply_markup=audition_menu()
    )


@router.message(F.text == "⬅️ Назад в меню")
async def back_to_main_menu(message: Message):
    await message.answer(
        "Главное меню:",
        reply_markup=main_menu()
    )
