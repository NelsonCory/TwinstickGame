import math

class Vec:

	def __init__(self, *args):
		self.__v = tuple(args)

	def __add__(self, other):
		return Vec(*(i + j for i, j in zip(self.__v, other.__v)))

	def __mul__(self, const):
		return Vec(*(i * const for i in self.__v))

	def __sub__(self, other):
		return self + other*(-1)

	def __truediv__(self, const):
		return Vec(*(i / const for i in self.__v))

	def __str__(self):
		return f"<{self.__v[0]}, {self.__v[1]}>"

	def magnitude(self):
		return math.sqrt(sum(i*i for i in self.__v))

	def normalize(self):
		if self.magnitude() > 0:
			return self / self.magnitude()
		else:
			return Vec(*((0,) * len(self.__v)))

	def get_tuple(self):
		return self.__v
