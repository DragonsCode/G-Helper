import pyttsx3

# if you receive errors such as No module named win32com.client,
# No module named win32, or No module named win32api, you will need to additionally install pypiwin32.

class TextToSpeech:
    engine: pyttsx3.Engine

    def __init__(self, voice, rate: int, volume: float) -> None:
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def list_available_voices(self) -> None:
        """
        Lists available voices on the device
        """
        voices: list = [self.engine.getProperty("voices")]

        for i, voice in enumerate(voices[0]):
            print(f"{i + 1}. Name: {voice.name}\nAge: {voice.age}\nLangs: {voice.languages}\nGender: ({voice.gender}) vid: [{voice.id}]\n\n")

    def text_to_speech(self, text: str, file_name: str, save: bool = True) -> None:
        """
        Converts text to speech
        """
        print('Processing voice...')

        if save:
            self.engine.save_to_file(text, file_name)
            
        self.engine.runAndWait()
