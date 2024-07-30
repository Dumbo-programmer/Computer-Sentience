import random

class Instincts:
    def __init__(self):
        self.hunger = 1.0
        self.relaxation = 1.0
        self.fear = 1.0
        self.self_preservation = 1.0
        self.reproduction = 1.0

    def update_instincts(self, model_performance=None, sensory_data=None):
        # Example of modifying instincts based on external factors
        if model_performance:
            self.hunger -= 0.1  # Adjust based on model performance
        if sensory_data:
            self.relaxation -= 0.1  # Adjust based on resource usage or stress
        self.fear += 0.1  # General behavior change
        self.self_preservation += 0.1
        self.reproduction -= 0.1

    def get_instincts(self):
        return {
            'hunger': self.hunger,
            'relaxation': self.relaxation,
            'fear': self.fear,
            'self_preservation': self.self_preservation,
            'reproduction': self.reproduction
        }
