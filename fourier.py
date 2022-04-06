#Import all the required libraries...
import librosa, librosa.display
import numpy as np, scipy, matplotlib.pyplot as plt, IPython.display as ipd, pandas as pd, glob
from scipy.optimize import curve_fit

#Creating a Spectrogram of specified sound file(simple)...
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
        global popt
        global pcov
        global noiseType
        
        n = np.linspace(0, rate/2, 4096)#4096
        X = scipy.fft.fft(sig[10000:50000])#25000; 125000
        X_mag = np.absolute(X)        
        dB = 20*np.log10(X_mag/np.amax(X_mag))

        def f(x, A, B):
                return A*np.log(x) + B
        
        popt, pcov = curve_fit(f, n[50:4000], dB[50:4000])
        #Use popt as the slope to compare to the other noises. 
        print(popt[0])

        if popt[0] < 1 and popt[0] > -1:
                print('The audio file is White noise.')
                noiseType = 'White Noise.'
        elif popt[0] < -2 and popt[0] > -8:
                print('The audio file is Pink noise.')
                noiseType = 'Pink Noise.'
        elif popt[0] < -8:
                print('The audio file is Brown noise.')
                noiseType = 'Brown Noise.'
        elif popt[0] > 2 and popt[0] < 8:
                print('The audio file is Blue noise.')
                noiseType = 'Blue Noise.'
        elif popt[0] > 8:
                print('The audio file is Violet noise.')
                noiseType = ' Violet Noise.'

        plt.figure(figsize=(14,5))
        
        plt.plot(n[50:4000], dB[50:4000])
        plt.plot(n[50:4000], f(n, *popt)[50:4000])
        plt.xscale('log')
        plt.xlabel('Frequency (Hz)')
        #plt.show()
        
#Outputting the spetrograms and showing the graph...
'''
(sig, rate) = librosa.load('marsData/soundFiles/ascam_sol0067.wav', sr=None)
spec_log(sig, rate)
'''

#Outputing the spectrograms as png's...
'''
for file in glob.glob('/home/titanslayer/2020internproj/noiseColor/marsData/soundFiles/*'):
        file = file.replace('/home/titanslayer/2020internproj/noiseColor/', '')
        (sig, rate) = librosa.load(file, sr=None)
        spec_log(sig, rate)

        file = file.replace('data/soundFiles/', '')
        file = file.replace('.wav', '.png')
        
        plt.savefig('log' + file)
'''

#Outputing the data into a single spectrogram.
'''
(sig, rate) = librosa.load('marsData/soundFiles/ascam_sol0123.wav', sr=None)
spec_log(sig, rate)

plt.savefig('ascam_sol0123.png')
'''
#Outputing the data & slopes to a text file water sound files...
'''
file = open('data_comparison.txt', 'w')

for files in glob.glob('/home/titanslayer/2020internproj/noiseColor/data/soundFiles/*'):
        files = files.replace('/home/titanslayer/2020internproj/noiseColor/', '')
        (sig, rate) = librosa.load(files, sr=None)
        spec_log(sig, rate)
        def define_noise():
                if abs(pop
        files = files.replace('data/soundFiles/', '')

        file.write(files + ' ; Slope=' + str(popt[0]) + ' ; Intercept=' + str(popt[1]) + ' ; Noise='+ '\n\n')

file.close()
'''


#Outputing the data & slopes to a text file Mars sound files...
'''
file = open('mars_datahold.txt', 'w')
for files in glob.glob('/home/titanslayer/2020internproj/noiseColor/marsData/soundFiles/*'):
        (sig, rate) = librosa.load(files, sr=None)
        spec_log(sig, rate)
        file.write(files + ' ; Slope=' + str(popt[0]) + ' ; Intercept=' + str(popt[1]) + ' ; Noise='+ '\n\n')
'''


'''
for files in glob.glob('/home/titanslayer/2020internproj/noiseColor/marsData/soundFiles/*'):
        if '0001' in files or '0004' in files or '0011' in files or '0038' in files or '0066' in files or '0067' in files or '0076' in files or '0079' in files or '0081' in files or '0096' in files or '0100' in files or '0114' in files or '0117' in files or '0120' in files:
                print(files)
                print('True')
                (sig, rate) = librosa.load(files, sr=None)
                spec_log(sig, rate)
                files = files.replace('/home/titanslayer/2020internproj/noiseColor/marsData/soundFiles/', '')
                file.write(files + ' ; Slope=' + str(popt[0]) + ' ; Intercept=' + str(popt[1]) + ' ; Noise=' + noiseType + '\n\n')

file.close()
'''
