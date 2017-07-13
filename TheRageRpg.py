import pygame
import random
import time
import threading
import math
stats = {
"health": 1,
"speed": 1,
"attack": 1,
"defense": 1,
'level': 1,
'xp': 0 
}
pygame.init()
inventory = {}
Dead = False
Restart = True
def dealtDamage(attack, defense):
	damageDealtSub = round(attack - math.sqrt(defense**1.5))
	if damageDealtSub < 1:
		damageDealt = 1
	else:
		damageDealt = damageDealtSub
	return damageDealt
choice = ""
enemy_stats = {
						'health': 1,
						'speed': 1,
						'attack': 0,
						'defense': 1,
						'xp': 3
						}

stats = {
'health': 1,
						'speed': 1,
						'attack': 0,
						'defense': 1,
						'xp': 3
						}

				
def sound():
	pygame.mixer.music.load("/home/vampy/Downloads/darude.ogg")
	pygame.mixer.music.play(-1)
class_choice = int(input("Yo what's going on? You're about to play TheRageRPG, and it's gonna be lit. You can choose 5 classes: type 1 for Theif, type 2 for Warrior, type 3 for Cleric, type 4 for Mage, or type 5 for Berzerker\n"))
if class_choice == 1:
	stats["health"] = 3
	stats["speed"] = 10
	stats["attack"] = 6
	stats['defense'] = 2
	print("Your stats are:\nHealth: {0}\nSpeed: {1}\nAttack: {2}\nDefense: {3}".format(stats["health"], stats["speed"], stats["attack"], stats["defense"]))
elif class_choice == 2:
	stats["health"] = 7
	stats["speed"] = 2
	stats["attack"] = 4
	stats['defense'] = 10
	print("Your stats are:\nHealth: {0}\nSpeed: {1}\nAttack: {2}\nDefense: {3}".format(stats["health"], stats["speed"], stats["attack"], stats["defense"]))
elif class_choice == 3:
	stats["health"] = 12
	stats["speed"] = 2
	stats["attack"] = 2
	stats['defense'] = 2
	print("Your stats are:\nHealth: {0}\nSpeed: {1}\nAttack: {2}\nDefense: {3}".format(stats["health"], stats["speed"], stats["attack"], stats["defense"]))
elif class_choice == 4:
	stats["health"] = 8
	stats["speed"] = 8
	stats["attack"] = 8
	stats['defense'] = 8
	print("Your stats are:\nHealth: {0}\nSpeed: {1}\nAttack: {2}\nDefense: {3}".format(stats["health"], stats["speed"], stats["attack"], stats["defense"]))
elif class_choice == 5:
	stats["health"] = 1
	stats["speed"] = 20
	stats["attack"] = 20
	stats['defense'] = 0
	print("Your stats are:\nHealth: {0}\nSpeed: {1}\nAttack: {2}\nDefense: {3}".format(stats["health"], stats["speed"], stats["attack"], stats["defense"]))
def DeathLoop():
	while True:
			if stats["health"] <= 0:
				Dead = True
				print("You died...")
				exit()
