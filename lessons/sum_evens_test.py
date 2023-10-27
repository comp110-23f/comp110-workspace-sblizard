from lessons.sum_evens import sum_evens


def test_empty_sum() -> None:
    """sum_evens of empty list should be 0."""
    assert sum_evens([]) == 0


def test_list_lenghth_1() -> None:
    """Testing on length one."""
    test_list: list[int] = [2]
    assert sum_evens(test_list) == 2