answer = input("Am I an object or a place? YES/NO: ")
if answer == "YES":
	answer = input("Am i larger than a household PC? YES/NO: ")
	if answer == "YES":
		answer = input("Am I a building? YES/NO: ")
		if answer == "YES":
			answer = input("Am I a salon? YES/NO: ")
			if answer == "YES":
				print("It's a salon")
			elif answer == "NO":
				print("It's a bowling alley")
			else:
				print("You did it wrong. Try again.")
		elif answer == "NO":
			answer = input("Am I New York? YES/NO: ")
			if answer == "YES":
				print("I am New York!")
			elif answer == "NO":
				print("I am an umbrella!")
			else:
				print("You did it wrong. Try again.")
		else:
			print("You did it wrong. Try again.")
		

	elif answer == "NO":
		answer = input("Am I consumed as you use me? YES/NO: ")
		if answer == "YES":
			answer = input("Am I a bar of soap? YES/NO: ")
			if answer == "YES":
				print("I am a bar of soap!")
			elif answer == "NO":
				print("I am a pizza!")
		elif answer == "NO":
			answer = input("Am I a hat? YES/NO: ")
			if answer == "YES":
				print("I am a hat!")
			elif answer == "NO":
				print("I am a computer!")
			else:
				print("You did it wrong. Try again.")
		else:
			print("You did it wrong. Try again.")
	else:
		print("You did it wrong. Try again.")

elif answer == "NO":
	answer = input("Am I human? YES/NO: ")
	if answer == "YES":
		answer = input("Am I fictional? YES/NO: ")
		if answer == "YES":
			answer = input("Am I Santa Claus? YES/NO: ")
			if answer == "YES":
				print("I am Santa Claus!")
			elif answer == "NO":
				print("I am James Bond!")
		elif answer == "NO":
			answer = input("Am I Britney Spears? YES/NO: ")
			if answer == "YES":
				print("I am Britney Spears!")
			elif answer == "NO":
				print("I am Michael Jackson!")
			else:
				print("You did it wrong. Try again.")
		else:
			print("You did it wrong. Try again.")

	elif answer == "NO":
		answer = input("Could you fit me in a coffee mug? YES/NO: ")
		if answer == "YES":
			answer = input("Am I a frog? YES/NO: ")
			if answer == "YES":
				print("I am a frog!")
			elif answer == "NO":
				print("I am a rat!")
			else:
				print("You did it wrong. Try again.")
		elif answer == "NO":
			answer = input("Am I a chicken? YES/NO: ")
			if answer == "YES":
				print("I am a chicken!")
			elif answer == "NO":
				print("I am Dracula!")
			else:
				print("You did it wrong. Try again.")
		else:
			print("You did it wrong. Try again.")
	else:
		print("You did it wrong. Try again.")
else:
	print("You did it wrong. Try again.")


