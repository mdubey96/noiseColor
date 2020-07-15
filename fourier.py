#Import all the required libraries...
import librosa
import matplotlib.pyplot as plt
import numpy as np

#Testing the librosa library...
(sig, rate) = librosa.load('data/waterSound1_1.wav', sr=None)
print(sig.size/rate)

#Simple Plotting
plt.plot(sig)
plt.ylabel('Frequency')
plt.xlabel('Time')
plt.show()

