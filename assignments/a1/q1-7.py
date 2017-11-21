import matplotlib.pyplot as plt
from pylab import *
import numpy as np
import struct

sampRate = 44100
samples = 2 * 44100
cycles = samples / sampRate
freq = 440

t = linspace(0, cycles, samples)
maxAmp= 2**14 - 1.0 # maximum amplitude
phase = 0.0

def inner_product(one, two):
    return np.inner(one, two)
  
#From Q1.2
def q_1_2(amp1, amp2, amp3, phase1, phase2, phase3):
    a = amp1 * sin(2 * pi * freq * t + phase1) * maxAmp #f
    b = amp2 * sin(2 * pi * 2*freq * t + phase2) * maxAmp #2f
    c = amp3 * sin(2 * pi * 3*freq * t + phase3) * maxAmp #3f    
    return a + b + c

#create mixture
mixture = np.array(q_1_2(1.0, 0.5, 0.33, pi, 0, 0))

def sinusoids(amp, freq, phase):
	x = amp * sin(2 * pi * freq * t + phase)
	return x

print("Inner products")
#unit amplitude
x_1 = sinusoids(1.0, freq, phase)
inner_product_1 = inner_product(mixture, x_1)
print('Unit amplitude:	' + str(inner_product_1))

#2f 
x_2 = sinusoids(1.0, (2*freq), phase)
inner_product_2 = inner_product(mixture, x_2)
print('2*frequency:	' +  str(inner_product_2))

#freq not in mixture: 0.2
x_3 = sinusoids(.2, freq, phase)
inner_product_3 = inner_product(mixture, x_3)
print('Freq not in mixture (0.2Hz):	'+ str(inner_product_3))


### Q1.8

x_diff_phase = sinusoids(1, (2*freq), (pi/2))
inner_product_diff_phase = inner_product(mixture, x_diff_phase)
print("Different phase pi/2:	" + str(inner_product_diff_phase))

x_diff_phase_2 = sinusoids(1, (2*freq), (3*pi/2))
inner_product_diff_phase_2 = inner_product(mixture, x_diff_phase_2)
print("Different phase 3pi/2:	" + str(inner_product_diff_phase_2))