import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import TOKEN
from handlers import general_router, gesture_router


dp = Dispatcher()

async def main() -> None:
    """
    Include all routers and run the bot polling
    """
    dp.include_routers(general_router, gesture_router)
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    # Enable logging
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # Run the bot's main loop
    asyncio.run(main())