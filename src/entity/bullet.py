from . entity import *
from core.game import *
from core.utils import Vec
import math

class Bullet(Entity):

	DEFAULT_BULLET_SPEED = 200
	BULLET_TRAIL_LENGTH = 10

	def __init__(self, x, y, angle, allegiance):
		super(Bullet, self).__init__()
		self.__pos = Vec(x, y)
		self.__direction_vec = Vec(math.cos(angle), math.sin(angle))
		self.__speed = Bullet.DEFAULT_BULLET_SPEED
		self.__allegiance = allegiance

	def draw(self):
		surface = get_game_instance().get_screen().get_surface()
		trail = self.__pos - self.__direction_vec * Bullet.BULLET_TRAIL_LENGTH
		start = self.__pos.get_tuple()
		end = trail.get_tuple()
		print(start, end)
		pygame.draw.line(surface, pygame.Color(255, 0, 0, 0), start, end, 3)

	def update(self, dt):
		self.__pos += self.__direction_vec * (dt * self.__speed)
