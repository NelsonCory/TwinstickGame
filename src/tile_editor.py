from core.resource_manager import *
from map.tile_map import *
from map.tile import *

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption('tile editor')

direction = 'right'

rm = ResourceManager(sys.argv[0])

tm = TileMap()

currTile = Tile()

currTile.load_tile("0 0 0")

def onClick(tmx, tmy, ctile):

	global tm
	tm.set_tile(tmx, tmy, ctile)


while True: # the main game loop
	DISPLAYSURF.fill((0, 0, 0))

	tm.draw(DISPLAYSURF)

	mouse = pygame.mouse.get_pos()

	mx = mouse[0]
	my = mouse[1]
	tmx = mx // 32
	tmy = my // 32
	#print(str(tmx) + " " + str(tmy))

	pygame.draw.rect(DISPLAYSURF, (90, 0, 50), (tmx*32,tmy*32, 32, 32), 2)


	for event in pygame.event.get():
		#print("input the id:")
		if event.type == pygame.MOUSEBUTTONUP:
			onClick(tmx, tmy, currTile)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				print("input the id:")
				currTile.set_t_id(int(input()))
				print("Solid?")
				currTile.set_solid(int(input()))
				print("Spawn?")
				currTile.set_spawn(int(input()))

		if event.type == QUIT:
			tm.save_map("map.dat")
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)
