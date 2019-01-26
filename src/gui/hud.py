from core.game import *

class Hud:

	def __init__(self):
		self.__hp = [3, 3]
		self.__shield = [10, 10]
		self.__heat = [0, 0]

	def draw(self):
		pass

	def update(self, dt):
		players = get_game_instance().get_screen().get_scene().get_players()
		self.__hp = [player.get_hp() for player in players]
		self.__shield = [player.get_shield() for player in players]
		self.__heat = [player.get_head() for player in players]
