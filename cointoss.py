import random

result = ["Heads", "Tails"]
coin = random.randint(0,1)
if coin == True:
    print(result[0])
else:
    print(result[1])
