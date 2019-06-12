import speech_recognition as sr

def listen():
	result = 'null'
	r = sr.Recognizer()
	r.energy_threshold = 3000
	with sr.Microphone() as source:
	    r.adjust_for_ambient_noise(source)
	    print("Say something!")
	    audio = r.listen(source, timeout= 4)	
	try:
		print('Processing...')
		result = r.recognize_google(audio, language = 'vi-VI').lower()
		return result
	except sr.UnknownValueError:
	    print("Could not understand audio")
	except sr.RequestError as e:
		print("Could not request; {0}".format(e))

