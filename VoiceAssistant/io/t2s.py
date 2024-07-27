import numpy as np
import sounddevice as sd
from TTS.api import TTS

tts = TTS("tts_models/en/ljspeech/vits")


print(TTS().list_models().list_models())
print(TTS().list_models().list_langs())



def play(txt: str):
    wav = tts.tts(txt)

    wav = np.array(wav, dtype=np.float32)

    sd.play(wav, samplerate=tts.synthesizer.output_sample_rate)
    sd.wait()
