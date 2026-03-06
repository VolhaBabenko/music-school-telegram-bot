import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import BOT_TOKEN

from bot.keyboards.audition import main_menu
from bot.handlers.audition import router as audition_router
from bot.handlers.navigation import router as navigation_router

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
            "Нажми кнопку ниже, чтобы начать:",
            reply_markup=main_menu(),
            parse_mode="Markdown"
        )

    dp.include_router(audition_router)
    dp.include_router(navigation_router)

    print("🎵 Бот прослушиваний запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
