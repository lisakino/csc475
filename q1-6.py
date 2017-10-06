freq = 300
data = generate_sin(freq, 0.5, amp =4.0)
data_probe1 = generate_sin(freq, 0.5, amp = 1)
noise = np.random.normal(0,0.5,len(data))
data_corrupted = data + noise 

# output the amplitude estimates of the corrupted data using different 
# methods. Experiment with finding amplitude of sinusoids of known frequencies
# in mixtures as well as with noise. try to understand what happens when 
# the phase is changed 
(round(peak_amplitude(data_corrupted), 3), round(rms_amplitude(data_corrupted), 3), 
round(dot_amplitude(data_corrupted, data_probe1), 3))

