import random
logo = """
  ________ ____ ______________ _________ _________ ______________ ______________ 
 /  _____/|    |   \_   _____//   _____//   _____/ \__    ___/   |   \_   _____/ 
/   \  ___|    |   /|    __)_ \_____  \ \_____  \    |    | /    ~    \    __)_  
\    \_\  \    |  / |        \/        \/        \   |    | \    Y    /        \ 
 \______  /______/ /_______  /_______  /_______  /   |____|  \___|_  /_______  / 
        \/                 \/        \/        \/                  \/        \/  
 _______   ____ ___  _____ _______________________________                       
 \      \ |    |   \/     \\______   \_   _____/\______   \                      
 /   |   \|    |   /  \ /  \|    |  _/|    __)_  |       _/                      
/    |    \    |  /    Y    \    |   \|        \ |    |   \                      
\____|__  /______/\____|__  /______  /_______  / |____|_  /                      
        \/                \/       \/        \/         \/                       """

answer = 0#random.randint(1, 100)
pguess = 0
result = ''
turnsLeft = 0


def setdifficulty():
  global turnsLeft
  difficulty = input("Choose difficulty: Easy or Hard\n")
  if difficulty.lower() == "hard":
    turnsLeft += 5
  else:
    turnsLeft += 10 
  
def playerguess():
  global pguess, turnsLeft
  print(f"You have {turnsLeft} guesses")
  pguess = int(input("Guess a number between 1 and 100\n>>"))
  turnsLeft -= 1
  return pguess, turnsLeft

def checkguess(pguess, turnsLeft):
  global result
  if pguess == answer:
    result = True
    print(f"That's correct, the answer was {answer}")
  elif pguess < answer:
    result = False
    print(f"That is too low.")
  elif pguess > answer:
    result = False
    print(f"That is too high.")
  return result

def game():
  global answer
  answer = random.randint(1, 100)
  setdifficulty()
  while (result != True) and turnsLeft > 0:
    playerguess()
    checkguess(pguess, turnsLeft)
  if result != True:
    print(f"You lost!!! the answer was {answer}")
  retry()

def retry():
  global turnsLeft, answer
  playagain = input("Do you want to play again? (Y/N)\n>>>")
  if playagain.lower() == "y":
    game()
  else:
    quit()

game()
