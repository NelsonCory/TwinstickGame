from . entity import *
from core.game import *
from core.resource_manager import *
from core.utils import *
import pygame

from entity import *

class Player(Entity):

	def __init__(self, id_, x, y):
		self.__id = id_
		self.__total_frames = ResourceManager.get_instance().get_entity_frames(self.__id)
		self.__frame = 0
		self.__hp = 100
		self.__shield = 100
		self.__current_heat = 0
		self.__MAX_HEAT = 100
		self.__pos = Vec(x, y)
		self.__direction = Vec(0, 1)
		self.__speed = 0

	def draw(self):
		surface = get_game_instance().get_screen().get_surface()
		surface.blit(ResourceManager.get_instance().get_entities(self.__id, self.__frame),
				self.__pos.get_tuple())

	def update(self, dt):
		self.__pos += self.__direction * self.__speed * dt

	def get_hp(self):
		return self.__hp

	def get_shield(self):
		return self.__shield

	def get_heat(self):
		return self.__current_heat

	def is_overheated(self):
		return self.__current_heat >= self.__MAX_HEAT
