from . scene import *
from core.event_manager import *
from entity.player import *
from controller.player_controller import *
from entity.bullet import *
from gui.hud import *
from map.tile_map import *

class World(Scene):

	def __init__(self):
		super(World, self).__init__()
		self.__bullets = []
		self.__tilemap = TileMap()
		self.__players = [Player(0), Player(1)]
		self.__hud = Hud()
		self.__AlphaInput = PlayerController(0)
		self.__BetaInput = PlayerController(1)
		EventManager.get_instance().subscribe('fire', self.on_fire)


	def draw(self):
		self.__game_screen = get_game_instance().get_screen()
		self.__tilemap.draw(self.__game_screen)

		for bullet in self.__bullets:
			bullet.draw()
		for player in self.__players:
			player.draw()
		self.__hud.draw()

	def update(self, dt):
		#self.__tilemap.update(dt)
		self.__AlphaInput.update(dt)
		self.__BetaInput.update(dt)
		for bullet in self.__bullets:
			bullet.update(dt)
		for player in self.__players:
			player.update(dt)
		self.__hud.update(dt)

	def get_players(self):
		return self.__players

	def on_fire(self, _):
		self.__bullets.append(Bullet(640, 360, 2, None))


