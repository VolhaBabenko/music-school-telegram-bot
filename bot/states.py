"""FSM состояния для записи на прослушивание"""

from aiogram.fsm.state import State, StatesGroup

class AuditionStates(StatesGroup):
    """Состояния диалога записи"""
    instrument = State()
    time_slot = State()
    personal_info = State()
    confirmation = State()
