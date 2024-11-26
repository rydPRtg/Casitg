from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

WEB_APP_URL = "https://ваш_сайт.com"  # Замените на URL вашего веб-приложения

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Играть в Казино", web_app=WebAppInfo(url=WEB_APP_URL))
    )
    await message.answer("Добро пожаловать в мини-казино! Нажмите кнопку ниже, чтобы начать.", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
