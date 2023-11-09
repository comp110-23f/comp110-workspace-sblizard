"""Functions to test my dictionary functions."""
from exercises.ex06.dictionary import invert, favorite_color, alphabetizer, update_attendance, count 
import pytest


__author__ = "730642587"


def test_invert_one_key_one_val() -> None:
    """Tests invert with one key."""
    assert invert({"hello": "hi"}) == {"hi": "hello"}


def test_invert_two_key_two_val() -> None:
    """Tests invert with two keys."""    
    assert invert({"hello": "hi", "goodbye": "bye"}) == {"hi": "hello", "bye": "goodbye"}


def test_invert_edge() -> None:
    """Tests invert if there are multible of the same keys."""
    with pytest.raises(KeyError):
        invert({"hello": "hi", "bye": "hi"})


def test_favorite_color() -> None:
    """Tests favorite_color."""
    assert favorite_color({"sean": "blue", "keith": "blue"}) == "blue"


def test_favorite_color_uppercase() -> None:
    """Tests favorite_color with uppercases."""
    assert favorite_color({"sean": "blue", "Keith": "Blue"}) == "blue"


def test_favorite_color_edge() -> None:
    """Tests favorite_color with empty dict."""
    assert favorite_color({}) == ""


def test_alphabetizer() -> None:
    """Tests alphabetizer with three eleements in a list."""
    assert alphabetizer(["apple", "bananna", "cat"]) == {"a": ["apple"], "b": ["bananna"], "c": ["cat"]}


def test_alphabetizer_2() -> None:
    """Tests alphabetizer with four eleements in a list two of them starting with an a."""
    assert alphabetizer(["apple", "bananna", "cat", "arrow"]) == {"a": ["apple", "arrow"], "b": ["bananna"], "c": ["cat"]}


def test_alphabetizer_edge() -> None:
    """Tests alphabetizer edge case."""
    assert alphabetizer([]) == {}


def test_update_attendence() -> None:
    """Tests update_attendence."""
    assert update_attendance({"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}, "Tuesday", "Vrinda") == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}


def test_update_attendence_2() -> None:
    """Tests update_attendence."""
    assert update_attendance({"Monday": ["Vrinda", "Kaleb"]}, "Monday", "Vrinda") != {"Monday": ["Virinda", "Vrinda", "Kaleb"]}


def test_update_attendence_edge() -> None:
    """Tests edge case of empty dict for update_attendence funciton."""
    assert update_attendance({}, "Monday", "Sean") == {"Monday": ["Sean"]}


def test_count() -> None:
    """Tests count function."""
    assert count(["a", "a", "b"]) == {"a": 2, "b": 1}


def test_count_2() -> None:
    """Tests count finciton when a and b are switched."""
    assert count(["b", "a", "a"]) == {"b": 1, "a": 2}


def test_count_edge() -> None:
    """Tests count funciton for empty list."""
    assert count([]) == {}