from . entity import *
import pygame

from entity import *

class Player(Entity):

	def __init__(self):
		self.__skin = None
		self.__hp = 100
		self.__shield = 100
		self.__current_heat = 0
		self.__MAX_HEAT = 100

	def draw(self):
		pass

	def update(self, dt):
		pass

	def get_hp(self):
		return self.__hp

	def get_shield(self):
		return self.__shield

	def get_heat(self):
		return self.__current_heat

	def is_overheated(self):
		return self.__current_heat >= self.__MAX_HEAT
