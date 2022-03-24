from random import randint

welcome_message = "Hi. Welcome to the Rock-Paper-Scissors game.\nYou are Sonic character and the computer \nit will be Super Mario character."
weapon_choices = ["rock", "paper", "scissors"]

user_player = "Sonic"
computer_player = "Super Mario"

user_coins = 3
computer_coins = 3
total_coins = 3

# True or False are Boolean data types
# essentially, booleans are equivalent to an on or off switch, 1 or 0.
user_choice = False

#define a win or lose function
def winorlose(status):
	#version 1 of function
	#print("Inside winorlose function: status is: ", status)
	print("You", status, " Would you like to play again?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("You chose to quit! Better luck next time.")
		exit()
	elif choice == "Y" or choice == "y":
		#reset the player lives and computer lives
		#and reset player choice to False
		global user_coins
		global computer_coins
		global total_coins

		player_coins = total_coins
		computer_coins = total_coins
	else:
		print("Make a valid choice - Y or N")
		#this might generate a bug that we need to fix later
		choice = input("Y / N? ")

# player_choice == False
while user_choice is False:
	print("▁ ▂ ▃ ▄ ▅ ▆ ▇ ▉ ☞ * RPS GAME * ☜ ▉ ▇ ▆ ▅ ▄ ▃ ▂ ▁")
	print(welcome_message)
	print("-------------------- $ $ $ --------------------")
	print("Computer Coins:", computer_coins, "/", total_coins)
	print("Player Coins:", player_coins, "/", total_coins)
	print("=====================================")
	# Version 1, to explain array indexing
	# player_choice = choices [1]
	# print ("index 1 in the choice array is " + player_choice + ", which is paper")

	print("Choose your weapon! Or type quit to exit\n")

	user_choice = input("Choose rock, paper, or scissors: \n")
	#player_choice now equals TRUE -> it has a value

	if user_choice == "quit":
		print("Your chose to quit")
		exit()

	print("user chose: " + user_choice)

	# this will be the AI choice -> a random pick from the choices array
	computer_choice = choices[randint(0, 2)]

	print("computer chose: " + computer_choice)

	if computer_choice == user_choice:
		print("tie")

	elif computer_choice == "rock":
		if user_choice == "scissors":
			print("you lose!")
			#verbose way
			#player_lives = player_lives - 1
			#simplified way
			player_coins -= 1
		else:
			print("you win!")
			computer_coins -= 1

	elif computer_choice == "paper":
		if user_choice == "scissors":
			print("you win!")
			computer_coins -= 1
		else:
			print("you lose!")
			player_coins -= 1

	elif computer_choice == "scissors":
		if user_choice == "paper":
			print("you lose!")
			player_coins -= 1
		else:
			print("you win!")
			computer_coins -= 1

	if player_coins == 0:
		winorlose("lose")

	if computer_coins == 0:
		winorlose("won")


	print("Player Coins:", player_coins)
	print("Computer Coins:", computer_coins)

	# map the loop keep running, by setting player_choice back to False
	# unset, so that our loop condition will evaluate to True
	user_choice = False







