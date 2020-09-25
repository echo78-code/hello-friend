from gtts import gTTS 
import os 

from playsound import playsound

print('enter text to be spoken')

mytext = input()

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("welcome.mp3") 

playsound("welcome.mp3")

os.remove("welcome.mp3")
