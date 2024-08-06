import logging
import sys
from RealtimeSTT import AudioToTextRecorder
from apis.api import ChatBotApi, TTSApi
import time

def process():
    listening = False
    listen_until = 0
    WAKE_UP_WORD = 'alexa'
    tts = TTSApi()
    chatbot = ChatBotApi()
    recorder = AudioToTextRecorder(model='base')

    def process_text(text):
        nonlocal listening, listen_until
        if WAKE_UP_WORD.lower() in text.lower():
            tts.server_play("i'm listening.")
            listening = True
            listen_until = time.time() + 60  
            return None
        
        if listening:
            text_res, json_res = chatbot.send_message(text)
            tts.server_play(text_res)
            if json_res is not None:
                print(json_res)
                listening = False
            if time.time() >= listen_until:
                listening = False

    while True:
        recorder.text(process_text)

if __name__ == '__main__':
    process()