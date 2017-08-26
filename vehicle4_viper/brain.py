from util import general_conversations,play_music,tell_time,sleep	
#import weather
from util.location import location
from util.restaurant import restaurant
from util.hospital import hospital
from util.headlight import head_light
from util.vipernew import *
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
	

	elif check_message(['viper']) or check_message(['Viper'])or  check_message(['on','motor']) or check_message(['Motors']) or check_message(['motors']) or check_message(['motor']) or check_message	(['on','Motor']):
		viper_on()
		




        elif check_message(['light']) or check_message(['light','head']) or check_message(['headlight']) or check_message(['lights']):
		head_light()


        elif check_message(['restaurant']) or check_message(['restaurants']) or check_message(['Restaurant']) or check_message(['Restaurants']):
		restaurant()
        elif check_message(['hospital']) or check_message(['clinic']) or check_message(['Hospital']) or check_message(['hospitals']) or check_message(['Hospitals']):
		hospital()

        elif check_message(['petrol']) or check_message(['gas','station']) or check_message(['diesel']) or check_message(['gas','stations']):
		location()
		
	



	elif check_message(['sleep']):
		sleep.go_to_sleep()	
 	else:
		general_conversations.undefined()
