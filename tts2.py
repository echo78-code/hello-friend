import pyttsx3 as p


def speak(param):
	engine = p.init()

	engine.setProperty('rate', 170)

	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[0].id)		#o for male, 1 for female

	engine.say(param)
	engine.runAndWait()