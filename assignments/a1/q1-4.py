import matplotlib.pyplot as plt
from pylab import *
import wave
import struct
import random
import numpy
import sympy

### Question 1.4

# Initialize
freq = 440
sampRate = 44100
samples = 2*sampRate #2 seconds 
cycles = samples / sampRate

t = linspace(0, cycles, samples)
maxAmp= 2**15 - 1.0 

def q_1_4(snrdb, freqHz):
	s_amp = 1 
	s_wave = (s_amp*sin(2*pi*freqHz*t))
	noise, signal, snr = sympy.symbols("noise, signal, snr")
	n_power = sympy.solve(sympy.Eq(10*sympy.log(signal/noise, 10), snr), noise)[0].evalf(
		subs = {signal: s_amp, snr: snrdb})
	n_wave = ((np.random.ranf(size=samples)*2)-1)*n_power
	#plot 
	plt.figure()
	title("SNR: " + str(snrdb) + "dB  " + str(freqHz) + " Hz")
	plot(t[0:1000]*sampRate, n_wave[0:1000] + s_wave[0:1000])
	plt.show()
	
	#create audio for mixture
	audio = wave.open('1_4_' + str(snrdb) + '_' +str(freqHz) +'.wav', 'w')
	audio.setparams((1, 2, sampRate, samples, "NONE", "Uncompressed"))
	for i in n_wave + s_wave:
		packed = struct.pack('h', int16(i*maxAmp))
		audio.writeframes(packed)
	audio.close()
	

q_1_4(0, 440) #generate a 440Hz audio with 0dB SNR
q_1_4(20, 440) #generate a 440Hz audio with 10dB SNR
q_1_4(-20, 440) #genearate a 440Hz audio with -10 SNR
