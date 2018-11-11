# -*- coding: utf-8 -*-
#Guessing Game
from random import randint
num=randint(0,100)
num
y=0 
guesses=[]
while y<3:
    guess=int(input("Your Guess:"))
    y=y+1
    guesses.append(guess)
    if guess not in range(0,100):
        print("Out of Bound")
        continue
    else:
        if guess==num:
            print(f"yay, correct guess! You guessed it in {len(guesses)} guesses")
            break
        elif guess!=num  and y==3:
            print("oops,out of chances!")
            continue
        else:
            print("try again!")
    
    if len(guesses)>1 and y==2:
        if abs(num-guess) < abs(num-guesses[-2]):
            print("Hint:warmer")
        else:
            print("Hint:colder")
    else:
        if abs(num-guess) <= 10:
            print("Hint:warm")
        else:
            print("Hint:cold") 

    


