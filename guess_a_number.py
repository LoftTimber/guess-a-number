

print ("Insert a high.")
high=input()


low=1


import random


rand = random.randint(low, int(high))
print("I'm thinking of a number from "+str(low)+" to "+str(high)+".");

guess = -1

while guess != rand:
    guess = input("Take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
    else:
        print("You got it!")

print("Game over")
