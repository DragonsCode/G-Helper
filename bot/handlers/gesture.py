from aiogram import F, Router, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from functions.process_message import process_message


gesture_router = Router()

@gesture_router.message(F.video)
async def video_handler(message: Message, bot: Bot) -> None:
    """
    This handler handles videos from users and saves them as video files if the video size is under 50 MB
    """
    # if video is bigger than 50 MB then we will not take it
    if message.video.file_size > 50*1024*1024:
        await message.answer("Too big file. Try to send video not bigger than 50 MB")
        return
    
    msg = await message.answer("Processing your video, please wait")

    file_id = message.video.file_id # get the file id of the video 
    file = await bot.get_file(file_id) # find the file using its file id

    await process_message(message, msg, bot, file)

@gesture_router.message(F.video_note)
async def video_note_handler(message: Message, bot: Bot) -> None:
    """
    This handler handles video notes from users and saves them as video files
    """
    msg = await message.answer("Processing your video, please wait")

    file_id = message.video_note.file_id # get the file id of the video note
    file = await bot.get_file(file_id) # find the file using its file id

    await process_message(message, msg, bot, file)
