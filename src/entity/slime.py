import pygame

class Slime(entity):

	def __init__(self,size = 0):
		self.__skin = None
		self.__size = size # 3 sizes: small, medium, venti
		self.__hp = 50
		
	
		