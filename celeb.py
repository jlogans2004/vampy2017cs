import time
connections = {}
connections["Joj"] = []
connections["Emily"] = ["Joj", "Jeph", "Jeff"]
connections["Jeph"] = ["Joj", "Geoff"]
connections["Jeff"] = ["Joj", "Judge"]
connections["Geoff"] = ["Joj", "Jebb"]
connections["Jebb"] = ["Joj", "Emily"]
connections["Judge"] = ["Joj", "Judy"]
connections["Jodge"] = ["Joj", "Jebb", "Stephan", "Judy"]
connections["Judy"] = ["Joj", "Judge"]
connections["Stephan"] = ["Joj", "Jodge"]
names = ["Emily", "Jeph", "Jeff", "Joj", "Geoff", "Jebb", "Judge", "Jodge", "Judy", "Stephan"]
print("Finding the celbrity candidate...")
time.sleep(1)
#time.sleep is for "realism"
candidate = names[0]
for i in range(1, len(names)):
	if names[i] in connections[candidate]:
		candidate = names[i]
print("Our best candidate is {0}".format(candidate))
time.sleep(1)
print("Verifying candidate...")
time.sleep(1)
for name in names:
	if name != candidate:
		if name in connections[candidate]:
			print("The candidate is a lie, they know somebody!")
			exit()
		elif candidate not in connections[name]:
			print("The candidate is a lie, they are not known by somebody!")
			exit()
print("We made it to the end, the celeb is a real deal!")
		
