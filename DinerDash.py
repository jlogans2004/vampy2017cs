import random
import time

names = ["Aaron", "Bobbb", "Camper", "Duulan", "Enoooch", "Films", "Geooof", "Hacker", "Indigo", "Jacksfilms", "Joj", "Jodge", "Kyle", "Leroy", "Leonard Skynerd", "Madam Zostra", "Noot", "Othello", "Pigeon", "Quincy", "Ryan", "Stuaaaart", "Toddddd", "Undying", "Victoria", "Wesley", "Xavier", "Yavii", "Zavier"]
Q = []
for name in random.sample(names, 3):
	joining = random.choice(names)
	Q.append(joining)
	print("{0} is joining!".format(joining))
hour = 1
print("It is {0} o'clock, and there are {1} people at the diner.".format(hour, len(Q)))
while len(Q) > 0:
	time.sleep(0.0625)
	for i in range(random.randint(1, 1500)):
		if random.uniform(0, 1) < 1:
			joining = random.choice(names)
			Q.append(joining)
			print("{0} is joining!".format(joining))
		elif len(Q) > 0:
			leaving = Q.pop(0)
			print("{0} is leaving!".format(leaving))
	hour += 1
	print("It is {0} o'clock, and there are {1} people at the diner.".format(hour, len(Q)))
print("Closing up shop!")
			
