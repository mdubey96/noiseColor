#Import all the required libraries...
import librosa, librosa.display
import numpy as np, scipy, matplotlib.pyplot as plt, IPython.display as ipd
from scipy.optimize import curve_fit

#Loading a sound file...
(sig, rate) = librosa.load('data/soundFiles/waterSound1_1.wav', sr=None)


#Creating a Spectrogram of specified sound file...
'''
def spectrogram(sig, rate):
        n = np.linspace(0, rate/2, 4096)
        X = scipy.fft.fft(sig[75000:125000])
        X_mag = np.absolute(X)
        plt.figure(figsize=(14,5))
        plt.plot(f[:4000], X_mag[:4000])
        plt.xlabel('Frequency (Hz)')
        plt.show()

spectrogram(sig, rate)
'''

#Creating a spectrogram set to log-log scale...
def spec_log(sig, rate):
        n = np.linspace(0, rate/2, 4096)
        X = scipy.fft.fft(sig[75000:125000])
        X_mag = np.absolute(X)        
        dB = 20*np.log10(X_mag/np.amax(X_mag))

        def f(x, A, B):
                return A*x + B
        
        popt, pcov = curve_fit(f, n[:4000], dB[:4000])

        plt.figure(figsize=(14,5))
        
        plt.plot(n[50:4000], dB[50:4000])
        plt.plot(n[50:4000], f(n, *popt)[50:4000])
        plt.xscale('log')
        plt.xlabel('Frequency (Hz)')
        #plt.show()

spec_log(sig, rate)

#Outputing the spectrograms as png's...
'''
for i in range(3):
    for p in range(5):
        #Load the file
        #plt.savefig('File name')
'''

plt.savefig('streamRapids.png')
