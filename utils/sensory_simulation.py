import numpy as np
import librosa

class SensorySimulator:
    def simulate_vision(self):
        # Simulate visual input as an array of colors
        return np.random.rand(32, 32, 3)

    def simulate_hearing(self, file_path):
        # Load the audio file
        y, sr = librosa.load(file_path, sr=None)
        # Extract MFCC features
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        return np.mean(mfccs, axis=1)  # Aggregate to a 1D array
