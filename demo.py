
#for x in range(1000):
#	print("Hello, "*x*x*x*x)

friends = ["Bill" , "Tom" , "Joj" , "Jaf" , "ggg"]

g = input("Find who?\n")

for person in friends:
	if(person == g):
		print("FOUND")
		quit()

print("Not found")
