from ultron.actions import Action
from gtts import gTTS
import os


class Voice(Action):
    def __init__(self):
        self.tts_engine = gTTS(' ')
        self.filename = ''

    def execute(self, text, filename='current_text.mp3'):
        self.tts_engine = gTTS(text=text, lang='en')
        self.filename = filename
        self.tts_engine.save(savefile=self.filename)
        os.system('mpg321 current_text.mp3 2> /dev/null')
        self.post_execute()
        pass

    def pre_execute(self):
        pass

    def post_execute(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
