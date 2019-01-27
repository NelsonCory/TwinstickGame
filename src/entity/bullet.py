from . entity import *
from core.game import *
import math

class Bullet(Entity):

	DEFAULT_BULLET_SPEED = 200
	BULLET_TRAIL_LENGTH = 10
	GREEN = pygame.Color(76, 195, 113)
	PURPLE = pygame.Color(147, 55, 165)
	COLORS = [GREEN, PURPLE]

	def __init__(self, x, y, rotx, roty, allegiance):
		super(Bullet, self).__init__()
		self.__x = x
		self.__y = y
		self.__velocity_x = rotx
		self.__velocity_y = roty
		self.__speed = Bullet.DEFAULT_BULLET_SPEED
		self.__allegiance = allegiance
		self.__color = Bullet.COLORS[allegiance]
		self.__dead = False

	def draw(self):
		surface = get_game_instance().get_screen().get_surface()
		self.__trail_x = self.__x - self.__velocity_x * Bullet.BULLET_TRAIL_LENGTH
		self.__trail_y = self.__y - self.__velocity_y * Bullet.BULLET_TRAIL_LENGTH
		start = (self.__x, self.__y)
		end = (self.__trail_x, self.__trail_y)
		pygame.draw.line(surface, self.__color, start, end, 3)

	def update(self, dt):
		self.__x += self.__velocity_x * dt * self.__speed
		self.__y += self.__velocity_y * dt * self.__speed
		self.check_enemy_collision()

	def check_enemy_collision(self):
		enemy_id = (2 - self.__allegiance) % 2
		enemy = get_game_instance().get_screen().get_scene().get_players()[enemy_id]
		print(enemy.get_position())
		enemy_rect = pygame.Rect(enemy.get_position(), (32, 32))
		enemy_rect.collidepoint(self.__x, self.__y)
		EventManager.get_instance().send("damage", enemy_id)
		#self.die()

	def die(self):
		self.__dead = True
		EventManager.get_instance().send("clean")

	def is_dead(self):
		return self.__dead

