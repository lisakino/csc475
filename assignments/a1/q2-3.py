import matplotlib.pyplot as plt
from pylab import *
import numpy as np

### Question 2.3


# Initialize
freq = 440
sampRate = 4096
samples = 2*sampRate
cycles = samples / sampRate

t = linspace(0, cycles, samples) #create a vector of evenly spaced points in the interval [0,cycles].
maxAmp= 2**14 - 1.0 

def q_1_2(amp1, amp2, amp3, phase1, phase2, phase3):
    a = amp1 * sin(2 * pi * freq * t + phase1) * maxAmp
    b = amp2 * sin(2 * pi * 2*freq * t + phase2) * maxAmp
    c = amp3 * sin(2 * pi * 3*freq * t + phase3) * maxAmp
    return a + b + c
    
# 0 Phases
zero_phase = q_1_2(1.0, 0.5, 0.33, 0.0, 0.0, 0.0)

def compute_dft(signal):
	n = len(signal)/2
	outreal = []
	outimag = []
	for k in range(n):  # For each output element
		sumreal = 0.0
		sumimag = 0.0
		for t in range(n):  # For each input element
			angle = 2 * pi * t * k / n
			sumreal +=  signal[t] * cos(angle) 
			sumimag += signal[t] * sin(angle)
		outreal.append(sumreal)
		outimag.append(sumimag)
	return outreal + outimag

dft_size = len(zero_phase)/2
dft_space = ((compute_dft(zero_phase))/dft_size)[0: int(dft_size/2)]
figure()
title("Magnitude Spectrum Q2.3")
size = len(zero_phase)
series = arange(size)
intervals = size/sampRate
freq = (series/intervals)[0:int(size/2)]
plt.plot(freq, np.abs(dft_space))
plt.show();

