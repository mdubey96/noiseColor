#Import all the required libraries...
import librosa
import matplotlib.pyplot as plt, IPython.display as ipd
import numpy as np

#Testing the librosa library...
(sig, rate) = librosa.load('data/waterSound1_1.wav', sr=None)
print(sig.size/rate)

#Simple Plotting
#plt.plot(sig)
#plt.ylabel('Frequency')
#plt.xlabel('Time')
#plt.show()

#Spectrogram 1

x, sr = librosa.load('data/waterSound2_1.wav')
ipd.Audio(x, rate=sr)
