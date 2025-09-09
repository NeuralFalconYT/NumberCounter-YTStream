from kokoro import KPipeline
import sounddevice as sd
from num2words import num2words

pipeline = KPipeline(lang_code='a')

def play_tts(text):
    generator = pipeline(text, voice='af_heart')
    for i, (gs, ps, audio) in enumerate(generator):
        sd.play(audio, samplerate=24000)
        sd.wait()
          
for number in range(1000, 10000):
    text = num2words(number)
    num_with_commas = f"{number:,}"
    print(num_with_commas)
    #only first letter capitalized
    print(text.capitalize())
    play_tts(text)
