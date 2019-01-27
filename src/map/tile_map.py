import pygame
from . tile import *
from core.game import *
from core.resource_manager import *


class TileMap:

	__instance = None

	def __init__(self):
		self.__chunk = [[Tile() for _ in range(22)] for _ in range(40)]

		self.__spawn_list = []

		self.__frame = 0
		self.__time = pygame.time.get_ticks()
		self.__ani_count = 0
		self.__ani_milli = 700

		self.init_map()
		TileMap.__instance = self

	@staticmethod
	def get_instance():
		return TileMap.__instance

	def init_map(self):
		for x in range(40):
			for y in range(22):
				self.__chunk[x][y].load_tile("0 0 0")

	def load_map(self, path):
		lines = [line.rstrip('\n') for line in open(path)]
		z = 0
		for x in range(40):
			for y in range(22):
				self.__chunk[x][y].load_tile(lines[z])
				z += 1
				if self.__chunk[x][y].get_spawn() > 0:
					self.__spawn_list.append((x, y, self.__chunk[x][y].get_spawn()))

	def save_map(self, path):
		f = open(path, "w")
		for x in range(40):
			for y in range(22):
				f.write(self.__chunk[x][y].save_tile())
		f.close()

	def draw(self,scrn):
		res = ResourceManager.get_instance()
		for x in range(40):
			for y in range(22):
				if res.get_tile_frames(self.__chunk[x][y].get_t_id(), 0) > 1:
					scrn.blit(res.get_tile(self.__chunk[x][y].get_t_id(), 0, self.__frame), (x*32, y*32))
				else:
					scrn.blit(res.get_tile(self.__chunk[x][y].get_t_id(), 0, 0), (x*32, y*32))

	def update(self, dt=0):
		self.__ani_time = pygame.time.get_ticks()
		if (self.__ani_time - self.__time) >= self.__ani_milli:
			self.__time = pygame.time.get_ticks()
			self.__frame += 1
			if self.__frame == 3:
				self.__frame = 0

	def get_tile(self, x, y):
		return self.__chunk[x][y]

	def set_tile(self, x, y, tile):
		self.__chunk[x][y] = tile

	def get_spawn_list(self):
		return self.__spawn_list
