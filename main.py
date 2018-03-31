import pyaudio
from rasp_class import Jarvis

#init cons
BUFFER_SIZE = 1024
REC_SECONDS = 5
RATE = 44100
FORMAT = pyaudio.paInt16
WAVE_OUTPUT_FILENAME = "file.wav"

def main():
	jarvis = Jarvis(FORMAT, RATE, BUFFER_SIZE, WAVE_OUTPUT_FILENAME)
	jarvis.record_sound(jarvis.RATE/jarvis.BUFFER_SIZE * REC_SECONDS)
	jarvis.save_file()
	jarvis.send_file("https://jarvis-api.herokuapp.com/users/5aadca3b71e9ff001f13cd89/verify")

	#jarvis.record_sound(-1)
	#jarvis.save_file()
	#jarvis.send_file("https://jarvis-api.herokuapp.com/users/5aadca3b71e9ff001f13cd89/calls")

	jarvis.close()
	print(jarvis.resposta)
	return jarvis.resposta