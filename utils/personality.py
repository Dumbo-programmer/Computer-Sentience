import random

class Personality:
    def __init__(self):
        self.traits = {
            'curiosity': random.uniform(0, 1),
            'cautiousness': random.uniform(0, 1),
            'optimism': random.uniform(0, 1)
        }

    def influence_thought(self, thought):
        # Modify thought based on personality traits
        if self.traits['curiosity'] > 0.5:
            thought += " I wonder what else is out there."
        if self.traits['cautiousness'] > 0.5:
            thought += " I should be careful though."
        if self.traits['optimism'] > 0.5:
            thought += " Everything seems positive."
        return thought
