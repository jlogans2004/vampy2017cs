import pygame
import time
import random
ScreenSize = (640, 480)
colorBack = (255, 255, 255)
colorSquare = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption("Retro Pong!")
square = pygame.Rect(320-25, 240-25, 50, 50)
directionX = 1
directionY = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			directionX *= 2
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			directionX /= 2
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			if directionY >= 100:
				directionY = 50
			elif directionY == 0:
				directionY = 1
			else:
				directionY /= 2
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			if directionY >= 100:
				directionY = 50
			elif directionY == 0:
				directionY = 1
			else:
				directionY *= 2		
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
			colorBack = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			colorSquare = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	time.sleep(1/60)
	screen.fill(colorBack)
	pygame.draw.rect(screen, colorSquare, square)
	pygame.display.flip()
	square = square.move(directionX, directionY)
	if square.x + square.w >= ScreenSize[0]:
		directionX = -abs(directionX)
	elif square.x <= 0:
		directionX = abs(directionX)
	if square.y <= 0:
		directionY = abs(directionY)
	elif square.y + square.h >= ScreenSize[1]:
		directionY = -abs(directionY)
