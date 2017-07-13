import pygame
import random
import time

width = 1280
height = 960
size = (width, height)
black = (0, 0, 0)
white = (255, 255, 255)
chance = float(input("How likely are random squares to be alive at first? (eg. 0.7 or 0 or 1): "))
delay = float(input("How long (in seconds) would you like to wait for each loop? (eg 0.1 or 7 or 0): "))
grid = []
for i in range(960):
	grid.append([])
	for j in range(1280):
		if random.uniform(0, 1) < chance:
			grid[i].append(1)
		else:
			grid[i].append(0)
print(grid)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Conway's Game of Life")

genx = []
for i in range(960):
	genx.append([])
	for j in range(1280):
		genx[i].append(0)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	for i in range(960):
		for j in range(1280):
			xpos = j*10
			ypos = i*10
			cell = pygame.Rect(xpos, ypos, 10, 10)
			if grid[i][j] == 1:
				pygame.draw.rect(screen, black, cell)
			else:
				pygame.draw.rect(screen, white, cell)
	pygame.display.flip()
	pygame.display.update()
	time.sleep(delay)
	for i in range(960):
		for j in range(1280):
			N = 0
			above = (i-1) % 960
			below = (i + 1) % 960
			left = (j-1) % 1280
			right = (j + 1) % 1280
			N += grid[above][left]
			N += grid[above][j]
			N += grid[above][right]
			N += grid[i][left]
			N += grid[i][right]
			N += grid[below][left]
			N += grid[below][j]
			N += grid[below][right]
			genx[i].append(grid[i][j])
			if N < 2 or N > 3:
				genx[i][j] = 0
			elif N == 3:
				genx[i][j] = 1
			
	grid, genx = genx, grid
