from RealtimeSTT import AudioToTextRecorder
from VoiceAssistant.api.bot_api import send_message
from VoiceAssistant.io.t2s import play
import time
import logging

logging.disable(logging.CRITICAL)
recorder = AudioToTextRecorder(model='base')

WAKE_UP_WORD = 'alex'

def process():
    listening = False
    listen_until = 0
    
    def process_text(text):
        print(text)
        nonlocal listening, listen_until
        if WAKE_UP_WORD.lower() in text.lower():
            play("hey, i'm listening.")
            listening = True
            listen_until = time.time() + 60  
            return None
        
        if listening:
            text_res, json_res = send_message(text)
            play(text_res)
            if json_res is not None:
                print(json_res)
            if time.time() >= listen_until:
                listening = False
        
    while True:
        recorder.text(process_text)
