import sys
import yaml
import speech_recognition as sr 
from util.tts import tts
from brain import brain

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']
city_name = profile_data['city_name']
city_code = profile_data['city_code']
music_path = profile_data['music_path']
tts('Hi ' +'my name is '+ name + ' How can I help you?')
def main():
 r = sr.Recognizer()
 with sr.Microphone() as source:
 	print("Say something!")
 	audio = r.listen(source)
 try:
	speech_text = r.recognize_google(audio,language='en-GB').lower().replace("'", "")
 	print("Melissa thinks you said '" + speech_text + "'")
 except sr.UnknownValueError:
	print("Dragon could not understand audio") 
 except sr.RequestError as e:
 	print("Could not request results from Google Speech Recognition service; {0}".format(e))
 brain(name, speech_text, music_path) 
while True:
	main()

