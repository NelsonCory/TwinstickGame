import os
import pygame

class ResourceManager:

	__instance = None

	def __init__(self, path):
		self.__base_path = os.path.dirname(path) + "/res/"
		self.__fonts = {}
		self.__tiles = [[[]]]
		self.__entities = [[]]
		self.__music = {}
		self.__effects = {}

		self.load_tiles()
		self.load_entities()
		self.load_fonts()
		self.load_effects()
		self.load_music()

		ResourceManager.__instance = self

	@staticmethod
	def get_instance():
		return ResourceManager.__instance

	def load_tiles(self):
	 	t_id= 0
		layer = 0
		for file in os.listdir(self.__base_path + "graphics/tiles/"):
			file_dat = os.path.basename(file).split("_")

			if int(file_dat[1]) > t_id:
				self.__tiles.append([[]])
				t_id = int(file_dat[1])

			if int(file_dat[2]) > layer:
				self.__tiles.append([])
				layer = int(file_dat[2])
			elif int(file_dat[2]) < layer:
				layer = int(file_dat[2])

			self.__tiles[t_id][layer].append(pygame.img.load(os.path.join(self.__base_path, "graphics/tiles/" + file)))

	def load_entities(self):
		e_id = 0
		for file in os.listdir(self.__base_path +"graphics/entities/"):
			file_dat = os.path.basename(file).split("_")

			if int(file_dat[1]) > e_id:
				self.__entities.append([])
				e_id = int(file_dat[1])

			self.__entities[e_id].append(pygame.img.load(os.path.join(self.__base_path, "graphics/entities/" + file)))

	def load_fonts(self):
		for file in os.listdir(self.__base_path + "fonts/"):
			key = "fonts/" + os.path.splitext(os.path.basename(file))[0]
			self.__fonts[key] = os.path.join(self.__base_path, "fonts/" + file)

	def load_music(self):
		for file in os.listdir(self.__base_path + "sounds/music/"):
			key = "music/" + os.path.splitext(os.path.basename(file))[0]
			self.__music[key] = pygame.mixer.Sound(os.path.join(self.__base_path, "music/" + file))

	def load_effects(self):
		for file in os.listdir(self.__base_path + "sounds/"):
			key = "sounds/" + os.path.splitext(os.path.basename(file))[0]
			self.__sounds[key] = pygame.mixer.Sound(os.path.join(self.__base_path, "sounds/" + file))

	def get_tile(self, t_id, layer, frame):
		return self.__tiles[t_id][layer][frame]

	def get_entities(self, e_id, frame):
		return self.__entities[e_id][frame]

	def get_font(self, key, size):
		return pygame.font.Font(self.__fonts[key], size)

	def get_music(self, key):
		return self.__music[key]

	def get_effects(self, key):
		return self.__effects[key]
