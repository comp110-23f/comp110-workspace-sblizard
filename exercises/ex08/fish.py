"""File to define Fish class."""


class Fish:
    """Fish class."""

    age: int

    def __init__(self, input_age: int = 0):
        """Constructor for fish object."""
        self.age = input_age
    
    def one_day(self):
        """One day passes for age."""
        self.age += 1