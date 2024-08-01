from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from config import TECH_SUPPORT


general_router = Router()

@general_router.message(CommandStart())
async def start_handler(message: Message) -> None:
    """
    This handler is responsible for the start command
    """
    await message.answer(
        "Hi there!\n"
        "This is a Gesture Helper project. "
        "I will help you to translate gestures to text! "
        "Just send me a video or a video note...\n\n"
        "For help enter /help command"
    )

@general_router.message(Command(commands=["help"]))
async def start_handler(message: Message) -> None:
    """
    This handler is responsible for the help command
    """
    await message.answer(
        "Hi there!\n"
        "This is a Gesture Helper project. "
        "I will help you to translate gestures to text!\n"
        "This is a help message.\n\n"
        "I am an AI powered gesture translator! "
        "Send me a video or a video note and I will translate gestures to text\n\n"
        "There are 7 supported signs for test purposes:\n"
        "✋ - hello\n"
        "☝️- look up\n"
        "🤘- I love you\n"
        "✊ - friend\n"
        "👍 - good\n"
        "👎 - bad\n"
        "✌️- victory\n\n"
        f"Technical support: {TECH_SUPPORT}"
    )
