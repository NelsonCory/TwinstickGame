
class Tile():

	def __init__(self):
		self.__t_id = None
		self.__solid = None

	def get_t_id(self):
		return self.__t_id

	def get_solid(self):
		return self.__solid

	def set_t_id(self, t_id):
		self.__t_id = t_id

	def set_solid(self, solid):
		self.__solid = __solid

	def load_tile(self, data):
		self.__t_id = int(data.split()[0])
		self.__solid = int(data.split()[1])
