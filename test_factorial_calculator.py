import builtins
import pytest
from factorial_calculator import get_factorial_input

def run_with_input(mock_inputs):
    """Helper to run get_factorial_input with a list of inputs."""
    inputs = iter(mock_inputs)
    def mock_input(prompt):
        return next(inputs)
    original_input = builtins.input
    builtins.input = mock_input
    try:
        return get_factorial_input()
    finally:
        builtins.input = original_input

def test_valid_input_first_try():
    assert run_with_input(['5']) == 5

def test_zero_input():
    assert run_with_input(['0']) == 0

def test_negative_then_valid():
    # First input is negative, second is valid
    assert run_with_input(['-3', '4']) == 4

def test_invalid_then_valid():
    # First input is not an integer, second is valid
    assert run_with_input(['abc', '7']) == 7

def test_multiple_invalid_then_valid():
    # Several invalid inputs before a valid one
    assert run_with_input(['', 'foo', '-1', '2']) == 2