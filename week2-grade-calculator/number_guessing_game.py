# Q 1.Create a number guessing game with hints.

print("\n")
print("*"*70)
print("\t\tNumber Guessing Game System")
print("*"*70)
print("\n")

import random
number=random.randint(1,100)
turns=0
while True:
    guess=int(input("Guess a number from 1 to 100: "))
    if(guess == number):
        print("\nCorrect..!You guessed the number")
        break
    elif(guess <number):
        print("Bigger number plese..!\n")
        turns +=1
    elif(guess > number):
        print("Lesser number plaese..!\n")
        turns +=1
    
print("Number of turns: ", turns+1)

print()
print("-"*70)
print("\t\tThanks for visiting me My Python Program..!")
print("-"*70)
print()