import pyaudio
import wave
import math
import requests
import itertools
import ast
import sys
import datetime

class Jarvis:
	pa = pyaudio.PyAudio()
	data_frames = []
	resposta = ''
	start_time = ''
	end_time = ''

	def __init__(self, format, rate, buffer_sz, file_name):
		self.FORMAT = format
		self.RATE = rate
		self.BUFFER_SIZE = buffer_sz
		self.FILE_NAME = file_name
		self.stream = self.pa.open(
		format = self.FORMAT,
		input = True,
		channels = 1,
		rate = self.RATE,
		input_device_index = 1,
		frames_per_buffer = self.BUFFER_SIZE
	)

	#save wave file
	def save_file(self):
		waveFile = wave.open(self.FILE_NAME, 'wb')
		waveFile.setnchannels(1)
		waveFile.setsampwidth(self.pa.get_sample_size(self.FORMAT))
		waveFile.setframerate(self.RATE)
		waveFile.writeframes(b''.join(self.data_frames))
		waveFile.close()

	#send wave file
	def send_file(self, URL):
		waveFile = open(self.FILE_NAME, 'rb')
		if(self.resposta != ''):
			r = requests.post(URL, body={'authorized': self.resposta, 'start':self.start_time, 'end':self.end_time}, files={'record': ('record', waveFile, 'audio/wav', {})})
		else:
			r = requests.post(URL, files={'record': ('record', waveFile, 'audio/wav', {})})
			self.resposta = ast.literal_eval(r.text)['decision']
			if(self.resposta == 'MATCH'):
				self.resposta = 'true'
			else:
				self.resposta = 'false'
		waveFile.close()
		files = {'file': b''.join(self.data_frames)}
		print(ast.literal_eval(r.text))

	#run validation record
	def record_sound(self, time):
		self.data_frames = []
		print('Recording voice...')
		self.start = datetime.datetime.now().isoformat()
		aux = 0
		if(time < 0):
			time_aux = math.inf
		else:
			time_aux = time
		try:
			while(aux < time_aux):
				data = self.stream.read(self.BUFFER_SIZE)
				self.data_frames.append(data)
				aux += 1
		except KeyboardInterrupt:
			pass
		print('Finished recording...')
		self.end_time = datetime.datetime.now().isoformat()

	def close(self):
		self.stream.stop_stream()
		self.stream.close()
		self.pa.terminate()