#Import all the required libraries...
import librosa, librosa.display
import numpy as np, scipy, matplotlib.pyplot as plt, IPython.display as ipd


#Testing the librosa library...
(sig, rate) = librosa.load('data/waterSound1_2.wav', sr=None)
print(sig.size/rate)

#Testing the plot library...
'''
#Simple Plotting
#plt.plot(sig)
#plt.ylabel('Amplitude')
#plt.xlabel('Time')
#plt.show()
'''

#Testing if code works...
'''
T = 2.0 # seconds
f0 = 1047.0
sr = 22050
f = np.linspace(0, sr, 4096)
t = np.linspace(0, T, int(T*sr), endpoint=False) # time variable
x = 0.1*np.sin(2*numpy.pi*f0*t)
X = scipy.fft(x[10000:14096])
X_mag = np.absolute(X)
plt.figure(figsize=(14, 5))
plt.plot(f[:2000], X_mag[:2000]) # magnitude spectrum
plt.xlabel('Frequency (Hz)')
plt.show()
'''

#Creating Spectrogram of specified sound file...
def spectrogram(sig, rate):
	f = np.linspace(0, rate/2, 4096)
	X = scipy.fft.fft(sig[75000:125000])
	X_mag = np.absolute(X)
	plt.figure(figsize=(14,5))
	plt.plot(f[:4000], X_mag[:4000])
	plt.xlabel('Frequency (Hz)')
	plt.show()

spectrogram(sig, rate)

#Outputing the spectrograms as png's...
'''
for i in range(3): 
	for p in range(5):
		(sig, rate) = librosa.load('data/waterSound'+str(i+1)+'_'+str(p+1)+'.wav', sr=None)
		spectrogram(sig, rate)
		plt.savefig('spectrogram'+str(i+1)+'_'+str(p+1)+'.png')
'''
