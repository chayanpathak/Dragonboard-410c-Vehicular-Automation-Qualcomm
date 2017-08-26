import os
import sys
# This function takes a message as an argument and converts it to speech depending on the OS.
def tts(message):
	if sys.platform == 'darwin':
 		tts_engine = 'say'
 		return os.system(tts_engine + ' ' + message) 
	elif sys.platform == 'linux2' or sys.platform == 'linux':
 		tts_engine = 'google_speech -l en'
 		return os.system(tts_engine + ' "' + message + '"') 

