import requests
import pyaudio
import wave
import io
import threading
import requests
import json

class ChatBotApi:
    
    def __init__(self, url="http://localhost:5005/webhooks/rest/webhook"):
        self.url = url

    def send_message(self, message):
        payload = {
            "sender": "user",
            "message": message.lower()
        }
        
        response = requests.post(self.url, json=payload)
        
        if response.status_code == 200:
            bot_responses = response.json()
            #print(f"bot_responses: {bot_responses}")
            control_json = None
            if len(bot_responses) > 1 and bot_responses[1]['custom'] is not None:
                control_json = bot_responses[1]['custom']
            return bot_responses[0]['text'], control_json 
        else:
            return f"Error: Received status code {response.status_code}", None
    
class TTSApi:
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = None

    def play_binary(self, bin_data):
        with wave.open(io.BytesIO(bin_data), 'rb') as f:
            width = f.getsampwidth()
            channels = f.getnchannels()
            rate = f.getframerate()

        if self.stream is None or self.stream.is_stopped():
            self.stream = self.pa.open(
                format=self.pa.get_format_from_width(width),
                channels=channels,
                rate=rate,
                output=True
            )

        def play_audio():
            self.stream.write(bin_data)
            self.stream.stop_stream()

        threading.Thread(target=play_audio).start()

    def server_play(self, text):
        url = f"http://localhost:5002/api/tts?text={text}&speaker_id=p260"
        response = requests.get(url, stream=True)
        
        if response.status_code == 200:
            self.play_binary(response.content)
        else:
            print(f"Error: Unable to fetch audio. Status code: {response.status_code}")

    def __del__(self):
        if self.stream:
            self.stream.close()
        self.pa.terminate()

