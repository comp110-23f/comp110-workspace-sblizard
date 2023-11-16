"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730642587"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, input_list: list[int]):
        """Simpy object constructor."""
        self.values = input_list


    def __str__(self):
        """Overwrites the str methiod for Simpy objects."""
        return f'Simpy({self.values})'


    def fill(self, value: float, times: int) -> None:
        """fill methiod for Simpy objects."""
        self.values = []
        for i in range(times):
            self.values.append(value)


    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Arrange method for Simpy objects."""
        assert step != 0.0
        while abs(start) < abs(stop):
            self.values.append(start)
            start += step


    def __add__(self, value: Union[Simpy, float]) -> Simpy:
        """Overwrites the add method for Simpy Objects."""
        return_simpy: Simpy = Simpy([])
        if isinstance(value, Simpy):
            assert len(self.values) == len(value.values)
            for i in range(len(self.values)):
                return_simpy.values.append(self.values[i] + value.values[i])
            return return_simpy
        elif isinstance(value, float):
            for j in range(len(self.values)):
                return_simpy.values.append(self.values[j] + value)
            return return_simpy
            

    def __pow__(self, value: Simpy | float):
        """Overwrites the pow method for Simpy Objects."""
        return_simpy: Simpy = Simpy([])
        if isinstance(value, Simpy):
            assert len(self.values) == len(value.values)
            for i in range(len(self.values)):
                return_simpy.values.append(self.values[i] ** value.values[i])
            return return_simpy
        elif isinstance(value, float):
            for j in range(len(self.values)):
                return_simpy.values.append(self.values[j] ** value)
            return return_simpy

    def __eq__(self, object: Simpy | float):
        """Overwrites the == operator for Simpy objects."""
        return_simpy: Simpy = Simpy([])
        if isinstance(object, Simpy):
            assert len(self.values) == len(object.values)
            for i in range(len(self.values)):
                return_simpy.values.append(self.values[i] == object.values[i])
            return return_simpy
        elif isinstance(object, float):
            for j in range(len(self.values)):
                return_simpy.values.append(self.values[j] == object)
            return return_simpy
        

    def __gt__(self, object: Simpy | float):
        """Overwrites the > operator for Simpy objects."""
        return_simpy: Simpy = Simpy([])
        if isinstance(object, Simpy):
            assert len(self.values) == len(object.values)
            for i in range(len(self.values)):
                return_simpy.values.append(self.values[i] > object.values[i])
            return return_simpy
        elif isinstance(object, float):
            for j in range(len(self.values)):
                return_simpy.values.append(self.values[j] > object)
            return return_simpy
        
    def __getitem__(self, idx: int) -> float:
        """Overwrite the get item method for Simpy obects."""
        return self.values[idx]