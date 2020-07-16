#Import all the required libraries...
import librosa, librosa.display
import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd


#Testing the librosa library...
(sig, rate) = librosa.load('data/waterSound1_1.wav', sr=None)
print(sig.size/rate)

#Simple Plotting
#plt.plot(sig)
#plt.ylabel('Amplitude')
#plt.xlabel('Time')
#plt.show()

#Testing if code works.
'''
T = 2.0 # seconds
f0 = 1047.0
sr = 22050
f = numpy.linspace(0, sr, 4096)
t = numpy.linspace(0, T, int(T*sr), endpoint=False) # time variable
x = 0.1*numpy.sin(2*numpy.pi*f0*t)
X = scipy.fft(x[10000:14096])
X_mag = numpy.absolute(X)
plt.figure(figsize=(14, 5))
plt.plot(f[:2000], X_mag[:2000]) # magnitude spectrum
plt.xlabel('Frequency (Hz)')
plt.show()
'''

#Spectrogram 1
print(rate)

f = numpy.linspace(0, rate/2, 4096)
X = scipy.fft.fft(sig[75000:125000])
X_mag = numpy.absolute(X)
plt.figure(figsize=(14,5))
plt.plot(f[:4000], X_mag[:4000])
plt.xlabel('Frequency (Hz)')
plt.show()

