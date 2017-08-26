import os
from os.path import basename
import sys
import random

def mp3gen():
    
    global music_listing
    music_listing = []
    for root, dirs, files in os.walk('/home/sandeepunna/Downloads'):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                if sys.platform == sys.platform == 'linux2' or sys.platform == 'linux':
                    music_listing.append([
                        'mpg123',
                        filename.lower()])

    print music_listing
mp3gen()
