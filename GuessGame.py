import random
import time
number=random.randint(0,10)
guess=0
tries=0
name=input("Hii ,May I Know Your Name Please?? ")
time.sleep(1)
print("Hello "+name+".")
question=input("Are You Ready To Guess?[Y/N]")

if question.lower()=='n':
    time.sleep(1)
    print("I'm Sorry We'll meet other next time!")
    exit()
if question.lower()=="y":
    time.sleep(1)
    print("Let's Guess a number between 1 & 10")

while not (guess==number):
    tries=+1
    guess=int(input("Guess Your Number:-"))
    if guess==number:
        time.sleep(1)
        print("Brilliant")
        print("Congrats ,Your Guess Was Correct.The Number was indeed {}".format(number))
        print("It has taken {} tries".format(tries))
    elif guess<number:
        time.sleep(1)
        print("No ! Guess a Higher Number")
    else:
        time.sleep(1)
        print("No! Guess the lower number")
