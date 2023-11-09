"""File to define Bear class"""

class Bear:
    
    age: int
    hunger_score: int

    def __init__(self, input_age: int = 0, input_hunger: int = 0):
       """Constructor for bear object."""
       self.age = input_age
       self.hunger_score = input_hunger
    
    def one_day(self):
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        self.hunger_score += num_fish

