#game start prompt
print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

#user input

print("You chose: ")
print(user_choice)

#comupter computing
import random
options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)

#computer output
print("Computer chose: ")
print(computer_choice)
