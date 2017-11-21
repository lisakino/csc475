import matplotlib.pyplot as plt
from pylab import *
import numpy as np

### Question 1.5

# Initialize
freq = 440
sampRate = 44100
samples = 2*sampRate #2 seconds 
cycles = samples / sampRate

t = linspace(0, cycles, samples)

def inner_product_amp(one, two):
    in_product = np.inner(one, two)
    return 2*(in_product/len(one)) #inner product amplitude equation

#function to generate sinusoids
def sinusoids(amp, freq):
	x = amp * np.sin(2 * np.pi * freq * t)
	return x

data = sinusoids(0.4, 440)
unit_amp = sinusoids(1.0, 440)
diff_amp = sinusoids(0.6, 440)
print("Inner Product Amplitude with same freq, phase and unit amp: ")
print(inner_product_amp(data, unit_amp)) 
print("Inner Product Amplitude with different amplitude: ")
print(inner_product_amp(data, diff_amp)) #different amplitude 
