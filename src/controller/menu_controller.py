import pygame, controller, core.event_manager

class MenuController(Controller):

	def __init__(self):
		super(MenuController,self).__init__()
	  
	
		#menu controller for player 1
		try:
			self.__joystick = pygame.joystick.Joystick(0)
			self.__joystick.init()
			self.__buttons = self.__joystick.get_button(3) #TODO - find out what this does
		except:
			print("ERROR IN MENU CONTROLLER PLAYER ONE JOYSTICK INITIALIZATION")
			
		#menu controller for player 2
		try:
			self.__joystick = pygame.joystick.Joystick(1)
			self.__joystick.init()
			self.__buttons = self.__joystick.get_button(3) #TODO - find out what this does
		except:
			print("ERROR IN MENU CONTROLLER PLAYER TWO JOYSTICK INITIALIZATION")
		
		def key_in(self,event):
			if event.key == pygame.K_SPACE:
				pass
		
		def receive_joy(self,event):
			#player 1
			try:
				self.__buttons = self.joystick.get_button(3)
				if(self.__buttons):
					pass
			except:
				print("ERROR in Menu Controller, receive joy player 1") 
			try:
				self.__buttons2 = self.__joysticks.get_button(3)
				if(self.__buttons2):
					pass
			except:
				pass