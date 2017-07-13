# Weird Unbeatable AI Pong
# by the VAMPY 2017 CS Class
import pygame
import time
import random
import numpy
import sounddevice
import math

# sounds
SOUND_FS   = 48000
WALL_SOUND = numpy.zeros(int(SOUND_FS * 0.096))
PADD_SOUND = numpy.zeros(int(SOUND_FS * 0.096))
PONT_SOUND = numpy.zeros(int(SOUND_FS * 0.257))
for x in range(len(WALL_SOUND)):
	WALL_SOUND[x]  = math.sin(2*math.pi * 226*x/SOUND_FS)
	if WALL_SOUND[x] > 0:
		WALL_SOUND[x] = 1
	else:
		WALL_SOUND[x] = -1
		
for x in range(len(PADD_SOUND)):
	PADD_SOUND[x]  = math.sin(2*math.pi * 459*x/SOUND_FS)
	if PADD_SOUND[x] > 0:
		PADD_SOUND[x] = 1
	else:
		PADD_SOUND[x] = -1
		
for x in range(len(PONT_SOUND)):
	PONT_SOUND[x]  = math.sin(2*math.pi * 490*x/SOUND_FS)
	if PONT_SOUND[x] > 0:
		PONT_SOUND[x] = 1
	else:
		PONT_SOUND[x] = -1


# some helper constants for later
WIDTH   = 1280
HEIGHT  = 720
SIZE    = (WIDTH, HEIGHT)
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
GREY    = (128, 128, 128)
YELLOW  = (255, 255, 0)
WAITING = 1
PLAYING = 2

# start the game engine, open a window, and set the window title
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.toggle_fullscreen()
pygame.display.set_caption("Let's Play Pong!")

# state
state      = WAITING
state_time = time.time()

# speeds
speed_lpaddle = 0
speed_rpaddle = 0
speed_ball_x  = 0
speed_ball_y  = 0

# scores
score_left  = 0
score_right = 0

# rects
# paddles are 5% of the width of the screen wide, and five times that tall
# the ball is just as wide as the paddle
paddle_w     = 0.05*WIDTH
paddle_h     = 5*paddle_w
ball_w       = paddle_w
ball_h       = ball_w
rect_lpaddle = pygame.Rect(paddle_w,             HEIGHT/2 - paddle_h/2, paddle_w, paddle_h)
rect_rpaddle = pygame.Rect(WIDTH - 2*paddle_w,   HEIGHT/2 - paddle_h/2, paddle_w, paddle_h)
rect_ball    = pygame.Rect(WIDTH/2 - ball_w/2,   HEIGHT/2 - ball_h/2,   ball_w,   ball_h)

