import pygame

class Screen:

	def __init__(self, resolution=(1280, 720)):
		self.__resolution = resolution
		self.__surface = pygame.display.set_mode(resolution)
		#self.__surface = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
		self.__scene = None

	def blit(self, *args, **kwargs):
		self.__surface.blit(*args, **kwargs)

	def blit_alpha(self, source, location, opacity):
		x = location[0]
		y = location[1]
		temp = pygame.Surface((source.get_width(), source.get_height())).convert()
		temp.blit(self.__surface, (-x, -y))
		temp.blit(source, (0, 0))
		temp.set_alpha(opacity)
		self.__surface.blit(temp, location)

	def draw(self):
		self.__surface.fill((0, 0, 0))
#		self.__scene.draw(self)
		pygame.display.flip()

	def update(self, dt):
#		self.__scene.update(dt)
		pass

	def get_resolution(self):
		return self.__resolution

#	def get_scene(self):
#		return self.__scene
#
#	def set_scene(self, scene):
#		if self.__scene:
#			self.__scene.clean()
#			del self.__scene
#		self.__scene = scene
#		self.__scene.ready()
