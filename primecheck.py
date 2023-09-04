# Write your code below this line 👇
def prime_checker(number):
    global answer
    answer = ''
    for i in range(2, number):
        if number % i == 0:
            answer = ' not'
    return answer


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
print("It's" + answer + " a prime number.")