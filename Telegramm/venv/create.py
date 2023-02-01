import os

from aiogram import Bot, Dispatcher

bot = Bot(os.environ['BOT_TOKEN'])
dp = Dispatcher(bot)
