import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import BOT_TOKEN

# Наши модули
from bot.keyboards.audition import audition_menu
from bot.states import AuditionStates
from bot.handlers.audition import router as audition_router

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    @dp.message(CommandStart())
    async def start_handler(message: Message):
        await message.answer(
            "🎼 **Музыкальная школа Меппел**\n\n"
            "📅 **Запись на ПРОСЛУШИВАНИЕ**\n\n"
            "Определим уровень ребёнка и подберём преподавателя.\n\n"
            "Выберите действие:",
            reply_markup=audition_menu(),
            parse_mode="Markdown"
        )
    
    # Подключаем роутеры
    dp.include_router(audition_router)
    
    print("🎵 Бот прослушиваний запущен!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

