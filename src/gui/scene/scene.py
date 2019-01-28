class Scene:

	def __init__(self):
		self.__controllers = []

	def add_controller(self, controller):
		self.__controllers.append(controller)

	def draw(self):
		pass

	def update(self, dt):
		pass

	def clean(self):
		pass

	def ready(self):
		pass

