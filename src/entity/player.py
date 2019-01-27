from . entity import *
from core.event_manager import *
from core.game import *
from core.resource_manager import *
from core.utils import *
import pygame

from entity import *

class Player(Entity):

	MAX_HEAT = 100
	MAX_SPEED = 500
	ANALOG_STICK_THRESHOLD = 0.25

	def __init__(self, id_, x, y):
		self.__id = id_
		self.__total_frames = ResourceManager.get_instance().get_entity_frames(self.__id)
		self.__frame = 0
		self.__hp = 100
		self.__shield = 100
		self.__current_heat = 0
		self.__x = x
		self.__y = y
		self.__velocity_x = 0
		self.__velocity_y = 0
		self.__speed = 0
		self.__rotation_x = 0
		self.__rotation_y = 1
		self.__alive = True

		EventManager.get_instance().subscribe(f"joystick{self.__id}_update", self.on_joystick_update)

	def draw(self):
		surface = get_game_instance().get_screen().get_surface()
		surface.blit(ResourceManager.get_instance().get_entities(self.__id, self.__frame),
				(self.__x, self.__y))

	def update(self, dt):
		if self.__velocity_x*self.__velocity_x + self.__velocity_y*self.__velocity_y > Player.ANALOG_STICK_THRESHOLD*Player.ANALOG_STICK_THRESHOLD:
			self.__speed = Player.MAX_SPEED
		else:
			self.__speed = 0
		norm = math.sqrt(self.__velocity_x*self.__velocity_x + self.__velocity_y*self.__velocity_y)
		if norm > 1:
			self.__velocity_x = self.__velocity_x / norm
			self.__velocity_y = self.__velocity_y / norm
		self.__x += self.__velocity_x * self.__speed * dt
		self.__y += self.__velocity_y * self.__speed * dt

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
