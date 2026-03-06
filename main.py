import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    @dp.message(CommandStart())
    async def start_handler(message: Message):
        await message.answer("🎹 Добро пожаловать в Музыкальную школу Меппел!\n\n"
                             "Выберите:\n/help - справка")
    
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
