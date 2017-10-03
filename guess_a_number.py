print("==========================")
print("Welcome to Guess a Number!")
print("==========================")

high_pick=True
number=10
guess=0
import math
import random

while high_pick:
    number=input("Insert a high: ")
        
    if int(number)==0 or int(number)==1 or int(number)==2:
        print("Use a different number.")
        
    elif number.isnumeric():
        high_pick=False
        
    else:
        print ("You need to use a number.")

def tries_pm(number):
    tries=math.log(int(number)-1,2)+1
    return int(tries)
        
def show_ending():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@Thank you for playing!@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def pick_number():
    print("I'm thinking of a number from 1 to "+str(number)+".");    

    return random.randint(1, int(number))
        
def get_guess():
    while True:
        guess=input("Take a guess: ")
    
        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print ("You need to use a number.")

            
def check_guess(guess,rand):
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
    else:
        print("-----------")
        print("You got it!")
        print("-----------")
        
def show_gameover():
    
    
    print("---------------------")
    print("You ran out of tries!")

def show_gameover2():
    print("---------------------")
    print(">>>>>>>>>-<<<<<<<<<")
    print(">>>>>Game Over<<<<<")
    print(">>>>>>>>>-<<<<<<<<<")
          
def c_tries(tries):
        c_tries=int(tries)-1
        return c_tries

def play():
    guess=-1
    tries_pm(number)
    tries=tries_pm(number)
    limit=2
    
    rand=pick_number()

    while guess != rand:
        if tries<limit:
            show_gameover()
            print("The number was "+(str(rand))+".")
            show_gameover2()
            return False
        else:
            c_tries(tries)
            tries=c_tries(tries)
            print("You have "+(str(tries))+" tries left.")
            guess=get_guess()

            check_guess(guess,rand)

        
       
            
                

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

            

playing=True
            
while playing:
    play()
    playing=play_again()

show_ending()
