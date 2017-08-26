from tts import tts
import random
def who_are_you():
    messages = ['I am  dragon, your lovely personal assistant.',
                 'dragon, did not I tell you before?',
                'You ask that so many times! I am dragon']
    tts(random.choice(messages))
def greeting():
    messages=['Hi','Hey']
    tts(random.choice(messages))

def toss_coin():
    outcomes = ['heads', 'tails']
    tts('I just flipped a coin. It shows ' + random.choice(outcomes))
def die_toss():
    outcomes = [1,2,3,4,5,6]
    tts(random.choice(outcomes))
def undefined():
 tts('I dont know what that means!') 
