"""Point class creation."""

from __future__ import annotations


class Point:
    """Creates a class that makes points."""

    x: float
    y: float

    def __init__(self, x_input: float = 0.0, y_input: float = 0.0):
        """Class constructor."""
        self.x = x_input
        self.y = y_input
    
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

    def __mul__(self, factor: int | float) -> Point:
        """Overwrite the multiplication method."""
        return self.scale(factor)

    def __add__(self, amount: int | float) -> Point:
        """Overwrites add method."""
        return Point(self.x + amount, self.y + amount)
    
new_point: Point = Point()

print(new_point + 4.0)