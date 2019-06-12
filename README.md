# Roboto-Speech
Chu Minh Tiến - 16020287
Controlling robot in Ai2thor with voice input

# Requirements
OS: Mac OS X 10.9+, Ubuntu 14.04+
Graphics Card: DX9 (shader model 3.0) or DX11 with feature level 9.3 capabilities.
CPU: SSE2 instruction set support.
Python 2.7 or Python 3.5+
Linux users: X server with GLX module enabled
CUDA

# GETTING STARTED
Installing AI2-THOR using pip:
$ pip install ai2thor
Installing keyboard using pip:
$ pip install keyboard
Installing SpeechRecognition using pip:
$ pip install SpeechRecognition
Installing PyAudio using pip:
$ pip install PyAudio

Actions
“w” - Move the agent forward by gridSize.
“a” - Move the agent left by gridSize (without changing view direction).
“s” - Move the agent backward by gridSize (without changing view direction).
“d” - Move the agent right by gridSize (without changing view direction).
“left arrow” - Rotate the agent by 90 degrees to the left of its current facing.
“right arrow” - Rotate the agent by 90 degrees to the right of its current facing.
“up arrow” - Angle the agent’s view up in 30 degree increments.
“down arrow” - Angle the agent’s view down in 30 degree increments.
"t" - 
