# Robot-Speech
Chu Minh Tiến - 16020287 <p>
Controlling robot in Ai2thor with voice input.

# Requirements
OS: Mac OS X 10.9+, Ubuntu 14.04+ <p>
Graphics Card: DX9 (shader model 3.0) or DX11 with feature level 9.3 capabilities. <p>
CPU: SSE2 instruction set support. <p>
Python 2.7 or Python 3.5+ <p>
Linux users: X server with GLX module enabled. <p>
CUDA <p>

# GETTING STARTED
Installing AI2-THOR using pip: <p>
$ pip install ai2thor <p>
Installing keyboard using pip: <p>
$ pip install keyboard <p>
Installing SpeechRecognition using pip: <p>
$ pip install SpeechRecognition<p>
Installing PyAudio using pip:<p>
$ pip install PyAudio<p>
Run robot.py<p>
In the first time you run ai2thor, a file containing scenarios weighs about 500MB will be downloaded.<p>

# Actions
Using keyboard to perform the following actions:<p>
“w” - Move the agent forward by gridSize.<p>
“a” - Move the agent left by gridSize (without changing view direction).<p>
“s” - Move the agent backward by gridSize (without changing view direction).<p>
“d” - Move the agent right by gridSize (without changing view direction).<p>
“left arrow” - Rotate the agent by 90 degrees to the left of its current facing.<p>
“right arrow” - Rotate the agent by 90 degrees to the right of its current facing.<p>
“up arrow” - Angle the agent’s view up in 30 degree increments.<p>
“down arrow” - Angle the agent’s view down in 30 degree increments.<p>
"t" - Begin recording voice input through microphone and use the input to perform above actions.<p>
 *** This action will occur delay in recording and processing ***<p>
 *** Sometimes the result can be wrong and no action will be performed ***<p>
 "m" - Change from the current FloorPlan (Room/Scenario) to another.<p>
 *** FloorPlan: 0->30 ; 201->230 ; 301->330 ; 401->430 ***
  
# Voice inputs for controlling:
Only the following speech input can be used to control:<p>
"đi thẳng" - Move the agent forward by gridSize.<p>
“sang trái” - Move the agent left by gridSize.<p>
“lùi về” - Move the agent backward by gridSize.<p>
“sang phải” - Move the agent right by gridSize.<p>
“quay trái” - Rotate the agent by 90 degrees to the left.<p>
“quay phải” - Rotate the agent by 90 degrees to the right.<p>
“nhìn lên” - Angle the agent’s view up in 30 degree increments.<p>
“nhìn xuống” - Angle the agent’s view down in 30 degree increments.<p>
