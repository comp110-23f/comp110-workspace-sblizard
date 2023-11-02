"""Instantiating a class."""

from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) #constructor

#my_pizza.size = "large"
#my_pizza.toppings = 10
#my_pizza.gliten_free = True

print(my_pizza.size)

pizza2 = Pizza("medium", 5, False)

def price(input_pizza: Pizza) -> float:
    if input_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += (.75*input_pizza.toppings)
    if input_pizza.gluten_free:
        return cost + 1
    return cost

print(pizza2.price())