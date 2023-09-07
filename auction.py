import os

allbids = {}
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def clear_console():
    if (os.name == 'posix'):  # works for MacOS and Linux
        cmd = 'clear'
    else:  # works for Windows
        cmd = 'cls'
    os.system(cmd)
    #So this works when you run the script on powershell or cmd
    #but PyCharm doesn't clear lines off.

def bidcalc():
    highest = 0
    for bidder in allbids:
        if allbids[bidder] > highest:
            highest = allbids[bidder]
            winner = bidder
        else:
            continue
    print("The highest bid is", highest, "\nCongradulations,", winner)


otherbidders = 'y'
while otherbidders.lower() == "y":
    print(logo)
    bidder = input("What is your name?\n>")
    bid = int(input(bidder + ", Please enter your bid.\n$"))
    allbids[bidder] = bid
    otherbidders = input("Are there other bidders? (Y/N)\n>")
    clear_console()

bidcalc()
