class Vec:

	def __init__(self, *args):
		self.__v = tuple(args)

	def __add__(self, other):
		return Vec(*(i + j for i, j in zip(self.__v, other.__v)))

	def __mul__(self, const):
		return Vec(*(i * const for i in self.__v))

	def __sub__(self, other):
		return self + other*(-1)

	def get_tuple(self):
		return self.__v
