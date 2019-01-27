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
		self.__time = pygame.time.get_ticks()
		self.__ani_count = 0
		self.__ani_milli = 200
		self.set_frame(0)
		self.__anim_state = 0


		EventManager.get_instance().subscribe(f"joystick{self.__id}_update", self.on_joystick_update)

	def draw(self):
		#print(self.get_frame())
		#print(ResourceManager.get_instance().get_entity_frames(1))
		surface = get_game_instance().get_screen().get_surface()
		surface.blit(ResourceManager.get_instance().get_entities(self.__id, self.get_frame()),
				(self.__x, self.__y))

	def update(self, dt):

		if(self.__anim_state == 0):
			self.set_frame(0)
		else:
			self.__ani_time = pygame.time.get_ticks()
			if (self.__ani_time - self.__time) >= self.__ani_milli:
				self.__time = pygame.time.get_ticks()
				self.__temp_frame = self.get_frame()+1
				self.set_frame(self.__temp_frame)
				if self.get_frame() == 3:
					self.set_frame(0)

		if(self.__speed == 0):
			self.__anim_state = 0
		else:
			self.__anim_state = 1

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

	def will_collide(self, tile_manager, test_rect, test_tile_x, test_tile_y):
		for x in range(test_tile_x - 1, test_tile_x + 2):
			for y in range(test_tile_y - 1, test_tile_y + 2):
				tile_x = x*32
				tile_y = y*32
				tile_rect = pygame.Rect(tile_x, tile_y, 32, 32)
				if tile_manager.get_tile(x, y).get_solid():
					 if test_rect.colliderect(tile_rect):
						 print("collide")
						 return tile_rect

		return None

	def check_collisions(self, dx, dy):
		# Get the tile coordinates
		tile_x = int(self.__x // 32)
		tile_y = int(self.__y // 32)
		tm = TileMap.get_instance()

		player_rect = pygame.Rect(self.__x, self.__y, 32, 32)

		test_rect_x = pygame.Rect(self.__x + dx, self.__y, 32, 32)
		test_tile_x = self.will_collide(tm, test_rect_x, tile_x, tile_y)
		if test_tile_x != None:
			if dx < 0:
				dx = test_tile_x.right - player_rect.left
			if dx > 0:
				if not(player_rect.bottom - test_tile_x.top < player_rect.right - test_tile_x.left):
					dx = test_tile_x.left - player_rect.right
			print("x_collision")

		test_rect_y = pygame.Rect(self.__x, self.__y + dy, 32, 32)
		test_tile_y = self.will_collide(tm, test_rect_y, tile_x, tile_y)
		if test_tile_y != None:
			if dy < 0:
				dy = test_tile_y.bottom - player_rect.top
			if dy > 0:
				if not(player_rect.right - test_tile_y.left < player_rect.bottom - test_tile_y.top):
					dy = test_tile_y.top - player_rect.bottom
			print("y_collision")
		return dx, dy


	def get_hp(self):
		return self.__hp

	def get_shield(self):
		return self.__shield

	def get_heat(self):
		return self.__current_heat

	def is_overheated(self):
		return self.__current_heat >= Player.MAX_HEAT

	def on_joystick_update(self, joystick_data):
		self.__velocity_x = joystick_data[0]
		self.__velocity_y = joystick_data[1]
		rot_x, rot_y = joystick_data[2:]
		if rot_x*rot_x + rot_y*rot_y > Player.ANALOG_STICK_THRESHOLD*Player.ANALOG_STICK_THRESHOLD:
			self.__rotation_x = rot_x
			self.__rotation_y = rot_y
