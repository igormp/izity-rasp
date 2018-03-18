import pyaudio
from rasp_class import Izity

#init cons
BUFFER_SIZE = 1024
REC_SECONDS = 5
RATE = 44100
FORMAT = pyaudio.paInt16
WAVE_OUTPUT_FILENAME = "file.wav"

def main():
	izity = Izity(FORMAT, RATE, BUFFER_SIZE, WAVE_OUTPUT_FILENAME)
	izity.record_sound(izity.RATE/izity.BUFFER_SIZE * REC_SECONDS)
	izity.save_file()
	izity.send_file("https://izity-api.herokuapp.com/users/5aadca3b71e9ff001f13cd89/verify")

	#izity.record_sound(-1)
	#izity.save_file()
	#izity.send_file("https://izity-api.herokuapp.com/users/5aadca3b71e9ff001f13cd89/calls")

	izity.close()
	print(izity.resposta)
	return izity.resposta