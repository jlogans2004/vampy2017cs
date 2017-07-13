id = 0
tops = ["Eezy", "Vecteezy", "ACM", "VAMPY", "Red Tank Top", "Green Tank Top", "Black Tank Top"]
bottoms =["Khakis", "Black Skinny Jeans", "Blue Skinny Jeans", "Blue Skinny Jeans", "Green Skinny Jeans", "Light Blue Dress Pants", "Sweatpant", "Swim Trunks"]
shoes = ["None", "Vans", "High Tops"]
headgear = ["none","Brown Beanie", "Grey Beanie", "Red Bandana", "White Bandana", "Cactus Bandana", "Shark Fat Quarter"]
socks = ["none", "Pink", "Salmon", "Red", "Blue", "Dark Blue", "Light Blue", "Blue/White Stripes", "Orange"]
#DEAD = ["1","2","3","4","%","DIAASDFGFDSDFRE"]
#idk = ["Locffwef","covfefe","DQWCWCFEC","CWFCFFCEWFWCWEF","CWWECECFCWFFWFFWCWFFCWFWCFFW"]
#wow = ["yep", "nnofisjeeeejfiejoefisijefoeijsoijefojiseoijfosiejfsoeifjsoeijf", "plzx fsf", "oooooooooooooooooooooooooooooo"]
pattern = "#{0}: Top={1}, Bottom{2}, Shoes={3}, Head={4}, Socks={5}"
for top in tops:
	for bottom in bottoms:
		for kicks in shoes:
			for headitem in headgear:
				for pair in socks:
					#for dead in DEAD:
						#for idont in idk:
							#for woww in wow:
								id += 1
								print(pattern.format(id, top, bottom, kicks, headitem, pair))
#Dead={6}, wow={7}, no={8}, dead, idont, woww
