import pickle
cities = {}	

try:
	cities = pickle.load(open("cities.pickle", "rb"))
except:
	pass
city = input("What is the name of your city?").strip().title()
if city in cities:
	print("Your city is in the database. T")
else:
	print("Your city is not in the database yet.")
	cities[city] = []
	lrate = []
	for i in range(int(input("How many years of data would you like to input regarding the yearly number of prothetics needed?"))):
		lrate.append(int(input("Input a number prothetics needed in a past year:")))
	cities[city].append(lrate)
	frate = round(sum(lrate)/len(lrate))
	cities[city].append(frate)
	materials = int(input("How many prosthetics can currently be made with materials in your city?"))
	cities[city].append(materials)
	excess = round(materials - frate)
	cities[city].append(excess)
	for i in cities:
		if cities[i][3] < 0:
			print("You don't have enough materials here. We are sending matl's there.")
			cities[i][2] += abs(cities[i][3])
			excess = round(cities[i][2] - cities[i][1])
pickle.dump(cities, open("cities.pickle", "wb"))
print(cities[city])