def main():
	loop0 = True
	time.sleep(1)
	enemy_stats = {
	'health': 1,
	'speed': 2,
	'attack': 1,
	'defense': 1,
	'xp': 3
	}
	choice = input("You are walking around in the forest one day when a snake pops up out of the grass. You can 'Fight' it, or try to 'run away'.")
	while loop0 == True:
		if choice.capitalize() == "Fight":
			loop1 = True
			loop0 = False
			while loop1 == True:
				choice = input("Would you like to use a normal 'attack', 'block' or use your 'special'?")
				if choice.capitalize() == 'Attack':
					enemy_stats['health'] -= dealtDamage(stats['attack'], enemy_stats['defense'])
					print("Your enemy took {0} damage. It is now at {1} health.".format(dealtDamage(stats['attack'], enemy_stats['defense']), enemy_stats['health']))
					if enemy_stats['health'] <= 0:
							print("You beat the monster.")
							break				
				elif choice.capitalize() == 'Block':
					print("You blocked your opponent's attack. Nothing happens.")
				elif choice.capitalize() == 'Special':
					if class_choice	== 1:
						print("You steal the opponent's items. Their stats are reset to 0.")
						enemy_stats = {
						'health': 1,
						'speed': 1,
						'attack': 0,
						'defense': 1,
						'xp': 3
						}
					elif class_choice == 2:
						print('You bludgeon your opponent with your sheild. They take 5 damage.')
						enemy_stats['health'] -= 5
						if enemy_stats['health'] <= 0:
							print("You beat the monster.")
							break
					elif class_choice == 3:
						print('You heal yourself. You gain 5 life.')
						stats['health'] += 5
					elif class_choice == 4:
						print("You attack the creature with a fire attack. It burns the creature's armor and deals 2 damage.")
						enemy_stats['defense'] = 0
						enemy_stats['health'] -= 2
						if enemy_stats['health'] <= 0:
							print("You beat the monster.")
							break
					else:
						print("You attack the creature with all-out force. It takes 10 damage.")
						enemy_stats['health'] -= 10
						if enemy_stats['health'] <= 0:
							print("You beat the monster.")
							break
		elif choice.capitalize() == "Run away":
			if random.uniform(0,1) * math.sqrt(math.log2(stats[speed])) > 0.5:
				print("You ran away!")
				run = True
				loop0 = False
			else:
				stats['health'] -= dealtDamage(enemy_stats['attack'], stats['defense'])
				print("You couldn't run away. Try again. You take {0} damage. You are at {1} health.".format(dealtDamage(enemy_stats['attack'], stats['defense']), stats['health']))
				choice = input("Do you want to 'Fight' or try to 'run away' again?")
		dealtDamage(enemy_stats['attack'], stats['defense'])		
		print("You took {0} damage when the creature attacked you. You are at {1} health.".format(dealtDamage(enemy_stats['attack'], stats['defense']), stats['health']))
	enemy_stats = {
	'health': 10,
	'speed': 4,
	'attack': 3,
	'defense': 0,
	'xp': 10
	}
	choice = input("After beating the monster, you stumble upon a cave. As soon as you walk in, a bear pummles you from behind.('Fight' or 'Run away' again)\n")
	while loop0 == True:
		if choice.capitalize() == "Fight":
			loop1 = True
			loop0 = False
			while loop1 == True:
				choice = input("Would you like to use a normal 'attack', 'block' or use your 'special'?")
				if choice.capitalize() == 'Attack':
					enemy_stats['health'] -= dealtDamage(stats['attack'], enemy_stats['defense'])
					print("Your enemy took {0} damage. It is now at {1} health.".format(dealtDamage(stats['attack'], enemy_stats['defense'], enemy_stats['health'])))
					if enemy_stats['health'] <= 0:
							print("You beat the monster.")
							loop1 = False	
				elif choice.capitalize() == 'Block':
					print("You blocked your opponent's attack. Nothing happens.")
				elif choice.capitalize() == 'Special':
					if class_choice	== 1:
						print("You steal the opponent's items. Their stats are reset to 0.")
						enemy_stats = {
						'health': 1,
						'speed': 1,
						'attack': 0,
						'defense': 1,
						'xp': 3
						}
					elif class_choice == 2:
						print('You bludgeon your opponent with your sheild. They take 5 damage.')
						enemy_stats['health'] -= 5
						if enemy_stats['health'] <= 0:
							print("You beat the monster.")
							loop1 = False
						
					elif class_choice == 3:
						print('You heal yourself. You gain 5 life.')
						stats['health'] += 5
					elif class_choice == 4:
						print("You attack the creature with a fire attack. It burns the creature's armor and deals 2 damage.")
						enemy_stats['defense'] = 0
						enemy_stats['health'] -= 2
						if enemy_stats['health'] <= 0:
							print("You beat the monster.")
							loop1 = False		
					else:
						print("You attack the creature with all-out force. It takes 10 damage.")
						enemy_stats['health'] -= 10
						if enemy_stats['health'] <= 0:
							print("You beat the monster.")
							loop1 = False
		elif choice.capitalize() == "Run away":
			if random.uniform(0,1) * math.sqrt(math.log2(stats[speed])) > 0.5:
				print("You ran away!")
				run = True
				loop1 = False
				loop0 = False
			else:
				stats['health'] -= dealtDamage(enemy_stats['attack'], stats['defense'])
				print("You couldn't run away. Try again. You take {0} damage. You are at {1} health.".format(dealtDamage(enemy_stats['attack'], stats['defense']), stats['health']))
				choice = input("Do you want to 'Fight' or try to 'run away' again?")
		dealtDamage(enemy_stats['attack'], stats['defense'])		
		print("You took {0} damage when the creature attacked you. You are at {1} health.".format(dealtDamage(enemy_stats['attack'], stats['defense']), stats['health']))
	enemy_stats = {
	'health': 12,
	'speed': 5,
	'attack': 7,
	'defense': 12,
	'xp': 10
	}
	choice = input("After you beat the bear, you find a passageway. You walk down the pathway and find a door. You go inside and get jumped by a lionlike creature. Same thing as before, 'fight' or 'run away'")
	while loop0 == True:
			if choice.capitalize() == "Fight":
				loop1 = True
				loop0 = False
				while loop1 == True:
					choice = input("Would you like to use a normal 'attack', 'block' or use your 'special'?")
					if choice.capitalize() == 'Attack':
						enemy_stats['health'] -= dealtDamage(stats['attack'], enemy_stats['defense'])
						print("Your enemy took {0} damage. It is now at {1} health.".format(dealtDamage(stats['attack'], enemy_stats['defense'], enemy_stats['health'])))
						if enemy_stats['health'] <= 0:
								print("You beat the monster.")
								break				
					elif choice.capitalize() == 'Block':
						print("You blocked your opponent's attack. Nothing happens.")
					elif choice.capitalize() == 'Special':
						if class_choice	== 1:
							print("You steal the opponent's items. Their stats are reset to 0.")
							enemy_stats = {
							'health': 1,
							'speed': 1,
							'attack': 0,
							'defense': 1,
							'xp': 3
							}
						elif class_choice == 2:
							print('You bludgeon your opponent with your sheild. They take 5 damage.')
							enemy_stats['health'] -= 5
							if enemy_stats['health'] <= 0:
								print("You beat the monster.")
								break
						elif class_choice == 3:
							print('You heal yourself. You gain 5 life.')
							stats['health'] += 5
						elif class_choice == 4:
							print("You attack the creature with a fire attack. It burns the creature's armor and deals 2 damage.")
							enemy_stats['defense'] = 0
							enemy_stats['health'] -= 2
							if enemy_stats['health'] <= 0:
								print("You beat the monster.")
								break
						else:
							print("You attack the creature with all-out force. It takes 10 damage.")
							enemy_stats['health'] -= 10
							if enemy_stats['health'] <= 0:
								print("You beat the monster.")
								break
			elif choice.capitalize() == "Run away":
				if random.uniform(0,1) * math.sqrt(math.log2(stats[speed])) > 0.5:
					print("You ran away!")
					run = True
					loop0 = False
				else:
					stats['health'] -= dealtDamage(enemy_stats['attack'], stats['defense'])
					print("You couldn't run away. Try again. You take {0} damage. You are at {1} health.".format(dealtDamage(enemy_stats['attack'], stats['defense']), stats['health']))
					choice = input("Do you want to 'Fight' or try to 'run away' again?")
			dealtDamage(enemy_stats['attack'], stats['defense'])		
			print("You took {0} damage when the creature attacked you. You are at {1} health.".format(dealtDamage(enemy_stats['attack'], stats['defense']), stats['health']))
t1 = threading.Thread(target=DeathLoop)
t2 = threading.Thread(target=main)
t3 = threading.Thread(target=sound)
t3.start()
t2.start()
t1.start()
t1.join()
t2.join()
t3.join()
