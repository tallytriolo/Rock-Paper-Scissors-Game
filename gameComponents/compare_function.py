from gameComponents import gameVars

def compare():
	if gameVars.super_mario_choice == gameVars.sonic_choice:
		print("tie")

	elif gameVars.super_mario_choice == "rock":
		if gameVars.sonic_choice == "scissors":
			print("You lost a coin!")
			gameVars.sonic_coins -= 1
		else:
			print("You won and Super Mario lost a coin!")
			gameVars.super_mario_coins -= 1

	elif gameVars.super_mario_choice == "paper":
		if gameVars.sonic_choice == "scissors":
			print("You won and Super Mario lost a coin!")
			gameVars.super_mario_coins -= 1
		else:
			print("You lost a coin!")
			gameVars.sonic_coins -= 1

	elif gameVars.super_mario_choice == "scissors":
		if gameVars.sonic_choice == "paper":
			print("You lost a coin!")
			gameVars.sonic_coins -= 1
		else:
			print("You won and Super Mario lost a coin!")
			gameVars.super_mario_coins -= 1
