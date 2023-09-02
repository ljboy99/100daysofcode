height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height, weight = float(height), float(weight)

BMI = round(weight / height**2)
print(BMI)