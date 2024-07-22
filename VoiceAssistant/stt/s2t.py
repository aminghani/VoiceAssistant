from RealtimeSTT import AudioToTextRecorder

recorder = AudioToTextRecorder(model='small')

def process_text(text):
    print (text)
    
while True:
    recorder.text(process_text)