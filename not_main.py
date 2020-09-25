import tts2
import stt
import os
import timeFunc
import detectionwords
import wakeword

NameErrorSpeak = "first open spotify"
var = True


def mainthread(param = ''):
    if(param == ''):
        input = stt.listen()
    else:
        input = param

    #bot commands -start
    if(input == 'exit' or input == 'bye' or input == 'quiet'):
        input = ''
        tts2.speak('goodbye, have a nice day sir!')
        global var
        var = False

    #spotify commands check - start
    elif (input == "open spotify"):
        input = ""
        import spotify
        tts2.speak('spotify opened')   

    elif (input == "play" or input == "pause"):
        input = ""
        try:
            spotify.playPause()
        except NameError:
            tts2.speak(NameErrorSpeak)

    elif (input == "exit spotify" or input == "close spotify"):
        input = ""
        try:
            spotify.close()
        except NameError:
            tts2.speak(NameErrorSpeak)

    elif (input == "mute"):
        input = ""
        try:    
            spotify.mute()
        except NameError:
            tts2.speak(NameErrorSpeak)

    elif (input == "next"):
        input = ""
        try:
            spotify.next()
        except NameError:
            tts2.speak(NameErrorSpeak)

    elif (input == "previous"):
        input = ""
        try:
            spotify.prev()
        except NameError:
            tts2.speak(NameErrorSpeak)

    elif (input == "shuffle"):
        input = ""
        try:
            spotify.shuffle()
        except NameError:
            tts2.speak(NameErrorSpeak)

    elif (input == "repeat"):
        input = ""
        try:
            spotify.repeat()
        except NameError:
            tts2.speak(NameErrorSpeak)

    elif (input == "like"):
        input = ""
        try:
            spotify.like()
        except NameError:
            tts2.speak(NameErrorSpeak)

    elif (input == "what is playing" or input == "what's playing"):
        input = ""
        try:
            spotify.nowPlaying()
        except NameError:
            tts2.speak(NameErrorSpeak)

    elif ('search' in str(input) and 'spotify' in str(input)):
        try:
            stopwords = ['search', 'for', 'spotify', 'on']
            querywords = input.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)

            spotify.search(result)
            input = ""
        except NameError:
            tts2.speak(NameErrorSpeak)
        except:
            print("error occured!")

    elif (input == "test method"):
        input = ""
        spotify.search("attention")

    elif (input == "home"):
        input = ""
        try:
            spotify.home()
        except NameError:
            tts2.speak(NameErrorSpeak)

     #spotify commands check -end

    #time and date commands -start
    elif((detectionwords.detectwhat(input) == 'found') and ('time' in str(input))):
        input = ''
        tts2.speak(str(timeFunc.exec('time')))

    elif((detectionwords.detectwhat(input) == 'found') and ('date' in str(input))):
        input = ''
        tts2.speak(str(timeFunc.exec('date')))

    elif((detectionwords.detectwhat(input) == 'found') and ('day' in str(input))):
        input = ''
        tts2.speak(str(timeFunc.exec('day')))

    elif((detectionwords.detectwhat(input) == 'found') and ('month' in str(input))):
        input = ''
        tts2.speak(str(timeFunc.exec('month')))

    elif((detectionwords.detectwhat(input) == 'found') and ('year' in str(input))):
        input = ''
        tts2.speak(str(timeFunc.exec('year')))

    elif((detectionwords.detectwhat(input) == 'found') and ('hour' in str(input))):
        input = ''
        tts2.speak(str(timeFunc.exec('hour')))     
                
    elif((detectionwords.detectwhat(input) == 'found') and (('minute' in str(input)) or ('minutes' in str(input)))):
        input = ''
        tts2.speak(str(timeFunc.exec('minute')))

        #time and date commands -end

#wake word detection
while 1:
    wakewordinput = stt.listen()
    wakewordlistener = wakeword.wakeworddetect(wakewordinput)

    if(wakewordlistener == 'awake'):
        timeFunc.welcome()

        while var:
            mainthread('')

    else: #wakeword detection else
        continue

