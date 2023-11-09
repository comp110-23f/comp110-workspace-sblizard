"""Point class creation."""

from __future__ import annotations


class Point:
    """Creates a class that makes points."""

    x: float
    y: float

    def __init__(self, x_input: float, y_input: float):
        """Class constructor."""
        self.x = x_input
        self.y = y_input

    def __init__(self):
        """Setting default values for Point object."""
        self.x = 0.0
        self.y = 0.0

    def scale_by(self, factor: int) -> None:
        """Method that scales point by a factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Method that constructs a new Point object."""
        new_point = Point(self.x * factor, self.y * factor)
        return new_point

    def __str__(self) -> str:
        """Overwrite the str method."""
        return "x: " + str(self.x) + "; y: " + str(self.y)

    def __mul__(self, factor: int) -> Point:
        """Overwrite the multiplication method."""
        return self.scale(factor)
    
    def __mul__(self, factor: float) -> Point:
        """Overwrite multiplication method for a float factor."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, amount: float) -> Point:
        """Overwrites add method."""
        return Point(self.x + amount, self.y + amount)
    
    def __add__(self, amount: int) -> Point:
        """Overwrites add method with an int."""
        return Point(self.x + amount, self.y + amount)