import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Concatenate, Flatten
from tensorflow.keras.models import Model

def image_feature_extractor():
    img_input = Input(shape=(32, 32, 3))
    x = tf.keras.layers.Conv2D(32, (3, 3), activation='relu')(img_input)
    x = tf.keras.layers.MaxPooling2D((2, 2))(x)
    x = tf.keras.layers.Conv2D(64, (3, 3), activation='relu')(x)
    x = tf.keras.layers.MaxPooling2D((2, 2))(x)
    x = tf.keras.layers.Conv2D(128, (3, 3), activation='relu')(x)
    x = tf.keras.layers.MaxPooling2D((2, 2))(x)
    x = tf.keras.layers.Flatten()(x)
    return Model(img_input, x)

def sound_feature_extractor():
    sound_input = Input(shape=(44, 13))  # Example shape for audio features
    y = tf.keras.layers.Conv1D(64, 3, activation='relu')(sound_input)
    y = tf.keras.layers.MaxPooling1D(2)(y)
    y = tf.keras.layers.Flatten()(y)
    return Model(sound_input, y)

def decision_making_model():
    img_features = image_feature_extractor()
    snd_features = sound_feature_extractor()
    
    img_input = img_features.input
    snd_input = snd_features.input
    
    img_out = img_features(img_input)
    snd_out = snd_features(snd_input)
    
    combined = Concatenate()([img_out, snd_out])
    x = Dense(512, activation='relu')(combined)
    x = Dense(256, activation='relu')(x)
    output = Dense(10, activation='softmax')(x)  # Adjust the output layer as needed
    
    return Model(inputs=[img_input, snd_input], outputs=output)
