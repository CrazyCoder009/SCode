#!sudo apt install python3.6
#!sudo apt-get install python3-pip
#!pip3 install speechrecognition
#!sudo pip3 install pyaudio
#!sudo apt-get install python-pyaudio python3-pyaudio

import speech_recognition as spr

mc=spr.Microphone()
mc.list_microphone_names()