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
		self.__pos = Vec(x, y)
		self.__move_direction = Vec(0, 0.1)
		self.__shoot_direction = Vec(0, 1)
		self.__speed = 0
		self.__alive = True

		EventManager.get_instance().subscribe(f"joystick{self.__id}_update", self.on_joystick_update)

	def draw(self):
		surface = get_game_instance().get_screen().get_surface()
		surface.blit(ResourceManager.get_instance().get_entities(self.__id, self.__frame),
				self.__pos.get_tuple())

	def update(self, dt):
		if self.__move_direction.magnitude() > Player.ANALOG_STICK_THRESHOLD:
			self.__speed = Player.MAX_SPEED
		else:
			self.__speed = 0
		if self.__move_direction.magnitude() > 1:
			self.__move_direction = self.__move_direction.normalize()
		self.__pos += self.__move_direction * self.__speed * dt

	def get_hp(self):
		return self.__hp

	def get_shield(self):
		return self.__shield

	def get_heat(self):
		return self.__current_heat

	def is_overheated(self):
		return self.__current_heat >= Player.MAX_HEAT

	def on_joystick_update(self, vecs):
		self.__move_direction = vecs[0]
		if vecs[1].magnitude() > Player.ANALOG_STICK_THRESHOLD:
			self.__shoot_direction = vecs[1]
