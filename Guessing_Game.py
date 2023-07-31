#Luke Brodak 
#CIS 261 Object-Oriented Computer Programming I
#Guessing Game Week 2 Lab 
import random

def display_title(): 
    print("Guess the Number")
    print()

def play_game(limit):
    number = random.randint(1, limit)
    print(f"I am thinkning of a number from 1 to {limit}\n")
    count = 1
    guess = int(input("Your guess: "))

    while(guess != number):
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
        guess = int(input("Your guess: "))
    print(f"You guessed it in {count} tries.\n")

def main():
    display_title()
    again = "yes"
    while again.lower() == "yes":
        limit = int(input("Enter the limit: "))
        play_game(limit)
        again = input("Would you like to play again? Enter (yes/no)")
        print()
    print("So long!")

if __name__ == "__main__":
    main()


