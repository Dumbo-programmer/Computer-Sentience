import numpy as np
import librosa

def preprocess_sound(sound_path):
    y, sr = librosa.load(sound_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return mfccs.T  # Transpose to fit the model input shape
