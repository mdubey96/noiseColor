import librosa
import matplotlib

(sig, rate) = librosa.load('data/Water Sound1 #1.wav', sr=None)

print(sig.size/rate)
