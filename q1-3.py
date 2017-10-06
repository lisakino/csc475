import matplotlib.pyplot as plt
from pylab import *
import wave
import struct
import random

### Question 1.3

# Initialize
freq = 440
sampRate = 44100
samples = 1*sampRate #1 sec audio
cycles = samples / sampRate

time_space = linspace(0, cycles, samples)
maxAmp= 2**15 - 1.0 

### From Question 1.2 

def q_1_2(amp1, amp2, amp3, phase1, phase2, phase3):
    a = (amp1 * sin(2 * pi * freq * time_space + phase1)) * maxAmp  #f
    b = (amp2 * sin(2 * pi * 2*freq * time_space + phase2)) * maxAmp #2f
    c = (amp3 * sin(2 * pi * 3*freq * time_space + phase3)) * maxAmp  #3f        
    return a+b+c
    

# 0 Phases
zero_phase = q_1_2(1.0, 0.5, 0.33, 0.0, 0.0, 0.0)

# Random Phases
rand_phase = q_1_2(1.0, 0.5, 0.33, random.random(), random.random(), random.random())

### Generate audio
# 0 Phase Audio  
audio_file = wave.open('zero_phase_q1.wav', 'w')
audio_file.setparams((1, 2, sampRate, samples, "NONE", "Uncompressed"))
for x in zero_phase:
    packed_value = struct.pack('h', int16(x))
    audio_file.writeframes(packed_value)
audio_file.close()
        
# Random Phase Audio
audio_file = wave.open('random_phase_q1.wav', 'w')
audio_file.setparams((1, 2, sampRate, samples, "NONE", "Uncompressed"))
for x in rand_phase:
    audio_file.writeframes(struct.pack('h', int16(x)))
audio_file.close()

