#game start prompt
print("-------------------\n Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#user input
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

#invalid user input prompt
if user_choice != "rock" or "paper" or "scissors": #?????????
    print("Invalid input friend! Use lower caps. Exiting game...")
    exit()

#comupter computing random output
import random
options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)

#user output
print("You chose: ")
print(user_choice)

#computer output
print("Computer chose: ")
print(computer_choice)
