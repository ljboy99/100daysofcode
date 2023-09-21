import random
#This is probably the most effort I've put into a script so far
#Also the longest script I've written so far at 150+ lines
#I want to create another script which dumps winning hands
#into a txt so I can make another which shows the best hands 
#and when to hit / stan
#Sept 7 2023 - added money so we can gamble now
#Sept 8 2023 - added function to log game results and cards drawn to txt file
#txt file will log as
#RESULT, PLAYEROPENINGHAND, PLAYERDRAWS, DEALEROPENINGHAND, DEALERDRAWS

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

K = 10
Q = 10
J = 10
A = 11
cards = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, K, Q, J]
# tens = ['10', 'King', 'Queen', 'Jack']



playerhand = []
dealerhand = []
playerActive = None
moneyfile = open("balance.txt", "r+")
money = 100
bet = 0
gameresult = ''

def writeresult():
    global playerhand, gameresult, dealerhand
    f = open("results.txt", "a")
    f.write(str(gameresult))
    f.write(", ")
    f.write(str(playerhand[0:2]).replace(',',' +'))
    f.write(", ")
    f.write(str(playerhand[2:]).replace(',',' +'))
    f.write(", ")
    f.write(str(dealerhand[0:2]).replace(',',' +'))
    f.write(", ")
    f.write(str(dealerhand[2:]).replace(',',' +'))
    f.write("\n")
    f.close()
    playerhand = []
    dealerhand = []

def wager():
    global money
    global bet
    bet = int(input(f"You have ${money}. How much are you betting?\n$"))
    money -= bet
    return bet


def wagerwin():
    global money, bet
    print(f"You won {bet}.")
    money += bet*2
    print(f"Your balance is now ${money}")

def dealerFirstDraw():
    dealerhand.append(random.choice(cards))
    dealerhand.append(random.choice(cards))
    dealerSumAdjust()
    #print("The dealer's hand value is " + str(sum(dealerhand)))
    print("The dealer has a face card of", dealerhand[-1])


def dealerSumAdjust():
    if (A in dealerhand) and sum(dealerhand) > 21:
        n = dealerhand.index(A)
        dealerhand[n] = 1
    else:
        return


def printDealerHand():
    global A
    global dealerhand
    if (A in dealerhand) and sum(dealerhand) <= 21:
        print('Dealer hand includes\n', dealerhand, '\nDealer hand is worth: ' + str(sum(dealerhand)))
    elif (A in dealerhand) and sum(dealerhand) > 21:
        m = dealerhand.index(A)
        dealerhand[m] = 1
        print('Dealer hand includes\n', dealerhand, '\nDealer hand is worth: ' + str((sum(dealerhand))))
    elif (A not in dealerhand):
        print('Dealer hand includes\n', dealerhand, '\nDealer hand is worth: ' + str(sum(dealerhand)))


def dealerDrawCard():
    global A, gameresult, dealerhand
    while sum(dealerhand) <= sum(playerhand) and sum(dealerhand) < 21:
        dealerhand.append(random.choice(cards))
        print("The dealer drew " + str(dealerhand[-1]))
        printDealerHand()
        if sum(dealerhand) > sum(playerhand) and sum(dealerhand) <= 21:
            print("The dealer wins!")
            gameresult = "DEALER WINS"
            return gameresult
        elif sum(dealerhand) == sum(playerhand) and sum(dealerhand) >= 17 and sum(playerhand) >= 17:
            print("PUSH!")
            gameresult = "TIE"
            game()
            return gameresult
        elif A not in dealerhand and sum(dealerhand) > 21:
            print("The dealer busts! You win!")
            gameresult = "PLAYER WINS"
            wagerwin()
            return gameresult
        else:
            continue


def playerDrawCard():
    playerhand.append(random.choice(cards))
    print(f'You drew ' + str(playerhand[-1]))


def playerFirstDraw():
    playerhand.append(random.choice(cards))
    playerhand.append(random.choice(cards))
    print(f'You drew ' + str(playerhand[-1]) + ', and ' + str(playerhand[-2]))


def printPlayerHand():
    global A
    global playerhand
    if (A in playerhand) and sum(playerhand) <= 21:
        print('Your hand includes\n', playerhand, '\nYour hand is worth: ' + str(sum(playerhand)))
    elif (A in playerhand) and sum(playerhand) > 21:
        m = playerhand.index(A)
        playerhand[m] = 1
        print('Your hand includes\n', playerhand, '\nYour hand is worth: ' + str((sum(playerhand))))
    elif (A not in playerhand):
        print('Your hand includes\n', playerhand, '\nYour hand is worth: ' + str(sum(playerhand)))


def playerChoice():
    global playerActive
    choice = input("Do you want a hit, stand, or double down?\n")
    if choice[0].lower() == 'h':
        playerDrawCard()
        printPlayerHand()
        if sum(playerhand) < 21:
            playerActive = True
            playerChoice()
        elif sum(playerhand) == 21:
            playerActive = True
            print("Blackjack!!\nGood job!")
            print("The dealer shows his hand.\n" + str(dealerhand))
            return playerActive, playerhand
        else:
            playerActive = False
            print("Bust!!!")
            print("The dealer shows his hand.\n" + str(dealerhand))
            return playerActive
    elif choice[0].lower() == 's':
        playerActive = True
        print("You chose to stand")
        print("The dealer shows his hand.\n" + str(dealerhand))
        return playerActive, playerhand
    elif choice[0].lower() == 'd':
        global money, bet
        money -= bet
        bet *= 2
        playerDrawCard()
        printPlayerHand()
        if sum(playerhand) <= 21:
            playerActive = True
        else:
            playerActive = False
        print("The dealer shows his hand.\n" + str(dealerhand))
        return playerActive, playerhand, bet

def game():
    global playerhand, dealerhand
    playerhand = []
    dealerhand = []
    if gameresult != "TIE":
      wager()
    playerFirstDraw()
    dealerFirstDraw()
    printPlayerHand()
    playerChoice()
    if playerActive == True:
        dealerDrawCard()
    writeresult()
    again()

def again():
    again = input("Do you want to play again? (Y/N)\n")
    if again.lower() == "y":
        playerhand.clear()
        dealerhand.clear()
        game()
    else:
        quit()


print(logo)
print("Welcome to blackjack.")

game()
