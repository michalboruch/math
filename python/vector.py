"""
Basic vector implementation
"""

from numbers import Real
from typing import List, TypeVar

TVector = TypeVar("TVector", bound="Vector")


class Vector:
    def __init__(self, initial_list: List[Real]):
        if not self._are_elements_valid(initial_list):
            raise ValueError("Vector elements must be type float")
        self._vector = [float(i) for i in initial_list]

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}({self._vector})"

    @staticmethod
    def _are_elements_valid(input_list: List) -> bool:
        return all([isinstance(i, Real) for i in input_list])

    @property
    def values(self) -> List[Real]:
        return self._vector

    def __add__(self, other: TVector) -> TVector:
        if not isinstance(other, self.__class__):
            raise TypeError(
                "Right operant has wrong type. Expected: Vector, got: "
                f"{type(other).__name__}")
        if len(self._vector) != len(other._vector):
            raise ValueError("Vectors must have the same length")
