# Making a Rock, Paper, Scissors game
import random

def game():

    user = " "

    while user != "e":
        user = input("Enter your choice. 'r' for rock, 'p' for paper or 's' for scissors or 'e' to exit the game: ").lower()
        list = ["r", "p", "s"]
        computer = random.choice(list)
        if user == "r" or user == "p" or user == "s":
            if user == computer:
                print("It\'s a tie.")
            elif (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
                print("You won!!")
            else:
                print("The computer won.")
        elif user == "e":
            return("Thanks for playing, come back another time.")
        else:
            print("Invalid input. Try again")

print(game())
