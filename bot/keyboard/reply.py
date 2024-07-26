# TODO: Add language and male/female support for voices
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def language_keyboard() -> ReplyKeyboardMarkup:
    """
    Returns reply keyboard markup for languages
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="English")],
            [KeyboardButton(text="Русский")]
        ],
        resize_keyboard=True
    )
    return keyboard

def sex_keyboard() -> ReplyKeyboardMarkup:
    """
    Returns reply keyboard markup for male/female
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Male")],
            [KeyboardButton(text="Female")]
        ],
        resize_keyboard=True
    )
    return keyboard