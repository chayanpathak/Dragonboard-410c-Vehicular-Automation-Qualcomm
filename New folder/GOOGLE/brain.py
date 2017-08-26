from util import general_conversations,play_music,tell_time,sleep	
#import weather
def brain(name, speech_text, music_path):
	def check_message(check):
		words_of_message = speech_text.split()
		if set(check).issubset(set(words_of_message)):
			return True
		else:
			return False
	if check_message(['who', 'are', 'you']):
		general_conversations.who_are_you()
	elif check_message(['time']):
		tell_time.what_is_time()
	elif check_message(['sleep']):
		sleep.go_to_sleep()
	elif check_message(['play', 'music']) or check_message(['music']):
		play_music.play_random(music_path)
	elif check_message(['play']):
		play_music.play_specific_music(speech_text, music_path)	
	else:
		general_conversations.undefined()
