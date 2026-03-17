import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command

import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")

bot= Bot(token=TOKEN)
dp= Dispatcher()



klaviatura = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Telefon1'), KeyboardButton(text='kanal1')],
        [KeyboardButton(text='Telefon2'), KeyboardButton(text='kanal2')],
    ],
    resize_keyboard=True
)

async def main():
    print('bot ishladi')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
