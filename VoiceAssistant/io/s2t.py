from RealtimeSTT import AudioToTextRecorder
from VoiceAssistant.api.bot_api import send_message

recorder = AudioToTextRecorder(model='small')

def process():
    def process_text(text):
        res = send_message(text)
        print(f"User: {text}")
        for response in res:
            print(f"Bot: {response}")
        
    while True:
        recorder.text(process_text)