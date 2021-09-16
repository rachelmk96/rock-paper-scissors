#starting prompt
print("Rock, Paper, Scissors, Shoot!")
#user input
user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")
print("User choice: ")
print(user_choice)
#computer choice at random
options = ["rock", "paper", "scissors"]

import random
options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Comupter chose: ")
print(computer_choice)
