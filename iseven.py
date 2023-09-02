number = int(input("Which number do you want to check? "))
iseven = number % 2

if iseven == 0:
    print("This is an even number")
else:
    print("This is an odd number")