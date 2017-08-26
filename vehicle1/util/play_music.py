import os
import sys
import random
import subprocess
from tts import tts
def mp3gen(music_path):
	music_list = []
	for root, dirs, files in os.walk(music_path):
		for filename in files:
			if os.path.splitext(filename)[1] == ".mp3":
				music_list.append(os.path.join(root, filename.lower()))
				print music_list
	return music_list








def music_player(file_name):
	if sys.platform == 'darwin':
		player = "afplay '" + file_name + "'"
		return os.system(player)	
	elif sys.platform == 'linux2' or sys.platform == 'linux':
		print file_name
		subprocess.Popen(['mpg123', '-q', file_name]).wait()
		#player = "mpg123 '" + file_name + "'"
		#print player		
		#return os.system(player)
def play_random(music_path):
	try:
		music_listing = mp3gen(music_path)
		music_playing = random.choice(music_listing)
		song_name=os.path.split(music_playing)		
		tts("Now playing: " + song_name[1])
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

