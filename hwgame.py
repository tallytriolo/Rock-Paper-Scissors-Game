from random import randint

# re-import game variables and function
from rpsGame import gameVars, compareFunctions


def winorlose(status):

	print("You", status, "!!!", " Would you like to play again?")
	gameVars.choice = input("Y / N? ")

	if gameVars.choice == "N" or gameVars.choice == "n":
		print("You chose to quit! Better luck next time.")
		exit()
	elif gameVars.choice == "Y" or gameVars.choice == "y":
		global sonic_coins
		global super_mario_coins
		global total_coins

		gameVars.sonic_coins = gameVars.total_coins
		gameVars.super_mario_coins = gameVars.total_coins
	else:
		print("Make a valid choice - Y or N")
		gameVars.choice = input("Y / N? ")

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

	compareFunctions()

	if gameVars.sonic_coins == 0:
		winorlose("lose")

	if gameVars.super_mario_coins == 0:
		winorlose("won")


	print("Sonic Coins:", gameVars.sonic_coins)
	print("Super Mario Coins:", gameVars.super_mario_coins)


	gameVars.sonic_choice = False







