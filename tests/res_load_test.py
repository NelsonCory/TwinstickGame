from core.resource_manager import *

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catx = 10
caty = 10
direction = 'right'

rm = ResourceManager(sys.argv[0])

while True: # the main game loop
	DISPLAYSURF.fill((0, 0, 0))

	for t_id in range(rm.get_num_tiles()):
		for layer in range(rm.get_tile_layers(t_id)):
			for frame in range(rm.get_tile_frames(t_id, layer)):
				layOffset = 0
				if layer == 1:
					layOffset = 64
				DISPLAYSURF.blit(rm.get_tile(t_id, layer, frame), ((layer+frame)*64+layOffset, t_id*64))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)
