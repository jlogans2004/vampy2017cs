import random
import time
#friends = ["Bill" , "Tom" , "Joj" , "Jaf" , "ggg"]

#num = 0

#while True:
#	num = random.randint(1,3)
#	guess = input("Rock, paper or scizzors?\n")
#	if(guess == "Rock" or guess == "rock" or guess == "ROCK"):
#		guess = 1
#	elif(guess == "Paper" or guess == "paper" or guess == "PAPER"):
#		guess = 2
#	elif(guess == "Scizzors" or guess == "scizzors" or guess == "SCIZZORS"):
#		guess = 3
#	else:
#		print("You did it wrong. Try again.")
#	if(guess == num - 1 or guess == num + 2):
#		print("You win!")
#		break;
#	elif(guess == num):
#		print("Tie!")
#	elif(guess == num + 1):
#		print("You Lose!")

numGuess = False
guess = 1
lower = 0
upper = 0
print("Think of a number. Keep it in your head and write it down. The computer will guess a number. If the guess is greater than your number, type 'greater' in the console. If it is less than, type 'less' and if it is the number type 'equal'.\n")
while numGuess != True:
	ans = input("Is " + str(guess) + " your number?\n")
	if ans == "greater":
		if upper == 0:
			guess *= 2
		else:
			lower = guess
			guess = int((lower + upper) / 2)
	elif ans == "less":
		if upper == 0:
			lower = int(guess / 2)
			
		upper = guess
		guess = int((lower + upper) / 2)
	elif ans == "equal":
		numGuess = True
		print("I guessed it! your number is " + str(guess) + "!")
	else:
		print("You did it wrong. Guess again.")
		time.sleep(5)

		
