from core.game import *

class Hud:

	def __init__(self):
		self.__hp = [3, 3]
		self.__shield = [10, 10]
		self.__heat = [0, 0]

	def draw(self):
		surface = get_game_instance().get_screen().get_surface()
		rm = ResourceManager.get_instance()

		surface.blit(rm.get_hud(1), (100, 656))
		surface.blit(rm.get_hud(0), (1153-100, 656))

		for h1 in range(self.__hp[0]):
			x = 164
			y = 680
			pygame.draw.rect(surface, (0, 40, 150), (x+((4+14)*h1), y, 14, 9))

		for h1 in range(self.__hp[0]):
			x = 1153-100+10
			y = 680
			pygame.draw.rect(surface, (0, 40, 150), (x+((4+14)*h1), y, 14, 9))

	def update(self, dt):
		players = get_game_instance().get_screen().get_scene().get_players()
		self.__hp = [player.get_hp() for player in players]
		self.__shield = [player.get_shield() for player in players]
		self.__heat = [player.get_heat() for player in players]
