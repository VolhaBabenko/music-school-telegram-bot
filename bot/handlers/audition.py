from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.keyboards.audition import audition_menu, instrument_menu
from bot.states import AuditionStates

router = Router()

@router.callback_query(F.data == "audition_start")
async def start_audition(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        "🎼 **Запись на прослушивание**\n\n"
        "Выберите инструмент для ребёнка:",
        reply_markup=instrument_menu(),
        parse_mode="Markdown"
    )
    await state.set_state(AuditionStates.instrument)
    await callback.answer()

@router.callback_query(F.data.startswith("instrument_"))
async def select_instrument(callback: CallbackQuery, state: FSMContext):
    instrument = callback.data.split("_")[1]
    await state.update_data(instrument=instrument)
    await callback.message.edit_text(
        f"✅ Выбрано: **{instrument.title()}**\n\n"
        "Выберите удобное время (пример слотов):",
        reply_markup=time_slots_example(),
        parse_mode="Markdown"
    )
    await state.set_state(AuditionStates.time)
    await callback.answer()
