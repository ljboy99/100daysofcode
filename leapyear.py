

year = int(input("What year do you want to check? "))


if year%4 == 0:
    if year%100 != 0:
        isleap = True
    else:
        if year%400 == 0:
            isleap = True
        else:
            isleap = False
else:
    isleap = False

if isleap == True:
    print(f"The year {year} is a leap year!")
elif isleap == False:
    print(f"The year {year} is not a leap year.")

