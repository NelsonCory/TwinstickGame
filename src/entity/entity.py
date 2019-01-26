import pygame

class Entity():

	def __init__(self):
		self.__position = (0,0)
		self.__tilePosition = (0,0)
		self.__e_id = 0 #e
		self.__e_frame = 0
	
	def get_skin(self):
		return self.skin
	
	def get_position(self):
		return self.__position
	
	def set_position(self,position):
		self.__position = position
	
	def get_tile_position(self):
		return self.__tile_position
		
	def set_tile_position(self,position):
		self.__tile_position = position
	
	def get_rect(self):
		rect = self.__skin.get_rect()
		return pygame.Rect(self.__position[0], self.__position[1], rect[2], rect[3])
	
	def get_id(self):
		return self.__e_id
	
	def set_id(self):
		return self.__e_id
		
	def get_frame(self):
		#get current frame
		return self.__e_frame
	
	def set_frame(self,frame):
		self.__e_frame = frame
	