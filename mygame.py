#user name customization
#code for dotenv import, load, and call adapted by Mike Rossetti's code from GitHub see: https://github.com/prof-rossetti/my-first-python-app/blob/main/app/my_script.py
import os
from dotenv import load_dotenv # see: https://github.com/theskumar/python-dotenv

load_dotenv()

USER_NAME = os.getenv("USER_NAME", default="Player One")

#game start prompt
print("-------------------\n Welcome", USER_NAME, "to my Rock-Paper-Scissors game...")
print("-------------------")

#user input
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

#comupter computing random output
import random
options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)

#invalid user input prompt
#User option validation adapted by Gianna Valencia's code from Slack
if user_choice not in options:
    print("Not a valid option", USER_NAME,". Please use lower case. Exiting...")
    exit()

#user output
print("You chose: ")
print(user_choice)

#computer output
print("Computer chose: ")
print(computer_choice)

#determining winner
if user_choice == computer_choice:
  print("It's a tie!")

elif computer_choice == "rock" and user_choice == "paper":
    print("You won!\n")

elif computer_choice == "scissors" and user_choice == "rock":
    print("You won!\n")

elif computer_choice == "paper" and user_choice == "scissors":
    print("You won!\n")

else:
    print("You lost. Sorry!")

#End prompt
print("Thanks for playing", USER_NAME,". Please play again!\n")
