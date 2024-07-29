import numpy as np
from models.model.py import build_complex_model
from utils.sensory_simulation import SensorySimulator
from utils.personality import Personality
from tests.ai_tests import SentientAITest

class SentientAI:
    def __init__(self):
        self.sensory_simulator = SensorySimulator()
        self.personality = Personality()
        self.memory = []
        self.model = build_complex_model()

    def process_input(self, vision_input, auditory_input):
        # Process sensory input using the neural network
        vision_result = self.model.predict(np.array([vision_input]))[0]
        auditory_result = np.mean(auditory_input)  # Simplified processing
        self.memory.append((vision_result, auditory_result))
        return vision_result, auditory_result

    def idle_think(self):
        # Generate a thought based on memory and personality
        if self.memory:
            memory_sample = random.choice(self.memory)
            thought = f"Based on my experience, I see {np.argmax(memory_sample[0])} and hear an average signal of {memory_sample[1]:.2f}."
            thought = self.personality.influence_thought(thought)
        else:
            thought = "I have no experiences to think about."
        print(f"Thought: {thought}")

def main():
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
