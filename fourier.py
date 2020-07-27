#Import all the required libraries...
import librosa, librosa.display
import numpy as np, scipy, matplotlib.pyplot as plt, IPython.display as ipd, pandas as pd, glob
from scipy.optimize import curve_fit


#Loading a sound file...
#(sig, rate) = librosa.load('data/soundFiles/whitenoise.wav', sr=None)


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
                return A*np.log(x) + B
        
        popt, pcov = curve_fit(f, n[50:4000], dB[50:4000])

        plt.figure(figsize=(14,5))
        
        plt.plot(n[50:4000], dB[50:4000])
        plt.plot(n[50:4000], f(n, *popt)[50:4000])
        plt.xscale('log')
        plt.xlabel('Frequency (Hz)')
        #plt.show()

#spec_log(sig, rate)


#Outputing the spectrograms as png's...
#all_files = glob.glob('/noiseColor/data/soundFiles/*')
for file in glob.glob('/home/titanslayer/2020internproj/noiseColor/data/soundFiles/*'):
        file = file.replace('/home/titanslayer/2020internproj/noiseColor/', '')
        (sig, rate) = librosa.load(file, sr=None)
        spec_log(sig, rate)

        file = file.replace('data/soundFiles/', '')
        file = file.replace('.wav', '.png')
        
        plt.savefig('log_'+file)
