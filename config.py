from main import bot, dp
from config import id

async def send_to_admin(dp):
    await bot.send_message(chat_id = id, text = 'Hi, Boys!'
                           '\nWhere are you from?')