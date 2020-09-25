import stt

name = 'sam'

def prepart(param):
    keywords = ['greetings', 'hey', 'hi', 'howdy', 'bonjour', 'good day', 'how are you', 'yo', 'good morning', 'what\'s up', 'hello']
    for word in keywords:
        if(word in str(param)):
            return 'found'

def wakeworddetect(listener):
    if(prepart(listener) == 'found' and name in listener):
        return 'awake'
    else:
        return 'sleeping'
