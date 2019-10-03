#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
#print out a message of congratulations to the winner, and ask if the players want to start a new game)


import sys

print("Please choose one: \n-Rock\n-Paper\n-Scissors ")
user1 = input("Please enter your choise: ")
user1 = user1.lower()
user2 = input("Please enter your choice: ")
user2 = user2.lower()

#I want to check if user imput is correct and loop it
temp = set([ 'rock', 'scissors', 'paper'] )

while True:
    if user1 not in temp and user2 not in temp:
        print('Please check your spell and type correct word: ')
    
    elif user1 not in temp and user2 in temp:
        print('Please check your spell and type correct word: ')

    elif user2 not in temp and user1 in temp:
        print('Please check your spell and type correct word: ')

    elif user1 == user2:
        print("The choise is even, please start all over again: ")
        print("Please choose one: \n-Rock\n-Paper\n-Scissors ")
    else:
        break

    user1 = input("Please enter your choise: ")
    user1 = user1.lower()
    user2 = input("Please enter your choice: ")
    user2 = user2.lower()


if user1 == 'scissors' and user2 == 'rock':
    print("User 2 is a WINNER! ")

elif user2 == 'scissors' and user1 == 'rock':
    print("User 1 is a WINNER! ")

elif user1 == 'paper' and user2 == 'rock':
    print("User 1 is the WINNER! ")

elif user2 == 'paper' and user1 == 'rock':
    print("User 2 is the WINNER! ")

elif user1 == 'scissors' and user2 == 'paper':
    print("User 1 is the WINNER! ")

elif user2 == 'scissors' and user1 == 'paper':
    print("User 2 is the WINNER! ")





	
