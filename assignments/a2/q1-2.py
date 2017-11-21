import matplotlib.pyplot as plt
from pylab import *
import marsyas

### Question 1.2

sampRate = 44100 #sampling rate
m = marsyas.MarSystemManager()
data = []

system = marsyas.system_from_script_file("q12.mrs")
system.getControl("SoundFileSource/input/mrs_bool/hasData").to_bool()
while (system.getControl("SoundFileSource/input/mrs_bool/hasData").to_bool()):
    system.tick()
    data.extend(system.getControl("Selector/selection/mrs_realvec/processedData").to_realvec())
    data[-1] *=  sampRate/513
    
plt.title("Q1-2 F0 Contours: Melody from A1")
plt.plot(range(0, len(data)), data)
plt.show();

