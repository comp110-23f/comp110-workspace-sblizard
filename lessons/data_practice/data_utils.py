"""Docstring."""
from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def col_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Return list of all values under a specific header."""
    results: list[str] = []
    for i in table:
        results.append(i[header])
    return results