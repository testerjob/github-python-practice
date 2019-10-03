#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
#print out a message of congratulations to the winner, and ask if the players want to start a new game)

import sys

print("Please choose one: \n-Rock\n-Paper\n-Scissors ")
user1 = input("Please enter your choise: ")
user1 = user1.lower()
user2 = input("Please enter your choice: ")
user2 = user2.lower()

while user1 == user2:
	print("The choise is even, please start all over again: ")
	print("Please choose one: \n-Rock\n-Paper\n-Scissors ")
	user1 = input("Please enter your choise: ")
	user1 = user1.lower()
	user2 = input("Please enter your choice: ")
	user2 = user2.lower()


if user1 == 'rock' or user2 == 'scissors':
	print("User 1 is a WINNER! ")
elif user1 == 'paper' or user2 == 'scissors':
	print("User 2 is the WINNER! ")
elif user1 == 'paper' or user2 == 'rock':
	print("User 1 is a WINNER! ")
elif user1 == 'scissors' or user2 == 'rock':
	print("User 2 is a WINNER! ")
elif user1 == 'scissors' or user2 == 'paper':
	print("User 1 is a WINNER! ")
else:
	print("Please check your spell and start it again: ")






	