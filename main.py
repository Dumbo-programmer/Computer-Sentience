import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
import random
from utils.sensory_simulation import SensorySimulator
from utils.instincts import Instincts
from utils.personality import Personality
import numpy as np

class SentientAI:
    def __init__(self):
        self.sensory_simulator = SensorySimulator()
        self.instincts = Instincts()
        self.personality = Personality()
        self.memory = []
        self.model = self.build_complex_model()

    def build_complex_model(self):
        model = Sequential()
        
        # First convolutional block
        model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
        model.add(BatchNormalization())
        model.add(MaxPooling2D((2, 2)))
        model.add(Dropout(0.25))
        
        # Second convolutional block
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(BatchNormalization())
        model.add(MaxPooling2D((2, 2)))
        model.add(Dropout(0.25))
        
        # Third convolutional block
        model.add(Conv2D(128, (3, 3), activation='relu'))
        model.add(BatchNormalization())
        model.add(MaxPooling2D((2, 2)))
        model.add(Dropout(0.25))
        
        # Fully connected layer
        model.add(Flatten())
        model.add(Dense(512, activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))
        
        # Output layer
        model.add(Dense(10, activation='softmax'))
        
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        
        return model

    def process_input(self, vision_input, auditory_input):
        # Process sensory input using the neural network
        vision_result = self.model.predict(np.array([vision_input]))[0]
        auditory_result = np.mean(auditory_input)  # Simplified processing
        self.memory.append((vision_result, auditory_result))
    
         # Generate a decision based on vision and auditory results
        decision = self.generate_decision(vision_result, auditory_result)
    
        return vision_result, auditory_result, decision
    def generate_decision(self, vision_result, auditory_result):
        # Simplified decision logic for example purposes
        if np.argmax(vision_result) > 5:
            decision = "Object detected is likely significant."
        else:
            decision = "Object detected is likely insignificant."
        return decision

    def idle_think(self):
        # Generate a thought based on memory, personality, and instincts
        if self.memory:
            memory_sample = random.choice(self.memory)
            thought = f"Based on my experience, I see {np.argmax(memory_sample[0])} and hear an average signal of {memory_sample[1]:.2f}."
            thought = self.personality.influence_thought(thought, memory_sample[0], memory_sample[1])
        else:
            thought = "I have no experiences to think about."
        
        # Influence thought based on instincts
        instincts = self.instincts.get_instincts()
        if instincts['hunger'] > 0.5:
            thought += " I feel the need to learn more."
        if instincts['fear'] > 0.5:
            thought += " I'm worried about being turned off."
        
        print(f"Thought: {thought}")

    def update_instincts(self):
        self.instincts.update_instincts()

def main():
    from tests.ai_tests import SentientAITest  # Moved inside the function to avoid circular import
    ai = SentientAI()
    tester = SentientAITest(ai)

    print("Evaluating behavior...")
    tester.evaluate_behavior()

    print("Analyzing thoughts...")
    tester.analyze_thoughts()

    print("Testing consistency...")
    tester.test_consistency()

    print("Testing adaptability...")
    tester.test_adaptability()

if __name__ == "__main__":
    main()
