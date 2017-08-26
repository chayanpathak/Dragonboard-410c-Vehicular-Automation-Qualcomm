# obtain audio from the microphone
import speech_recognition as sr
import os
import sys
r = sr.Recognizer()
with sr.Microphone() as source:
 print("Say something!")
 audio = r.listen(source)
# recognize speech using Google Speech Recognition
try:
 # for testing purposes, you're just using the default API key
 # to use another API key, use `r.recognize_google(audio,key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
 # instead of `r.recognize_google(audio)`
 message=r.recognize_google(audio,language='en-GB')
 print("Google Speech Recognition thinks you said " + message )
except sr.UnknownValueError:
 print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
 print("Could not request results from Google Speech Recognition service{0}".format(e)) 

tts(message)
# This function takes a message as an argument and converts it to speech depending on the OS.
def tts(message):
	if sys.platform == 'darwin':
 		tts_engine = 'say'
 		return os.system(tts_engine + ' ' + message) 
	elif sys.platform == 'linux2' or sys.platform == 'linux':
 		tts_engine = 'google_speech -l en'
 		return os.system(tts_engine + ' "' + message + '"') 

