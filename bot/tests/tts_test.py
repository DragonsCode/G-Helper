from tts.tts import TextToSpeech
from config import MALE_TTS, FEMALE_TTS

tts = TextToSpeech(FEMALE_TTS)

tts.list_available_voices()
tts.text_to_speech("Hello, this is a test!")