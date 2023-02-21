import pygame
import sys
import random

DISP_W = 800
DISP_H = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)


class Snake:
	def __init__(self):
		pass
	def draw(self):
	

class Food:
	pass


pygame.init()
screen = pygame.display.set_mode((DISP_W, DISP_H))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.flip()

