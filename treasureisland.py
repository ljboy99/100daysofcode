print('Welcome to Treasure Island. Your mission is to find the treasure.')
choice = input('Do you go LEFT or RIGHT?')

if choice.upper()=="LEFT":
    swimorwait = input("There is a lake. Do you swim or wait?")
    if swimorwait.upper() == "WAIT":
        print("A raft emerges and takes you to a building.")
        whichdoor = input("There are three doors \nWhich do you enter? \nRED DOOR\nBLUE DOOR\nYELLOW DOOR\n")
        if whichdoor.upper() == "RED":
            print("""The inside is on fire and you are engulfed in flames
            GAME OVER""")
        elif whichdoor.upper() == "BLUE":
            print("""You've enraged the beast, he consumes you.
            GAME OVER""")
        elif whichdoor.upper() == "YELLOW":
            print("YOU WIN!")
        else:
            print("GAMEOVER.")
else:
    print("You die\nGAME OVER")

