"""Establsiehs dictionary functions."""


__author__ = "730642687"


def invert(flip_dict: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary with flipped key and values."""
    return_dict: dict[str, str] = {}
    for i in flip_dict: 
        return_dict[flip_dict[i]] = i
    if len(flip_dict) != len(return_dict):
        raise KeyError("Your dictionary does not have all unique key values.")
    return return_dict


def invert_allow_dupes_keys(flip_dict: dict[str, str]) -> dict[str, str]:
    """Helper function for favorite_color."""
    return_dict: dict[str, str] = {}
    for i in flip_dict: 
        return_dict[flip_dict[i]] = i
    return return_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Returns the most popular color in a dictionary."""
    color_and_number: dict[str, str] = invert_allow_dupes_keys(color_dict)
    for i in color_and_number:
        color_and_number[i] = str(0)
    for j in color_dict:
        color_and_number[color_dict[j]] = str(1 + int(color_and_number[color_dict[j]]))
    key_of_max: str = ""
    max_count = 0
    for k in color_and_number:
        if int(color_and_number[i]) > max_count:
            max_count = int(color_and_number[i])
            key_of_max = k
    return key_of_max


def count(input_list: list[str]) -> dict[str, int]:
    """Cretes a dictionary that counts the number of times a string is in a list."""
    return_dict: dict[str, int] = {}
    for i in input_list:
        if i in return_dict:
            return_dict[i] += 1
        else:
            return_dict[i] = 1
    return return_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Function that alphebitizes a list into a dictionary."""
    lower_list: list[str] = []
    for i in range(len(input_list)):
        lower_list.append(input_list[i].lower())
    return_dict: dict[str, list[str]] = {}
    for k in lower_list:
        if k[0:1] in return_dict:
            return_dict[k[0:1]].append(k)
        else:
            return_dict[k[0:1]] = [k]
    print(return_dict)
    for j in input_list:
        return_dict[j.lower()[0:1]].remove(j.lower())
        return_dict[j.lower()[0:1]].append(j)
    return return_dict


def update_attendance(input_dict: dict[str, list[str]], day_of_week: str, student: str) -> dict[str, list[str]]:
    """Function to update attendce logs."""
    if (day_of_week in input_dict) is False:
        input_dict[day_of_week] = [student]
    else:
        if student not in input_dict[day_of_week]:
            input_dict[day_of_week].append(student)
    return input_dict