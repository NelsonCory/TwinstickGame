import pygame

from entity import *

class Player(Entity):

	def __init__(self):
		self.__skin = None
		self.__hp = 100
		self.__shield = 100
	
	def get_hp(self):
		return self.__hp
	
	def get_shield(self):
		return self.__shield
		
		
	