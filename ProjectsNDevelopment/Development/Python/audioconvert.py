from gtts import gTTS
from playsound import playsound

audio='Speech.mp3'
language = 'en'
sp=gTTS(text= "enter you text which you want to cconvert into audio file", lang= language, slow=False)

sp.save(audio)
playsound(audio)