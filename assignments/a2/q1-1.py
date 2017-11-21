import matplotlib.pyplot as plt
from pylab import *
import marsyas

### Question 1.1

sampRate = 44100 #sampling rate
m = marsyas.MarSystemManager()
data = []

system = marsyas.system_from_script_file("q11a.mrs") #replace this with correspond script for other audio
system.getControl("SoundFileSource/input/mrs_bool/hasData").to_bool()

while (system.getControl("SoundFileSource/input/mrs_bool/hasData").to_bool()):
    system.tick()
    data.extend(system.getControl("Selector/selection/mrs_realvec/processedData").to_realvec()) #Selector
    data[-1] *=  sampRate/513 #sampling rate divide by size of FFT

plt.title("Q1-1 Estimated F0: Melody from A1")
plt.plot(range(0, len(data)), data)
plt.show();

