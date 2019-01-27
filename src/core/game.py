# Grant the ability to get the current game instance across the program
def get_game_instance():
	return Game.get_instance()

from . event_manager import *
from . resource_manager import *
from gui.screen import *
import pygame
import sys

class Game():

	RESOLUTION = (1280, 720)

	__instance = None

	@staticmethod
	def get_instance():
		return Game.__instance

	# Initialize pygame here
	def __init__(self, path):
		Game.__instance = self
		self.init_pygame()
		self.__event_manager = EventManager()
		self.__resource_manager = ResourceManager(path)
		self.__done = False
		self.__clock = pygame.time.Clock()
		self.__screen = Screen(Game.RESOLUTION)

		self.__event_manager.subscribe("on_start", self.on_start)

	def init_pygame(self):
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.mixer.init()
		pygame.init()
		pygame.mouse.set_visible(False) #CHECK ON MACHINE

	# Main loop, returns exit code
	def run(self):
		dt = 0
		# Main loop
		while not self.__done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN and (event.key == pygame.K_z or event.key == pygame.K_x):
					self.__event_manager.send('fire')

			self.__event_manager.dispatch()
			self.__screen.update(dt)
			self.__screen.draw()

			dt = self.__clock.tick(60) / 1000.0
		return 0

	def on_start(self, event):
		pass

	def exit(self):
		self.__done = True

	# Accessors ------------------------------------------------------------------------------------

	def get_screen(self):
		return self.__screen