# the main loop
while True:

	# handle all events pygame has collected since the last loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
			
		#left paddle controls
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
			speed_lpaddle = -6
		elif event.type == pygame.KEYUP   and event.key == pygame.K_w:
			speed_lpaddle = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			speed_lpaddle = 6
		elif event.type == pygame.KEYUP   and event.key == pygame.K_s:
			speed_lpaddle = 0
		
		# right paddle controls
		#elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
		#	speed_rpaddle = -3
		#elif event.type == pygame.KEYUP   and event.key == pygame.K_UP:
		#	speed_rpaddle = 0
		#elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
		#	speed_rpaddle = 3
		#elif event.type == pygame.KEYUP   and event.key == pygame.K_DOWN:
		#	speed_rpaddle = 0
	
	# AI logic (right paddle)
	sure_mid = HEIGHT / 2
	if speed_ball_x > 0:
		id_rect = pygame.Rect(rect_ball.x, rect_ball.y, rect_ball.w, rect_ball.h)
		variable_x = speed_ball_x
		variable_y = speed_ball_y
		while id_rect.x < rect_rpaddle.x:
			id_rect.move_ip(variable_x, variable_y)
			if id_rect.y <= 0:
				id_rect.y  = 0
				variable_y = abs(variable_y)
			elif id_rect.y + id_rect.h >= HEIGHT:
				id_rect.y  = HEIGHT - id_rect.h
				variable_y = -abs(variable_y)
			
		# after the while: id_rect.x >= rect_rpaddle.x
		sure_mid = id_rect.y + id_rect.h/2
		
	padd_mid = rect_rpaddle.y + rect_rpaddle.h/2
	if sure_mid - padd_mid > 5:
		speed_rpaddle = 3
	elif sure_mid - padd_mid < -5:
		speed_rpaddle = -3
	else:
		speed_rpaddle = 0
	
	# AI logic (left paddle)
	#sure_mid = HEIGHT / 2
	#if speed_ball_x < 0:
	#	id_rect = pygame.Rect(rect_ball.x, rect_ball.y, rect_ball.w, rect_ball.h)
	#	variable_x = speed_ball_x
	#	variable_y = speed_ball_y
	#	while id_rect.x > rect_lpaddle.x:
	#		id_rect.move_ip(variable_x, variable_y)
	#		if id_rect.y <= 0:
	#			id_rect.y  = 0
	#			variable_y = abs(variable_y)
	#		elif id_rect.y + id_rect.h >= HEIGHT:
	#			id_rect.y  = HEIGHT - id_rect.h
	#			variable_y = -abs(variable_y)
	#		
	#	# after the while: id_rect.x >= rect_rpaddle.x
	#	sure_mid = id_rect.y + id_rect.h/2
	#	
	#padd_mid = rect_lpaddle.y + rect_lpaddle.h/2
	#if sure_mid - padd_mid > 5:
	#	speed_lpaddle = 3
	#elif sure_mid - padd_mid < -5:
	#	speed_lpaddle = -3
	#else:
	#	speed_lpaddle = 0
	#
	# motion logic
	rect_lpaddle.move_ip(0, speed_lpaddle)
	rect_rpaddle.move_ip(0, speed_rpaddle)
	if state == PLAYING:
		rect_ball.move_ip(speed_ball_x, speed_ball_y)
	elif state == WAITING:
		if time.time() - state_time >= 1:
			state        = PLAYING
			state_time   = time.time()
			speed_ball_x = 2*random.randint(0, 1) - 1
			speed_ball_y = 0 #random.randint(-5, 5)
	
	# wall bouncing
	if rect_ball.y <= 0:
		rect_ball.y  = 0
		speed_ball_y = abs(speed_ball_y)
		sounddevice.play(WALL_SOUND, SOUND_FS)
	elif rect_ball.y + rect_ball.h >= HEIGHT:
		rect_ball.y  = HEIGHT - rect_ball.h
		speed_ball_y = -abs(speed_ball_y)
		sounddevice.play(WALL_SOUND, SOUND_FS)
	
	# paddle bouncing
	if rect_lpaddle.x <= rect_ball.x and rect_ball.x <= rect_lpaddle.x+rect_lpaddle.w:
		if rect_lpaddle.y-rect_ball.h <= rect_ball.y and rect_ball.y <= rect_lpaddle.y+rect_lpaddle.h:
			rect_ball.x  = rect_lpaddle.x + rect_lpaddle.w
			speed_ball_x = abs(speed_ball_x)+random.uniform(0, 2)
			speed_ball_y = (abs(speed_ball_y)+1)*(2*random.randint(0, 1) - 1) #random.randint(-5, 5)
			sounddevice.play(PADD_SOUND, SOUND_FS)
			
	elif rect_rpaddle.x <= rect_ball.x+rect_ball.w and rect_ball.x+rect_ball.w <= rect_rpaddle.x+rect_rpaddle.w:
		if rect_rpaddle.y-rect_ball.h <= rect_ball.y and rect_ball.y <= rect_rpaddle.y+rect_rpaddle.h:
			rect_ball.x  = rect_rpaddle.x - rect_ball.w
			speed_ball_x = -abs(speed_ball_x)-random.uniform(0,2)
			speed_ball_y = (abs(speed_ball_y)+1)*(2*random.uniform(0, 1) - 1) #random.randint(-5, 5)
			sounddevice.play(PADD_SOUND, SOUND_FS)
	
	# scoring
	if rect_ball.x + rect_ball.w < 0 or rect_ball.x > WIDTH:
		if rect_ball.x + rect_ball.w < 0:
			score_right += 1
		else:
			score_left += 1
			
		state        = WAITING
		state_time   = time.time()
		rect_ball.x  = WIDTH/2  - rect_ball.w/2
		rect_ball.y  = HEIGHT/2 - rect_ball.h/2
		speed_ball_x = 0 
		speed_ball_y = 0
		sounddevice.play(PONT_SOUND, SOUND_FS)
	
	# erase the board, draw a box, and flip to the new drawing
	screen.fill(BLACK)
	for i in range(score_left):
		pip = pygame.Rect(rect_ball.w + i*(2+rect_ball.w/2), rect_ball.w, rect_ball.w/2, rect_ball.w)
		pygame.draw.rect(screen, YELLOW, pip)
		
	for i in range(score_right):
		pip = pygame.Rect(WIDTH-rect_ball.w - i*(2+rect_ball.w/2), rect_ball.w, rect_ball.w/2, rect_ball.w)
		pygame.draw.rect(screen, YELLOW, pip)
		
	pygame.draw.rect(screen, WHITE, rect_lpaddle)
	pygame.draw.rect(screen, WHITE, rect_rpaddle)
	pygame.draw.rect(screen, WHITE, rect_ball)
	pygame.display.flip()

