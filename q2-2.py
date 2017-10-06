import matplotlib.pyplot as plt
from pylab import *
import numpy as np
    
### Question 2.2

# Initialize
freq = 440
sampRate = 4096
samples = 2*sampRate
cycles = samples / sampRate

t = linspace(0, cycles, samples)
maxAmp= 2**15 - 1.0 

### From Question 1.2 

def q_1_2(amp1, amp2, amp3, phase1, phase2, phase3):
    a = amp1 * sin(2 * pi * freq * t + phase1) * maxAmp
    b = amp2 * sin(2 * pi * 2*freq * t + phase2) * maxAmp
    c = amp3 * sin(2 * pi * 3*freq * t + phase3) * maxAmp
    
    return a + b + c

# 0 Phases Mixture
zero_phase = q_1_2(1.0, 0.5, 0.33, 0.0, 0.0, 0.0)
    
fft_size = len(zero_phase)
fft_space = (np.fft.fft(zero_phase) / fft_size)[0 : int(fft_size / 2)]
figure()
title("Magnitude Spectrum")
size = len(zero_phase)
series = arange(size)
intervals = size / sampRate
freq = (series / intervals)[0 : int(size / 2)]
plot(freq, np.abs(fft_space))
plt.show();
