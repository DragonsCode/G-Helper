from aiogram.types import Message
from aiogram import Bot
from aiogram.types.input_file import FSInputFile

from model.gesture import gesture
from tts.tts import TextToSpeech
from config import MALE_TTS, FEMALE_TTS


async def process_message(message: Message, msg: Message, bot: Bot, file) -> None:
    """
    This function is responsible for processing requests for gesture translates
    """
    user_id = message.from_user.id
    download_path = f"downloads/{user_id}.mp4"

    await bot.download_file(file.file_path, download_path)  # download the video under user's ID name
    
    res = gesture(download_path)
    
    await msg.edit_text(f"Translation: {' '.join(res)}")
    
    upload_path = f"uploads/{user_id}.mp3"
    
    tts = TextToSpeech(FEMALE_TTS, 150, 1.0)
    tts.text_to_speech(' '.join(res), upload_path)
    
    audio = FSInputFile(upload_path)
    await message.answer_voice(audio)
