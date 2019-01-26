class TileMap:

	__instance = None

	def __init__(self):
		#self.__chunk[[]]

		self.__frame = 0

		TileMap.__instance = self


	@staticmethod
	def get_instance():
		return TileMap.__instance

	def load_map(self, path):
		pass

	def draw(self):
		pass

	def update(self, dt):
		pass
