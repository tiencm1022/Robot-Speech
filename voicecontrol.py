import os
import micin

def vc(key, action):
	#Listening to audio
	key = micin.listen()
	if isinstance(key, str):
		print('AUDIO: ' + key)

	#Control with audio input
	try:
		if 'đi thẳng' in key:
			action = 'MoveAhead'
		elif 'sang trái' in key:
			action = 'MoveLeft'
		elif 'sang phải' in key:
			action = 'MoveRight'
		elif 'lùi về' in key:
			action = 'MoveBack'
		elif 'nhìn lên' in key:
			action = 'LookUp'
		elif 'nhìn xuống' in key:
			action = 'LookDown'
		elif 'quay trái' in key:
			action = 'RotateLeft'
		elif 'quay phải' in key:
			action = 'RotateRight'
		else:
			action = 'null'
		print('Action: ' + action)
	except Exception as e:
		print('Voicecontrol error')
	return action





