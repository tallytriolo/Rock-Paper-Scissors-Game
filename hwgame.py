from random import randint
from gameComponents import gameVars, compare_function

#welcome_message = "Hi. Welcome to the Rock-Paper-Scissors game.\nYou are Sonic character and the computer \nit will be Super Mario character."
#choices = ["rock", "paper", "scissors"]

#sonic_coins = 1
#super_mario_coins = 1
#total_coins = 1

#sonic_choice = False
#super_mario_choice = -1

def winorlose(status):

	print("You", status, "the game!!!", " Would you like to play again?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("You chose to quit! See you next time.")
		exit()
	elif choice == "Y" or choice == "y":
		global sonic_coins
		global super_mario_coins
		global total_coins

		gameVars.sonic_coins = gameVars.total_coins
		gameVars.super_mario_coins = gameVars.total_coins
	else:
		print("Make a valid choice - Y or N")
		choice = input("Y / N? ")

while gameVars.sonic_choice is False:
	print("•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$")
	print("▁ ▂ ▃ ▄ ▅ ▆ ▇ ▉ ☞ * RPS GAME * ☜ ▉ ▇ ▆ ▅ ▄ ▃ ▂ ▁")
	print(gameVars.welcome_message)
	print("------------------------------------------------")
	print("Sonic Coins:", gameVars.sonic_coins, "/", gameVars.total_coins)
	print("-------------------- $ $ $ ---------------------")
	print("Super Mario Coins:", gameVars.super_mario_coins, "/", gameVars.total_coins)
	print("------------------------------------------------")
	print("•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$•$")

	print("Choose your weapon! Or type quit to exit\n")

	gameVars.sonic_choice = input("Choose rock, paper, or scissors: \n")

	if gameVars.sonic_choice == "quit":
		print("Your chose to quit!")
		exit()

	print("Sonic chose: " + gameVars.sonic_choice)

	gameVars.super_mario_choice = gameVars.choices[randint(0, 2)]

	print("Super Mario chose: " + gameVars.super_mario_choice)

	compare_function.compare()

	if gameVars.sonic_coins == 0:
		winorlose("lost")

	if gameVars.super_mario_coins == 0:
		winorlose("won")

	print("Sonic Coins:", gameVars.sonic_coins)
	print("Super Mario Coins:", gameVars.super_mario_coins)

	gameVars.sonic_choice = False
 






