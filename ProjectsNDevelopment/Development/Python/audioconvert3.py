from gtts import gTTS
from playsound import playsound

audio='Speech3.mp3'
language = 'es'
sp=gTTS(text= "escriba el texto a convertir y luego quedese viendo fijamente al ordenador sin parpadear ello es muestra clar e inequivoca de cuan manipulable es usted", lang= language, slow=False)

sp.save(audio)
playsound(audio)