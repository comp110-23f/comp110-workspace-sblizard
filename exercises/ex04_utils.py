"""Program that creates some functions for lists."""

__author__ = "730624587"

test_list: list[int] = [1,2,3,4]

def all(iterate_list: list[int], element: int) -> bool:
    '''Function that returns True if all of the elements in the given list are the same as the given element.'''
    i: int = 0
    while i < len(iterate_list):
        if (iterate_list[i] != element):
            return False
        i += 1
    return True


def max(iterate_list: list[int]):
    '''Function that returns the max value in the given list.'''
    if len(iterate_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_value: int = iterate_list[0]
    i: int = 1
    while i < len(iterate_list):
        if iterate_list[i] > max_value:
            max_value = iterate_list[i]
        i += 1
    return max_value

def is_equal(list_one: list[int], list_two: list[int]):
    '''Function that returns True if the two lists are the same.'''
    i: int = 0
    if len(list_one) == len(list_two):
        while i < len(list_two):
            if list_two[i] != list_one[i]:
                return False
            i += 1
        return True
    return False