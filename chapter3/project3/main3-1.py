from gtts import gTTS
from playsound import playsound

text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=text, lang='ko')
tts.save(r"본론.mp3")

playsound("본론.mp3")