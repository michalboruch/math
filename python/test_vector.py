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
    expected_err_msg = "Vector elements must be type float"
    # act & assert
    with pytest.raises(ValueError) as exc:
        Vector(initial_list)
    assert str(exc.value) == expected_err_msg


def test_add__wrong_type():
    # arrange
    v1 = Vector([1, 2, 3])
    v2 = [4, 5, 6]
    expected_err_msg = "Right operant has wrong type. Expected: Vector, got: list"
    # act & assert
    with pytest.raises(TypeError) as exc:
        v1 + v2
    assert str(exc.value) == expected_err_msg


def test_add__wrong_vectors_len():
    # arrange
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2])
    expected_err_msg = "Vectors must have the same length"
    # act & arrange
    with pytest.raises(ValueError) as exc:
        v1 + v2
    assert str(exc.value) == expected_err_msg
