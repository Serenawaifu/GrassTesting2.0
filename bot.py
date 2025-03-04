import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from config import TELEGRAM_BOT_TOKEN, EMAIL_PASSWORD_FILE
from proxy_manager import ProxyManager

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

proxy_manager = ProxyManager('proxies.txt')

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to the Grass Bot! Use /register to create an account.")

@dp.message_handler(commands=['register'])
async def register_account(message: types.Message):
    # Implement account registration logic here
    proxy = proxy_manager.get_random_proxy()
    await message.reply(f"Using proxy: {proxy}")
    # Add your registration logic here

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
