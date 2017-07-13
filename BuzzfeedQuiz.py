A = 0
B = 0
C = 0
D = 0
print("Buzzfeed will guess your age! Let's see how lit you are, fam! (For middle schoolers to college only)\nBy Logan Stewart")
answer = input("Question #1: What is your favorite subject in school?\nA. Math. It's fun.\nB. Nothing. School is for chumps.\nC. Lunch. I get to hang out with my friends.\nD. Why are you asking me this? I'm in the middle of writing a research paper. (Write A B C or D for the answer)\n")
if answer == "A":
	A = A + 1
elif answer == "B":
	B = B + 1
elif answer == "C":
	C = C + 1
elif answer == "D":
	D = D + 1
else:
	print("You did it wrong. Try again.")
answer = input("Question #2: What is your favorite food? \nA. Pizza\nB. Nothing. This quiz is stupid.\nC. Starbucks. I'm so not a normie.\nD. Ramen. I've gotten used to it.\n")

if answer == "A":
	A = A + 1
elif answer == "B":
	B = B + 1
elif answer == "C":
	C = C + 1
elif answer == "D":
	D = D + 1
else:
	print("You did it wrong. Try again.")
answer = input("Question #3: What is the one thing you can't live without?\nA. My video games.\nB. Nothing.\nC. My Unicorn Frappicino from Starbucks\nD. Money\n")
if answer == "A":
	A = A + 1
elif answer == "B":
	B = B + 1
elif answer == "C":
	C = C + 1
elif answer == "D":
	D = D + 1
else:
	print("You did it wrong. Try again.")
answer = input("Question #4: What's your favorite game?\nA. Magic the Gathering\nB. Punching people in the face.\nC. The Starbucks Game (Actual thing, we had a board game project and a group made it)\nD. The 'try to find a job' game. It's the hardest out there.\n")
if answer == "A":
	A = A + 1
elif answer == "B":
	B = B + 1
elif answer == "C":
	C = C + 1
elif answer == "D":
	D = D + 1
elif answer == "joj":
	print("boom easter egg u win\nxddddddddddddddddddddddddddd")
else:
	print("You did it wrong. Try again.")


if A == 4:
	print("You are probably a 13 year old nerd in middle school.")
elif A == 3 and B == 1 or A == 2 and B == 2 or A == 1 and B == 3:
	print("You are probably a jock in middle school.")
elif B == 4:
	print("You are a high school jock.")
elif B == 3 and C == 1 or B == 2 and C == 2 or B == 1 and C == 3:
	print("You are a high school girl.")
elif C == 4:
	print("You are a high school normie.")
elif A + B + C + D == 3:
	print("Congrats u did right good job")
elif D == 4:
	print("You are any college student")
elif (A == 1 and B == 1 and C == 1 and D == 1) or (A == 2 and B == 1 and C == 1) or (A == 2 and C == 1 and D == 1) or (A == 2 and B == 1 and D == 1) or (A == 1 and B == 2 and D == 1) or (B == 2 and C == 1 and D == 1) or (A == 1 and B == 2 and C == 1) or (B == 1 and C == 2 and D == 1) or (A == 1 and C == 2 and D == 1) or (A == 1 and B == 1 and C == 2) or (B == 1 and C == 1 and D == 2) or (A == 1 and C == 1 and D == 2) or (A == 1 and B == 1 and D == 2):
	print("You are probably in high school.")
elif C == 3 and D == 1 or C == 2 and D == 2 or D == 3 and C == 1:
	print("You are an early college girl.")
elif D == 3 and A == 1 or A == 2 and D == 2 or A == 3 and D == 1:
	print("You are a college age nerd.")

