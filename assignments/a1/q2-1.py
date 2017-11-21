from pylab import *
import wave

### Question 2.1

buffer = 2048
in_audio = wave.open('1_4_mix.wav', 'r')
out_audio = wave.open('q2_1.wav', 'w')

out_audio.setparams(in_audio.getparams())

num_frames = buffer / (in_audio.getsampwidth() + in_audio.getnchannels())
num_frames = int(num_frames)

while True:
	frame = in_audio.readframes(num_frames)
	out_frame = bytearray(frame)
	length = len(out_frame)
	for i in range(0, length):
		if out_frame[i] is not 255:
			out_frame[i] +=1
	out_audio.writeframes(out_frame)

in_audio.close();
out_audio.close();

