"""Defining a class!"""

from __future__ import annotations

class Pizza:
    """My class to represent pizza!"""

    size: str
    toppings: int
    gliten_free: bool

    def __init__(self, size_input: str, toppings_input: int, gf: bool):
        """Pizza constructor."""
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gf
    
    def price(self) -> float:
        if self.size == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += .75*self.toppings
        if self.gluten_free:
            return cost + 1
        return cost

    def add_toppings_new_order(self, num_toppings: int) -> Pizza:
        """Making new pizza order using existing order."""
        new_pizza = Pizza(self.size, self.toppings + num_toppings, self.gliten_free)
        