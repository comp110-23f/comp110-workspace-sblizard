"""Combining two lists into a dictionary."""


__author__ = "730642587"


def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Combines two lists into a dictionary."""
    return_dict: dict[str, int] = {}
    if len(str_list) != len(int_list):
        return return_dict
    for i in range(len(int_list)):
        return_dict[str_list[i]] = int_list[i]
    return return_dict