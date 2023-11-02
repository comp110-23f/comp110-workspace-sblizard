"""Test my zip function."""


from lessons.zip import zip


__author__ = "730642587"


def test_empty_lists() -> None:
    """Zipping two empty lists returns an empty dictionary."""
    assert zip([], []) == {}


def test_even_number_of_elements() -> None:
    """Zipping two lists with an even number of elements works."""
    assert len(zip([1, 2, 3, 4], [3, 2, 1, 4])) == 4


def test_different_lengths() -> None:
    """Zipping two lists with different lengths returns an empty dictionary.""" 
    assert zip([1, 2], [1]) == {}