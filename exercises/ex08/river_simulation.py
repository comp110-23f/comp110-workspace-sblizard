"""Implemntation of river class."""

from exercises.ex08.river import River
from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

my_river: River = River(10, 2)

my_river.one_river_week()

print(my_river.view_river())