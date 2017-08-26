import sys
import yaml
import speech_recognition as sr 
from util.tts import tts
from brain import brain
import subprocess
from util.stt import stt
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
	while True: 





#		if sys.platform.startswith('linux') or sys.platform == 'win32':
#		       subprocess.Popen(['mpg123', '-q', '/home/sandeepunna/GOOGLE/util/MainTera.mp3']).wait()		
 
		speech_text=stt()
		if speech_text is None:
	           continue
		else: 
		   brain(name, speech_text, music_path) 

	#
if __name__ == "__main__":
    main()

	

