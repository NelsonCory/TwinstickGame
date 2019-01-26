from map.tile_map import *

class World(Scene):

	def __init__(self):
		super(World, self).__init__()
		self.__tilemap = TileMap()
		self.__players = [Player(), Player()]
