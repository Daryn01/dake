import asyncio
from aiogram import Bot, Dispatcehr, executor
from config import token

loop = asyncio.get_event_loop()
bot = Bot(token, parse_mode = 'HTML')
dp = Dispatcher(bot, loop = loop)

if name == 'main':
    from dispatcher import dp, send_to_admin
    executor.start_polling(dp, on startup = send_to_admin)
