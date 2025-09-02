# main.py

import logging
from aiogram import Bot, Dispatcher, executor, types
import config

# Setup logging
logging.basicConfig(level=logging.INFO)

# Init bot
bot = Bot(token=config.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# Import handlers
from handlers import start, menu

# Register handlers
start.register_handlers(dp)
menu.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
  
