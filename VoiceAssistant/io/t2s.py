import numpy as np
import sounddevice as sd
from TTS.api import TTS

#en: tts_models/en/ljspeech/vits, fa: tts_models/fa/custom/glow-tts
tts = TTS("tts_models/en/ljspeech/vits")

# List available 🐸TTS models
#print(dir(TTS().list_models()))
print(TTS().list_models().list_models())
print(TTS().list_models().list_langs())
# Text to be converted to speech
text = "hello, this is a test."
#print(tts.speakers)
# Generate the speech
#print(tts.voice_converter.vc_config.audio.output_sample_rate)


def play(txt: str):
    wav = tts.tts(text)

    wav = np.array(wav, dtype=np.float32)

    sd.play(wav, samplerate=tts.synthesizer.output_sample_rate)
    sd.wait()
