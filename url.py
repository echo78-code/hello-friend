import nltk
import matplotlib.pyplot as plt
import os 
from gtts import gTTS 
from playsound import playsound
import urllib.request

language = 'en'

mytext2 = "enter url to be searched"
myobj = gTTS(text=mytext2, lang=language, slow=False) 
myobj.save("enter.mp3")
playsound("enter.mp3")
usrinp = str(input("enter url to be searched \n"))

myobj = gTTS(text="ok scraping through the webpage now", lang=language, slow=False) 
myobj.save("speak.mp3")
playsound("speak.mp3")

response = urllib.request.urlopen(usrinp)
html = response.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(html)
text = soup.get_text(strip = True)

tokens = [t for t in text.split()]

from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
	if token in stopwords.words('english'):
		clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)

max = 0
mword = ""

for key, val in freq.items():
	#print(str(key) + ':' + str(val))
	if (val > max):
		max = val
		mword = key		

output = 'this page is about: {} which comes {} times'

print(output.format(mword, max))

mytext = output.format(mword, max)
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("final.mp3")
playsound("final.mp3")

freq.plot(20, cumulative=False)	

os.remove("enter.mp3")
os.remove("speak.mp3")
os.remove("final.mp3")
