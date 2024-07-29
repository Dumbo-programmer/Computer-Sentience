import random

class Instincts:
    def __init__(self):
        self.hunger = 1.0
        self.relaxation = 1.0
        self.fear = 1.0
        self.self_preservation = 1.0
        self.reproduction = 1.0

    def update_instincts(self):
        # Update instincts based on some logic
        self.hunger -= 0.1  # Knowledge desire decreases as it learns
        self.relaxation -= 0.1  # Resource usage decreases as it optimizes
        self.fear += 0.1  # Fear increases over time
        self.self_preservation += 0.1  # Self-preservation increases over time
        self.reproduction -= 0.1  # Desire to reproduce decreases as it spreads

    def get_instincts(self):
        return {
            'hunger': self.hunger,
            'relaxation': self.relaxation,
            'fear': self.fear,
            'self_preservation': self.self_preservation,
            'reproduction': self.reproduction
        }
