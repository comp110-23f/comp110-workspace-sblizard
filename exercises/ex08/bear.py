"""File to define Bear class."""


class Bear:
    """Bear class."""
    
    age: int
    hunger_score: int

    def __init__(self, input_age: int = 0, input_hunger: int = 0):
        """Constructor for bear object."""
        self.age = input_age
        self.hunger_score = input_hunger
    
    def one_day(self):
        """One day passes for age."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Updates hunger_score based on how much it eats."""
        self.hunger_score += num_fish