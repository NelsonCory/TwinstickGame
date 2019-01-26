import os
import pygame

class ResourceManager:

	__instance = None

	def __init__(self, path):
		self.__base_path = os.path.dirname(path) + "/res/"
		self.__fonts = {}
		self.__graphics = {}
		self.__music = {}
		self.__sounds = {}
		for file in os.listdir(self.__base_path + "fonts/"):
			key = "fonts/" + os.path.splitext(os.path.basename(file))[0]
			self.__fonts[key] = os.path.join(self.__base_path, "fonts/" + file)
		for file in os.listdir(self.__base_path + "graphics/"):
			key = "graphics/" + os.path.splitext(os.path.basename(file))[0]
			surface = pygame.image.load(os.path.join(self.__base_path, "graphics/" + file))
			self.__graphics[key] = surface
		for file in os.listdir(self.__base_path + "music/"):
			key = "music/" + os.path.splitext(os.path.basename(file))[0]
			music = pygame.mixer.Sound(os.path.join(self.__base_path, "music/" + file))
			self.__music[key] = music
		for file in os.listdir(self.__base_path + "sounds/"):
			key = "sounds/" + os.path.splitext(os.path.basename(file))[0]
			sound = pygame.mixer.Sound(os.path.join(self.__base_path, "sounds/" + file))
			self.__sounds[key] = sound

		ResourceManager.__instance = self

	@staticmethod
	def get_instance():
		return ResourceManager.__instance

	def get_font(self, key, size):
		return pygame.font.Font(self.__fonts[key], size)

	def get_image(self, key):
		return self.__graphics[key]

	def get_music(self, key):
		return self.__music[key]

	def get_sound(self, key):
		return self.__sounds[key]
