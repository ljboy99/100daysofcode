import random

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


def dealerFirstDraw():
    dealerhand.append(random.choice(cards))
    dealerhand.append(random.choice(cards))
    dealerSumAdjust()
    print("The dealer's hand value is " + str(sum(dealerhand)))
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
    global A
    global dealerhand
    while sum(dealerhand) <= sum(playerhand) and sum(dealerhand) < 21:
        dealerhand.append(random.choice(cards))
        print("The dealer drew " + str(dealerhand[-1]))
        printDealerHand()
        if sum(dealerhand) > sum(playerhand) and sum(dealerhand) <= 21:
            print("The dealer wins!")
        elif sum(dealerhand) == sum(playerhand) and sum(dealerhand) >= 17 and sum(playerhand) >= 17:
            print("PUSH!")
        elif A not in dealerhand and sum(dealerhand) > 21:
            print("The dealer busts! You win!")
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
        playerDrawCard()
        printPlayerHand()
        if sum(playerhand) <= 21:
            playerActive = True
        else:
            playerActive = False
        print("The dealer shows his hand.\n" + str(dealerhand))
        return playerActive, playerhand

def game():
    playerFirstDraw()
    dealerFirstDraw()
    printPlayerHand()
    playerChoice()
    if playerActive == True:
        dealerDrawCard()
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
