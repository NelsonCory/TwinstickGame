class Scene:

	def __init__(self):
		self.__controllers = []

	def add_controller(self, controller):
		self.__controllers.append(controller)

	def remove_controller(self, controller):
		del self.__controllers.find(controller)

	def draw(self):
		pass

	def tick(self, dt):
		pass

