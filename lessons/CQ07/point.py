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

    def scale_by(self, factor: int) -> None:
        """Method that scales point by a factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Method that constructs a new Point object."""
        new_point = Point(self.x * factor, self.y * factor)
        return new_point