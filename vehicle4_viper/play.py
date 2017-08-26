import os
import sys
import random
from tts import tts


def mp3gen():
	global music_listing = []
	for root, dirs, files in os.walk(profile.data['music_path']):
		for filename in files:
			if os.path.splitext(filename)[1] == ".mp3":
				music_listing.append(os.path.join(root, filename.lower()))
	
def music_player(music_selection):
    
    player = music_selection[0] + " '" + music_selection[1] + "'"
    return os.system(player)


def music_player(file_name):
	if sys.platform == 'darwin':
		player = "afplay '" + file_name + "'"
		return os.system(player)
	elif sys.platform == 'linux2' or sys.platform == 'linux':
		player = "mpg123 '" + file_name + "'"
                print player
		return os.system(player)

def play_random(music_path):
	try:
		music_listing = mp3gen(music_path)
		music_playing = random.choice(music_listing)
		song_name = os.path.splitext(basename(music_playing[1]))[0]
		print song_name        	
		tts("Now playing: " + song_name)
        	music_player(song_name)
		print music_playing
		tts("Now playing: " + music_playing)
		music_player(music_playing)
	except IndexError as e:
		tts('No music files found.')
		print("No music files found: {0}".format(e))
def play_specific_music(speech_text, music_path):
	words_of_message = speech_text.split()
	words_of_message.remove('play')
	cleaned_message = ' '.join(words_of_message)
	music_listing = mp3gen(music_path)
	for i in range(0, len(music_listing)):
		if cleaned_message in music_listing[i]:
			music_player(music_listing[i])

