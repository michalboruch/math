"""
Unit tests for vector module
"""

import pytest

from .vector import Vector


def test_init_vector():
    # arrange
    initial_list = [1, 2, 4.3]
    expected_repr = "Vector([1.0, 2.0, 4.3])"
    expected_value = initial_list
    # act
    v = Vector(initial_list)
    # assert
    assert str(v) == expected_repr
    assert v.values == expected_value


def test_init_vector__invalid_input():
    # arrange
    initial_list = [1, 2, "3"]
    expected_error_msg = "Vector elements must be type float"
    # act & assert
    with pytest.raises(ValueError) as exc:
        Vector(initial_list)
    assert str(exc.value) == expected_error_msg
