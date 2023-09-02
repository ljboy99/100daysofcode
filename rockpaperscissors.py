rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

rps = [rock, paper, scissors]
playerchoice = ''
opponentchoice = None
def chooseinput():
    global playerchoice
    playerchoice = input("Press 1 for rock, 2 for paper, and 3 for scissors")
    global opponentchoice
    opponentchoice = random.choice(rps)
    generateresult()
    return playerchoice, opponentchoice

def generateresult():
    global playerchoice, opponentchoice
    if playerchoice == "1":
        playerchoice = rps[0]
        if opponentchoice == rps[0]:
            result = "The game is a tie!"
        elif opponentchoice == rps[1]:
            result = "Paper beats rock! You lose!"
        else:
            result = "You win!"
    elif playerchoice == "2":
        playerchoice = rps[1]
        if opponentchoice == rps[0]:
            result = "You win!"
        elif opponentchoice == rps[1]:
            result = "The game is a tie!"
        else:
            result = "Scissors beats paper! You lose!"
    elif playerchoice == "3":
        playerchoice = rps[2]
        if opponentchoice == rps[0]:
            result = "Rock beats scissors! You lose!"
        elif opponentchoice == rps[1]:
            result = "You win!"
        else:
            result = "The game is a tie!"
    print(f"""
    You played
    {playerchoice}
    Your opponent played
    {opponentchoice}
    {result}""")
    playagain()

def playagain():
    replay = input("Do you want to play again? Y/N\n")
    if replay.upper() == "Y":
        chooseinput()
    else:
        return

chooseinput()



