from core.game import *

class Hud:
	def __init__(self):
		players = get_game_instance().get_screen().get_scene().get_players()
		self.__hp = [player.get_hp() for player in players]
		self.__shield = [player.get_shield() for player in players]
		self.__heat = [player.get_head() for player in players]

	def draw(self):
		pass

	def update(self, dt):
		pass
