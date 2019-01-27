from . entity import *
from core.game import *
import math

class Bullet(Entity):

	DEFAULT_BULLET_SPEED = 200
	BULLET_TRAIL_LENGTH = 10

	def __init__(self, x, y, angle, allegiance):
		super(Bullet, self).__init__()
		self.__x = x
		self.__y = y
		self.__velocity_x = math.cos(angle)
		self.__velocity_y = math.sin(angle)
		self.__speed = Bullet.DEFAULT_BULLET_SPEED
		self.__allegiance = allegiance

	def draw(self):
		surface = get_game_instance().get_screen().get_surface()
		trail_x = self.__x - self.__velocity_x * Bullet.BULLET_TRAIL_LENGTH
		trail_y = self.__y - self.__velocity_y * Bullet.BULLET_TRAIL_LENGTH
		start = (self.__x, self.__y)
		end = (trail_x, trail_y)
		pygame.draw.line(surface, pygame.Color(255, 0, 0, 0), start, end, 3)

	def update(self, dt):
		self.__x += self.__velocity_x * dt * self.__speed
		self.__y += self.__velocity_y * dt * self.__speed
