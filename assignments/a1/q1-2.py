import matplotlib.pyplot as plt
from pylab import *
import random
import numpy

### Question 1.2 
# Initialize
freq = 440
sampRate = 44100  
samples = 2*sampRate
cycles = samples / sampRate
time_space = linspace(0, cycles, samples) #create a vector of evenly spaced points in the interval [0,cycles].
maxAmp= 2**14 - 1.0 

#Makes a mixture of three harmonically related sinusoids with frequencies
# f, 2f, 3f with user provided amplitudes and phases
def q_1_2(amp1, amp2, amp3, phase1, phase2, phase3):
    a = amp1 * sin(2 * pi * freq * time_space + phase1) * maxAmp #f
    b = amp2 * sin(2 * pi * 2*freq * time_space + phase2) * maxAmp #2f
    c = amp3 * sin(2 * pi * 3*freq * time_space + phase3) * maxAmp #3f
    
    return a + b + c
    
# 0 Phases
zero_phase = q_1_2(1.0, 0.5, 0.33, 0.0, 0.0, 0.0)
plt.figure()
plt.title("0 Phase")
plt.plot(time_space[0:1000] * sampRate, zero_phase[0:1000])
plt.show()

# Random Phases
rand_phase = q_1_2(1.0, 0.5, 0.33, random.random(), random.random(), random.random())
plt.figure()
plt.title("Random Phase")
plt.plot(time_space[0:1000] * sampRate, rand_phase[0:1000])
plt.show()

