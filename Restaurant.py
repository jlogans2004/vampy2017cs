f = open("reciept.txt", "w")
print("Welcome to Covfefe and Diner!\n-----------------------------------------")
f.write("Welcome to Covfefe & Diner!\n-----------------------------------------\nThe Menu is\nCovfefe,\nPancake,\nMorris,\nand\nBeestiality.\n	")
print("The Menu is\nCovfefe,\nPancake,\nMorris,\nand\nBeestiality")
itemNum = int(input("How many items are being processed?"))
for i in range(0, itemNum):
	item = input("What is Item #" + str(i+1) + "?\n")
	if item == "Pancake":
		f.write("1 Pancake: $6.90")
	elif item == "Morris":
		f.write("1 Morris: $4.20")
	elif item == "Covfefe":
		f.write("1 Covfefe: "
