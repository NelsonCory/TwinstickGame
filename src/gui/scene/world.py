from . scene import *
from core.event_manager import *
from entity.player import *
from entity.bullet import *
from gui.hud import *
from map.tile_map import *

class World(Scene):

	def __init__(self):
		super(World, self).__init__()
		self.__bullets = []
		self.__tilemap = TileMap()
		self.__players = [Player(), Player()]
		self.__hud = Hud()
		EventManager.get_instance().subscribe('fire', self.on_fire)

	def draw(self):
		self.__tilemap.draw()
		for bullet in self.__bullets:
			bullet.draw()
		for player in self.__players:
			player.draw()
		self.__hud.draw()

	def update(self, dt):
		self.__tilemap.update(dt)
		for bullet in self.__bullets:
			bullet.update(dt)
		for player in self.__players:
			player.update(dt)
		self.__hud.update(dt)

	def get_players(self):
		return self.__players

	def on_fire(self, _):
		self.__bullets.append(Bullet(640, 360, 2, None))
