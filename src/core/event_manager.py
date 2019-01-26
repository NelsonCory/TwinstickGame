import time

class EventManager:

	instance = None

	@staticmethod
	def get_instance():
		return EventManager.instance

	def __init__(self):
		EventManager.instance = self
		self.__queue = []
		self.__callbacks = {}

	def send(self, label, value = None, delay = 0):
		self.__queue.insert(0, (label, value, time.time() + delay))

	def dispatch(self):
		num_events = len(self.__queue)
		current_time = time.time()
		for i in range(num_events):
			label, value, timestamp = self.__queue.pop()
			if current_time >= timestamp:
				if label in self.__callbacks:
					callbacks = self.__callbacks[label].copy()
					for f in callbacks:
						f(value)
			else:
				self.__queue.insert(0, (label, value, timestamp))

	def subscribe(self, label, callback):
		if label in self.__callbacks:
			self.__callbacks[label].append(callback)
		else:
			self.__callbacks[label] = [callback]

	def unsubscribe(self, label, callback):
		try:
			self.__callbacks[label].remove(callback)
		except ValueError:
			pass
