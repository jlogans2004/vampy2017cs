import random
import time
print("Welcome to the Choose your Own Adventure game thing. For now this is a crude prototype.")
restart = True
restarted = False
if restarted == True:
	time.sleep(5)
	print("Welcome back! You're about to start again, since you chose to restart. Have fun!\n")
	time.sleep(5)
while restart == True:
	stats_sneak = random.randint(15, 25)
	stats_run = random.randint(15, 25)
	stats_strength = random.randint(15, 25)
	stats_know = random.randint(15, 25)
	skillBoostRestart = True
	while skillBoostRestart == True:
		skillBoost = input("What skill do you want to boost? There are Sneak or Stealth, Running, Strength, and Knowledge (Your skills are at: \nKnowledge: " + str(stats_know) + "\nRunning: " + str(stats_run) + "\nStrength: " + str(stats_strength) + "\nSneak: " + str(stats_sneak) + "\n")
		if skillBoost == "Sneak" or skillBoost == "Stealth":
			stats_sneak += 10
			skillBoostRestart = False
			print("Congrats, your sneak is at " + str(stats_sneak) + "!")
		elif skillBoost == "Running":
			stats_run += 10
			skillBoostRestart = False
			print("Congrats, your running is at " + str(stats_run) + "!")
		elif skillBoost == "Strength":
			stats_strength += 10
			skillBoostRestart = False
			print("Congrats, your strength is at " + str(stats_strength) + "!")
		elif skillBoost == "Knowledge":
			stats_know += 10
			skillBoostRestart = False
			print("Congrats, your knowledge is at " + str(stats_know) + "!")
		else:
			print("Try again, you entered incorrectly.")
	time.sleep(1)
	print("\nOkay, let's begin.\n")
	runOrSolve = True
	startSelection = True
	while startSelection == True:
		time.sleep(1)
		choice = input('You start out in a dungeon, not knowing where you are. "Have fun!" a unknown voice calls out from the distance. There are three doors. You can either\ngo forward\ngo left\ngo right.\nWhat will you do?\n')
		if choice == "go forward" or choice == "Go forward" or choice == "Go Forward" or choice == "GO FORWARD":
			startSelection = False
			choice = input("The forward path leads into a library. You can choose to 'Stop' in the library to gain 10 Knowledge or you could 'Go' forward (and out of the library) to get 5 Stealth because reasons.\n")
			if choice == "Stop":
				stats_know += 10
				time.sleep(1)
				print("\nYour Knowledge skill has increased by 10. It is now " + str(stats_know) + "!")
			elif choice == "Go":
				stats_sneak += 5
				time.sleep(1)
				print("\nYour Stealth skill has increased by 5. It is now " + str(stats_sneak) + "!")
			while runOrSolve == True:
				choice = input("You walk out of the library into a room with puzzles. You can try to 'Solve' them, but that requires 25 Knowledge. You currently have " + str(stats_know) + " Knowledge. There is also a opening on the ceiling. If you have 25 Strength or 25 Running you can try to 'Climb' up. You currently have " + str(stats_strength) + " Strength and " + str(stats_run) + " Running.")
				if choice == "Solve":
					if stats_know >= 25:
						print("You solved the puzzles, and a door appeared out of the far wall.")
						time.sleep(2)
						choice = input("You walk through the door which leads to a strange bedroom. There is a picture on the wall and a trapdoor in the middle of the room. Do you 'look' behind the picture frame or 'drop' into the trapdoor?\n").capitalize()
						bedroom = True
						while bedroom == True:
							if choice == "Look":
								time.sleep(2)
								print("You look behind the painting and you see a corridor behind it. You reach to climb in it but a gust of wind knocks you down into the trapdoor.")
								bedroom = False
							else:
								time.sleep(2)
								print("You did it wrong. Try again.")
							time.sleep(2)
							print("You drop from the trapdoor into an empty room.")
						runOrSolve = False
					elif stats_know < 25 and stats_strength < 25 and stats_run < 25:
						print("You don't have enough skill to do anything, so the game took pity on you and boosted your Knowledge to 25. You should've stayed in the library.")
						stats_know = 25
					else:
						time.sleep(1)
						print("You don't have enough skill to do that.")
				elif choice == "Climb":
					if stats_strength >= 25 or stats_run >= 25:
						print("You jumped up into the ceiling, doing some softcore parkour. You reach the top and keep going, until you fall into a passageway.")
						runOrSolve = False
						time.sleep(1)
					elif stats_know < 25 and stats_strength < 25 and stats_run < 25:
						print("You don't have enough skill to do anything, so the game took pity on you and boosted your Strength and Running to 25.")
						stats_strength = 25
						stats_run = 25
					else:
						time.sleep(1)
						print("You don't have enough skill to do that.")
				else:
					time.sleep(1)
					print("You did it wrong, try again.")
		elif choice == "go left" or choice == "Go left" or choice == "Go Left" or choice == "GO LEFT":
			startSelection = False
			time.sleep(1)
			choice = input("You walk to the left and stumble into a dark... gym. 'Why is this here?' you ask to yourself. There are treadmills (somehow running) and some weights. You can 'boost Strength' to increase your Strength by 10 or 'boost Speed' to boost your Speed by 10.\n")
			boost = True
			while boost == True:
				if choice == "boost Strength":
					time.sleep(1)
					stats_strength += 10
					boost = False
					print("Your Strength was increased by 10. It is now " + str(stats_strength) + "!")
				elif choice == "boost Speed":
					time.sleep(1)
					stats_run += 10
					print("Your Running was increased by 10. It is now " + str(stats_run) + "!")
					boost = False
				else:
					print("You did it wrong. Try again.")
			print("You run forward, out of the gym and into a maze. It is relatively short, and you can choose to either stick to the left or stick to the right.")
			time.sleep(1)
			choice = input("What will you do? Keep your hand to the 'right' or keep your hand to the 'left'?\n")
			if choice == "MORRIS IS GOD":
				print("Congradulation easter egg over 9000. You increase skills to 9001.")
				stats_know = 9001
				stats_run = 9001
				stats_strength = 9001
				stats_sneak = 9001
				time.sleep(1)
				print("\nBy the way, you have illusion of choice here.\n")
			monster = True
			choice = input("You get through the maze, keeping your hand on the wall. You walk out of the maze into a empty room. There is a creature shrouded in darkness on a throne in the middle of the room. Do you 'Fight' it (requires 30 strength) or 'Run Away' (Requires 20 stealth and 30 running)\n").capitalize()
			if choice == "Fight":
				if stats_strength >= 30:
					print("You walk up to the beast, punching it in the face. It surprisingly just falls over. You walk out a door into the fresh air.")
		elif choice == "go right" or choice == "Go right" or choice == "Go Right" or choice == "GO RIGHT":
			startSelection = False
		else:
			print("You did it wrong. Pick again.")
			time.sleep(5)

	time.sleep(2)
	choice = input("Do you want to restart?\n").capitalize()
	if choice == "Yes":
		restarted = True
		restart = True
	if choice == "No":
		restart = False
		restarted = False
	print("Your skills were:\nKnowledge: " + str(stats_know) + "\nStrength: " + str(stats_strength) + "\nRunning: " + str(stats_run) + "\nStealth: " + str(stats_sneak))
