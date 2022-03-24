# Import packages to extend Python (just like we extend Sublime, Atom, os VSCode)
from random import randint

# [] => this is an array
# name = [value1, value2, value3]
# an array is a special type of container that can hold multiple items
# arrays are indexed (their contents are assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

sonic_coins = 3
super_mario_coins = 3
total_coins = 3

# True or False are Boolean data types
# essentially, booleans are equivalent to an on or off switch, 1 or 0.
sonic_choice = False

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
		global sonic_coins
		global super_mario_coins
		global total_coins

		sonic_coins = total_coins
		super_mario_coins = total_coins
	else:
		print("Make a valid choice - Y or N")
		#this might generate a bug that we need to fix later
		choice = input("Y / N? ")

# player_choice == False
while sonic_choice is False:
	print("============*/ RPS GAME */===========")
	print("Super Mario Coins:", super_mario_coins, "/", total_coins)
	print("Sonic Coins:", sonic_coins, "/", total_coins)
	print("=====================================")
	# Version 1, to explain array indexing
	# player_choice = choices [1]
	# print ("index 1 in the choice array is " + player_choice + ", which is paper")

	print("Choose your weapon! Or type quit to exit\n")

	sonic_choice = input("Choose rock, paper, or scissors: \n")
	#player_choice now equals TRUE -> it has a value

	if sonic_choice == "quit":
		print("Your chose to quit")
		exit()

	print("user chose: " + sonic_choice)

	# this will be the AI choice -> a random pick from the choices array
	super_mario_choice = choices[randint(0, 2)]

	print("Super Mario chose: " + super_mario_choice)

	if super_mario_choice == sonic_choice
		print("tie")

	elif super_mario_choice == "rock":
		if sonic_choice == "scissors":
			print("you lose!")
			#verbose way
			#player_lives = player_lives - 1
			#simplified way
			sonic_coins -= 1
		else:
			print("you win!")
			super_mario_coins -= 1

	elif super_mario_choice == "paper":
		if sonic_choice == "scissors":
			print("you win!")
			super_mario_coins -= 1
		else:
			print("you lose!")
			sonic_coins -= 1

	elif super_mario_choice == "scissors":
		if sonic_choice == "paper":
			print("you lose!")
			sonic_coins -= 1
		else:
			print("you win!")
			super_mario_coins -= 1

	if sonic_coins == 0:
		winorlose("lose")

	if super_mario_coins == 0:
		winorlose("won")


	print("Sonic Coins:", sonic_coins)
	print("Super Mario Coins:", super_mario_coins)

	# map the loop keep running, by setting player_choice back to False
	# unset, so that our loop condition will evaluate to True
	sonic_choice = False
