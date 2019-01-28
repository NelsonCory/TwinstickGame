from . scene import *
from core.event_manager import *
from entity.player import *
from controller.player_controller import *
from entity.bullet import *
from gui.hud import *
from map.tile_map import *
import sys

class World(Scene):

	def __init__(self):
		super(World, self).__init__()
		self.__bullets = []
		self.__tilemap = TileMap()
		self.__tilemap.load_map(os.path.dirname(sys.argv[0]) + "/res/maps/map.dat")
		self.__players = [Player(0), Player(1)]
		self.__hud = Hud()
		self.__AlphaInput = PlayerController(0)
		self.__BetaInput = PlayerController(1)
		event_mgr = EventManager.get_instance()
		event_mgr.subscribe("fire", self.on_fire)
		event_mgr.subscribe("damage", self.on_damage)
		event_mgr.subscribe("clean", self.remove_dead_bullets)


	def draw(self):
		self.__game_screen = get_game_instance().get_screen()
		self.__tilemap.draw(self.__game_screen)

		for bullet in self.__bullets:
			bullet.draw()
		for player in self.__players:
			player.draw()
		self.__hud.draw()

	def update(self, dt):
		self.__tilemap.update(dt)
		self.__AlphaInput.update(dt)
		self.__BetaInput.update(dt)
		for bullet in self.__bullets:
			bullet.update(dt)
		for player in self.__players:
			player.update(dt)
		self.__hud.update(dt)

	def clean(self):
		super(World, self).clean()
		event_mgr = EventManager.get_instance()
		event_mgr.unsubscribe("fire", self.on_fire)
		event_mgr.unsubscribe("damage", self.on_damage)
		event_mgr.unsubscribe("clean", self.remove_dead_bullets)
		for player in self.__players:
			player.clean()

	def get_players(self):
		return self.__players

	def on_fire(self, player_id):
		rotx, roty = self.__players[player_id].get_rotation()
		x, y = self.__players[player_id].get_position()
		self.__bullets.append(Bullet(x, y, rotx, roty, player_id))

	def on_damage(self, player_id):
		player = self.__players[player_id]
		player.set_hp(player.get_hp() - 1)
		if player.get_hp() == 0:
			EventManager.get_instance().send("death", player_id)
			print("Killed player")

	def remove_dead_bullets(self, _):
		self.__bullets = list(filter(lambda x: not(x.is_dead()), self.__bullets))
