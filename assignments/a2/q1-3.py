import matplotlib.pyplot as plt
from pylab import *
import marsyas

### Question 1.3 

m = marsyas.MarSystemManager()
data = []
sampRate = 44100 #sampling rate

system = marsyas.system_from_script_file("q13.mrs")
system.getControl("SoundFileSource/input/mrs_bool/hasData").to_bool()
while (system.getControl("SoundFileSource/input/mrs_bool/hasData").to_bool()):
    system.tick()
	data.extend(system.getControl("Sum/summer/mrs_realvec/processedData").to_realvec())
    data[-1] *=  sampRate/513

plt.plot(range(0, len(data)), data)