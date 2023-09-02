height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(float(weight/height**2))

BMICLASS = ''
if BMI < 18.5:
    BMICLASS = "you are underweight"
elif 18.5 <= BMI <= 25:
    BMICLASS = "you have a normal weight"
elif 25 < BMI <= 30:
    BMICLASS = "you are slightly overweight"
elif 30 < BMI <= 35:
    BMICLASS = "you are obese"
else:
    BMICLASS = "you are clinically obese"

print(f'Your BMI is', BMI, ',', BMICLASS)
