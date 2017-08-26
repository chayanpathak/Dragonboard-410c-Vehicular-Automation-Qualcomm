from util import general_conversations,play_music,tell_time,sleep	
#import weather

import ctypes
from util.GPIOlibrary import GPIOProcessor

from util.location import location
from util.restaurant import restaurant
from util.hospital import hospital
from util.headlight import head_light

def brain(name, speech_text, music_path):
	def check_message(check):
		words_of_message = speech_text.split()
		if set(check).issubset(set(words_of_message)):
			return True
		else:
			return False
	if check_message(['who', 'are', 'you']):
		general_conversations.who_are_you()
	elif check_message(['hi']) or check_message(['hey']):
		general_conversations.greeting()
        elif check_message(['time']):
		tell_time.what_is_time()
	elif check_message(['play', 'music']) or check_message(['music']):
		play_music.play_random(music_path)
	elif check_message(['play']):
		play_music.play_specific_music(speech_text, music_path)	
	



   	elif check_message(['Security']) or check_message(['security','on']) or check_message(['security']) or check_message(['Security on']):
		GP= GPIOProcessor()


 		my_test_lib=ctypes.cdll.LoadLibrary('/home/linaro/vehicle3/touch.so')
		value=my_test_lib.main()
		if (value<2):
			print('NO SMS')
		else:
			print('SMS')

		GP.cleanup()


        elif check_message(['light']) or check_message(['light','head']) or check_message(['headlight']):
		head_light()


        elif check_message(['restaurant']):
		restaurant()
        elif check_message(['hospital']) or check_message(['clinic']) or check_message(['Hospital']):
		hospital()

        elif check_message(['petrol']) or check_message(['gas','station']) or check_message(['diesel']):
		location()
		
	



	elif check_message(['sleep']):
		sleep.go_to_sleep()	
 	else:
		general_conversations.undefined()
