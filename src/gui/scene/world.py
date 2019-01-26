from . scene import *
from entity.player import *
from gui.hud import *
from map.tile_map import *

class World(Scene):

	def __init__(self):
		super(World, self).__init__()
		self.__tilemap = TileMap()
		self.__players = [Player(), Player()]
		self.__hud = Hud()

	def draw(self):
		self.__tilemap.draw()
		for player in self.__players:
			player.draw()
		self.__hud.draw()

	def update(self, dt):
		self.__tilemap.update(dt)
		for player in self.__players:
			player.update(dt)
		self.__hud.update(dt)

	def get_players(self):
		return self.__players

	