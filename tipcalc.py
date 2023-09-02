print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
people = input("How many people to split the bill? ")
tip = input("What percentage tip would you like to give? 10, 12 or 15?" )

bill, people, tip = int(bill), int(people), int(tip)
tip *= .01
tip += 1

totalpaid = bill*tip
splitbill = totalpaid/people


print(f"Each person should pay:", round(splitbill,2))