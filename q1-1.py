import matplotlib.pyplot as plt
from pylab import *
import numpy as np

### Question 1.1

# Initialize
freq = 440 
sampRate = 44100  
samples = 2*sampRate
cycles = samples / sampRate
t = linspace(0, cycles, samples) #create a vector of evenly spaced points in the interval [0,cycles]

#function to generate sinusoids
def sinusoids(amp, freq):
	x = amp * np.sin(2 * np.pi * freq * t)
	return x

#Takes input array of audio samples and return the peak amplitude
def peakAmplitude(audio_samp):
    return np.max(audio_samp)
    
    
#generate sinusoids of frequencies 200Hz, 440Hz, 500Hz
#with amplitudes 0.5, 1.0, 2.0, 3.0 
#print out peak amplitude for each combination
print("The peak amplitudes:")
print(peakAmplitude(sinusoids(0.5, 200)))
print(peakAmplitude(sinusoids(1.0, 200)))
print(peakAmplitude(sinusoids(2.0, 200)))  
print(peakAmplitude(sinusoids(3.0, 200)))
print(peakAmplitude(sinusoids(0.5, 440)))
print(peakAmplitude(sinusoids(1.0, 440)))
print(peakAmplitude(sinusoids(2.0, 440)))  
print(peakAmplitude(sinusoids(3.0, 440)))    
print(peakAmplitude(sinusoids(0.5, 500)))
print(peakAmplitude(sinusoids(1.0, 500)))
print(peakAmplitude(sinusoids(2.0, 500)))  
print(peakAmplitude(sinusoids(3.0, 500)))


#Takes input array of audio samples and return the RMS amplitude
def peakRMS(audio_samp):
    sum = 0.0
    for i in range(0, len(audio_samp)):
    	sum += np.power(audio_samp[i], 2) #take the sum of squares
    sum /= len(audio_samp) #divide
    return np.sqrt(sum) * np.sqrt(2.0)

#print out RMS amplitude for each combination
print("The RMS amplitdues:")
print(peakRMS(sinusoids(0.5, 200)))
print(peakRMS(sinusoids(1.0, 200)))
print(peakRMS(sinusoids(2.0, 200)))  
print(peakRMS(sinusoids(3.0, 200)))
print(peakRMS(sinusoids(0.5, 440)))
print(peakRMS(sinusoids(1.0, 440)))
print(peakRMS(sinusoids(2.0, 440))) 
print(peakRMS(sinusoids(3.0, 440)))    
print(peakRMS(sinusoids(0.5, 500)))
print(peakRMS(sinusoids(1.0, 500)))
print(peakRMS(sinusoids(2.0, 500)))  
print(peakRMS(sinusoids(3.0, 500)))
	
	