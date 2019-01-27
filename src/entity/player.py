from . entity import *
from core.event_manager import *
from core.game import *
from core.resource_manager import *
from map.tile_map import *
import math
import pygame
import time

from entity import *

class Player(Entity):

	MAX_HEAT = 100
	MAX_SPEED = 200
	ANALOG_STICK_THRESHOLD = 0.25

	def __init__(self, id_):
		self.__id = id_
		self.__total_frames = ResourceManager.get_instance().get_entity_frames(self.__id)
		self.__hp = 100
		self.__shield = 100
		self.__current_heat = 0
		spawn_list = TileMap.get_instance().get_spawn_list()
		self.__x = 0
		self.__y = 0
		for spawnpoint in spawn_list:
			if spawnpoint[2] == self.__id+1:
				self.__x, self.__y = spawnpoint[0]*32, spawnpoint[1]*32
				break
		self.__velocity_x = 0
		self.__velocity_y = 0
		self.__speed = 0
		self.__rotation_x = 0
		self.__rotation_y = 1
		self.__alive = True
		self.__anim_state = 0
		self.__anim_speed = 0.2 #seconds
		self.__base_time = time.clock()


		EventManager.get_instance().subscribe(f"joystick{self.__id}_update", self.on_joystick_update)

	def draw(self):
		#print(self.get_frame())
		#print(ResourceManager.get_instance().get_entity_frames(1))
		surface = get_game_instance().get_screen().get_surface()
		surface.blit(ResourceManager.get_instance().get_entities(self.__id, self.get_frame()),
				(self.__x, self.__y))

	def update(self, dt):

		self.set_frame(1)

		if self.__velocity_x*self.__velocity_x + self.__velocity_y*self.__velocity_y > Player.ANALOG_STICK_THRESHOLD*Player.ANALOG_STICK_THRESHOLD:
			self.__speed = Player.MAX_SPEED
		else:
			self.__speed = 0

		norm = math.sqrt(self.__velocity_x*self.__velocity_x + self.__velocity_y*self.__velocity_y)
		if norm > 1:
			self.__velocity_x = self.__velocity_x / norm
			self.__velocity_y = self.__velocity_y / norm
		dx = self.__velocity_x * self.__speed * dt
		dy = self.__velocity_y * self.__speed * dt
		dx, dy = self.check_collisions(dx, dy)
		self.__x += dx
		self.__y += dy

	def check_collisions(self, dx, dy):
		# Get the tile coordinates
		tile_x = int(self.__x // 32)
		tile_y = int(self.__y // 32)

		# Iterate over every square around the current tile
		for i in range(-1, 2):
			for j in range(-1, 2):

				# Skip out-of-range tiles
				if tile_x + i < 0 or tile_x + i >= 40 or tile_y + j < 0 or tile_y + j >= 22:
					continue

				# Skip non-solid tiles
				if not(TileMap.get_instance().get_tile(tile_x+i, tile_y+j).get_solid()):
					continue

				# Create rects for collision testing
				test_rect_x = pygame.Rect(self.__x + dx, self.__y, 32, 32)
				test_rect_y = pygame.Rect(self.__x, self.__y + dy, 32, 32)
				tile_rect = pygame.Rect((tile_x + i)*32, (tile_y + j)*32, 32, 32)
				player_rect = pygame.Rect(self.__x, self.__y, 32, 32)

				# Collision corrections
				if test_rect_x.colliderect(tile_rect):
					if dx < 0:
						dx = tile_rect.right - player_rect.left
					elif dx > 0:
						dx = tile_rect.left - player_rect.right
					else:
						dx = 0
				if test_rect_y.colliderect(tile_rect):
					if dy < 0:
						dy = tile_rect.bottom - player_rect.top
					elif dy > 0:
						dy = tile_rect.top - player_rect.bottom
					else:
						dy = 0

		return dx, dy


	def get_hp(self):
		return self.__hp

	def get_shield(self):
		return self.__shield

	def get_heat(self):
		return self.__current_heat

	def get_position(self):
		return self.__x, self.__y

	def get_rotation(self):
		return self.__rotation_x, self.__rotation_y

	def set_hp(self, hp):
		self.__hp = hp

	def set_shield(self, shield):
		self.__shield = shield

	def set_heat(self, heat):
		self.__heat = heat

	def is_overheated(self):
		return self.__current_heat >= Player.MAX_HEAT

	def on_joystick_update(self, joystick_data):
		self.__velocity_x = joystick_data[0]
		self.__velocity_y = joystick_data[1]
		rot_x, rot_y = joystick_data[2:]
		if rot_x*rot_x + rot_y*rot_y > Player.ANALOG_STICK_THRESHOLD*Player.ANALOG_STICK_THRESHOLD:
			self.__rotation_x = rot_x
			self.__rotation_y = rot_y

