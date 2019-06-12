import ai2thor.controller
import keyboard
import time
import voicecontrol


if __name__ == "__main__":
	#Start up ai2thor and initialize floor
	controller = ai2thor.controller.Controller()
	controller.start(player_screen_height=666, player_screen_width=666)
	controller.reset('FloorPlan3')	
	##FloorPlan: <=30 ; 201<=<=230 ; 301<=<=330 ; 401<=<=430
	controller.step(dict(action='Initialize', gridSize=0.5))
	print('Initialized')	
	
	#Control
	while True:
		if keyboard.is_pressed('a'):
			event = controller.step(dict(action = 'MoveLeft'))
			time.sleep(0.3)
		elif keyboard.is_pressed('d'):
			event = controller.step(dict(action = 'MoveRight'))
			time.sleep(0.3)
		elif keyboard.is_pressed('w'):
			event = controller.step(dict(action = 'MoveAhead'))
			time.sleep(0.3)
		elif keyboard.is_pressed('s'):
			event = controller.step(dict(action = 'MoveBack'))
			time.sleep(0.3)
		elif keyboard.is_pressed('up arrow'):
			event = controller.step(dict(action = 'LookUp'))
			time.sleep(0.3)
		elif keyboard.is_pressed('down arrow'):
			event = controller.step(dict(action = 'LookDown'))
			time.sleep(0.3)
		elif keyboard.is_pressed('right arrow'):
			event = controller.step(dict(action = 'RotateRight'))
			time.sleep(0.3)
		elif keyboard.is_pressed('left arrow'):
			event = controller.step(dict(action = 'RotateLeft'))
			time.sleep(0.3)
		elif keyboard.is_pressed('m'):
			print('FloorPlan: 0->30 ; 201->230 ; 301->330 ; 401->430')
			print('To room number: ')
			room = input()
			room = str(room)
			controller.reset('FloorPlan' + room)
			time.sleep(0.3)
		elif keyboard.is_pressed('t'):
			act = voicecontrol.vc('null', 'null')
			if act in ['MoveLeft', 'MoveRight', 'MoveAhead', 'MoveBack', 'LookUp', 'LookDown', 'RotateRight', 'RotateLeft']:
				event = controller.step(dict(action = act))	
			time.sleep(0.3)
		elif keyboard.is_pressed('esc'):
			exit()
