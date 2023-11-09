"""File to define Fish class"""

class Fish:
    
    age: int

    def __init__(self, input_age: int = 0):
        """Constructor for fish object."""
        self.age = input_age
    
    def one_day(self):
        self.age += 1