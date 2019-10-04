'''1.DONE  Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

DONE: Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.'''


#Task9.1_________________________________________________________________________________

import random

number = random.randint(1,9)

guess = input("Hi, let's play the game! \n-if you want to stop the game type \'enter\'\n-now guess a number from 1 to 9: ")

not_in = [1,2,3,4,5,6,7,8,9]

guess_str = guess.isalpha() 

while True:
	guess=guess.lower()

	if guess == 'exit':
		print("Thank you for the game. Bye! ")
		exit()
		
	guess = int(guess)

	if guess not in not_in: #and guess not in guess_str:
		print("Please check your entry. It should be only the number 1 to 9: ")
		guess = input("Hi, guess a number from 1 to 9: ")

	elif guess > number:
		print("Your gues is higher than a number. Try again and Enter a new number:  ")
		guess = input("Hi, guess a number from 1 to 9: ")

	elif guess < number:
		print("Your gues is low than a number. Try again and Enter a new number:  ")
		guess = input("Hi, guess a number from 1 to 9: ")

	else:
		break

if guess == number:
	print("Congradulation, you are correct, the number is " + str(number))