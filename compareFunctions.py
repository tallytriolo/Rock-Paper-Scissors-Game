from Rock-Paper-Scissors-Game import gameVars

def comparefunction():

if super_mario_choice == sonic_choice:
		print("tie")

	elif super_mario_choice == "rock":
		if sonic_choice == "scissors":
			print("you lose!")
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
