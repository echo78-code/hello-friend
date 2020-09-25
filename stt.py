import speech_recognition as sr

r = sr.Recognizer()

recognised_text = False

def listen():
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source, duration=1.6)
        print("speak now")
        text = r.listen(source)

        try:
            global recognised_text
            recognised_text = r.recognize_google(text).lower()
            print(recognised_text)
        except sr.UnknownValueError:
            print("not recognised")
        except sr.RequestError as e:
            print(e)
            
    return recognised_text
