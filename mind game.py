import random
number =random.randint(1, 100)
while True :
    guess=int(input("enter your guess:"))
    if guess > number:
        print("it's high value")
    elif guess < number:
        print("it's low value")
    else:
        print("great\n")
        print("correct\n")
        break

