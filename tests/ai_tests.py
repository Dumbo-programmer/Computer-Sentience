import os
import numpy as np
from sklearn.model_selection import train_test_split
from main import SentientAI

class SentientAITest:
    def __init__(self, ai_model):
        self.ai = ai_model

    def load_data(self, data_dir='data'):
        image_data = np.load(os.path.join(data_dir, 'image_data.npy'))
        sound_data = np.load(os.path.join(data_dir, 'sound_data.npy'))
        return image_data, sound_data

    def prepare_labels(self, num_samples):
        return np.random.randint(0, 2, size=(num_samples,))

    def train_model(self, image_data, sound_data):
        labels = self.prepare_labels(len(image_data))
        X_train_img, X_test_img, X_train_snd, X_test_snd, y_train, y_test = train_test_split(
            image_data, sound_data, labels, test_size=0.2
        )
        # Dummy training step, assuming the decision_model trains on image data
        self.ai.decision_model.train(X_train_img, y_train)  # Adjust according to your actual implementation
        test_loss, test_accuracy = self.ai.decision_model.evaluate(X_test_img, y_test)
        print(f"Test Loss: {test_loss}, Test Accuracy: {test_accuracy}")

    def evaluate_behavior(self):
        for _ in range(5):
            vision_input = self.ai.sensory_simulator.simulate_vision()
            auditory_input = self.ai.sensory_simulator.simulate_hearing('data/auditory_data/sample.mp3')
            vision_result, auditory_result, decision = self.ai.process_input(vision_input, auditory_input)
            print(f"Vision result: {vision_result}, Auditory result: {auditory_result}, Decision: {decision}")

    def analyze_thoughts(self):
        self.ai.idle_think()

    def test_consistency(self):
        for _ in range(3):
            self.analyze_thoughts()

    def test_adaptability(self):
        new_vision_input = np.ones((32, 32, 3))  # Example new input
        new_auditory_input = np.zeros((13, 44))  # Example new input
        vision_result, auditory_result, decision = self.ai.process_input(new_vision_input, new_auditory_input)
        print(f"New Vision result: {vision_result}, New Auditory result: {auditory_result}, New Decision: {decision}")
        self.analyze_thoughts()

if __name__ == "__main__":
    ai_model = SentientAI()  # Initialize your AI model here
    tester = SentientAITest(ai_model)
    
    # Load data and train the model
    image_data, sound_data = tester.load_data()
    tester.train_model(image_data, sound_data)
    
    # Perform tests
    tester.evaluate_behavior()
    tester.test_consistency()
    tester.test_adaptability()
