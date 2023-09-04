word_list = ['aardvark', 'danger', 'outside', 'spouse', 'dramatic', 'mystery']
display = []

import random
answer = random.choice(word_list)
answerlist = list(answer)
for i in answer:
    display.append('_')
#print(answer)
guess = ''
def userinput():
    print(display)
    global guess
    guess = input('Guess a letter: ')
    guess = guess[0].lower()
#    return guess

def guesscheck():
    global guess
    wrongtries = 0
    for position in range(len(answer)):
        letter = answer[position]
        if letter == guess:
            display[position] = letter
    #print(display)


def gameplay():
    userinput()
    guesscheck()

while '_' in display:
    gameplay()
else:
    print('You win. The word was '+answer)