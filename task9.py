'''9.1 -- DONE  Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

EXTRAS:

9.2 -- DONE: Keep the game going until the user types “exit”
9.3 -- DONE: Keep track of how many guesses the user has taken, and when the game ends, print this out.'''

#-------------------------------------------------------------------------------------------------------------------------------

import random

number = random.randint(1,9)

guess = input("Hi, let's play the game! \n-if you want to stop the game type \'enter\'\n-now guess a number from 1 to 9: ")

not_in = [1,2,3,4,5,6,7,8,9]

guess_str = guess.isalpha() 

count = 0
while True:
	
	guess=guess.lower()

	if guess == 'exit':
		print("\nThank you for the game. Bye!\n ")
		exit()
		
	guess = int(guess)

	if guess not in not_in: 
		print("Please check your entry. It should be only the number 1 to 9: ")
		guess = input("\nHi, guess a number from 1 to 9: ")
		
	elif guess > number:
		print("Your gues is higher than a number. Try again and Enter a new number:  ")
		guess = input("\nHi, guess a number from 1 to 9: ")
		
	elif guess < number:
		print("Your gues is low than a number. Try again and Enter a new number:  ")
		guess = input("\nHi, guess a number from 1 to 9: ")
		
	else:
		break

	count +=1	
	print("\nThis is your " + str(count) + " attempt.\n" )

if guess == number:
	print("Congradulation, you are correct, the number is " + str(number))









