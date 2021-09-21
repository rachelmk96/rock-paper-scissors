#game start prompt
print("-------------------\n Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#user input
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

#comupter computing random output
import random
options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)

#invalid user input prompt
# User option validation adapted shared by Gianna Valencia from Slack
if user_choice not in options:
    print("Not a valid option friend. Please use lower case. Exiting...")
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
#debugging
breakpoint()

print("Thanks for playing friend. Please play again!")
