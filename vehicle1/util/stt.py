# obtain audio from the microphone
import speech_recognition as sr
def stt():
	r = sr.Recognizer()
	r.energy_threshold = 4000
	r.dynamic_energy_threshold = True
	with sr.Microphone() as source:
 		r.adjust_for_ambient_noise(source, duration = 1)
 		print("Say something!")
		audio = r.listen(source)
# recognize speech using Google Speech Recognition
	try:
 # for testing purposes, you're just using the default API key
 # to use another API key, use `r.recognize_google(audio,key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
 # instead of `r.recognize_google(audio)`



         speech_text= r.recognize_google(audio,language='en-GB')
	 print("Google Speech Recognition thinks you said " + speech_text)
	except sr.UnknownValueError:
	 print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	 print("Could not request results from Google Speech Recognition service{0}".format(e)) 
	else: 
	 return speech_text
