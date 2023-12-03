"""Dictionary related utility functions."""
from csv import DictReader

__author__ = "730642587"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # loop through each element (dictionary) of the list
    for elem in table:
        # for each dictionary (elem), get the value at key "header" and add that to result
        result.append(elem[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key (header), make a dictionary entry with all the column values
        result[key] = column_values(table, key)
    return result


def head(input_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Gives first n rows of a table."""
    return_dict: dict[str, list[str]] = {}
    for i in input_table:
        if n >= len(input_table[i]):
            return input_table
        append_list: list[str] = []
        for j in range(n):
            append_list.append(input_table[i][j])
        return_dict[i] = append_list
    return return_dict


def select(input_table: dict[str, list[str]], copy_cols: list[str]) -> dict[str, list[str]]:
    """Returns a select few coloums in the input table."""
    return_dict: dict[str, list[str]] = {}
    for col in copy_cols:
        return_dict[col] = input_table[col]
    return return_dict


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concats two tables."""
    return_dict: dict[str, list[str]] = table1
    for col in table2:
        if col in return_dict:
            return_dict[col].extend(table2[col])
        else:
            return_dict[col] = table2[col]
    return return_dict


def count(input_list: list[str]) -> dict[str, int]:
    """Counts number of times an element appears in a col."""
    count_dict: dict[str, int] = {}
    for n in input_list:
        if n in count_dict:
            count_dict[n] += 1
        else:
            count_dict[n] = 1
    return count_dict