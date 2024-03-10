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

    def _check_other_operant_type(self, other: TVector) -> None:
        if not isinstance(other, self.__class__):
            raise TypeError(
                "Right operant has wrong type. Expected: Vector, got: "
                f"{type(other).__name__}")

    def _check_other_operant_length(self, other: TVector) -> None:
        if len(self._vector) != len(other._vector):
            raise ValueError("Vectors must have the same length")

    @property
    def values(self) -> List[Real]:
        """Get vector values

        Returns
        -------
        list of Real
        """
        return self._vector

    def __add__(self, other: TVector) -> TVector:
        """Perform vector addition

        Parameters
        ----------
        other: Vector

        Returns
        -------
        Vector
        """
        self._check_other_operant_type(other)
        self._check_other_operant_length(other)

        return self.__class__(
            [v1_i + v2_i for v1_i, v2_i in zip(self.values, other.values)]
        )

    def __sub__(self, other: TVector) -> TVector:
        """Perform vector subtraction

        Parameters
        ----------
        other: Vector

        Returns
        -------
        Vector
        """
        self._check_other_operant_type(other)
        self._check_other_operant_length(other)

        return self.__class__(
            [v1_i - v2_i for v1_i, v2_i in zip(self.values, other.values)]
        )


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sum vectors elements
    """
    if len(vectors) == 0:
        raise ValueError("Input list cannot be empty")
    v_types = [isinstance(i, Vector) for i in vectors]
    if not all(v_types):
        raise TypeError("Elements of the input list must have type Vector")
    v_lenghts = [len(i) == len(vectors[0]) for i in vectors]
    if not all(v_lenghts):
        raise ValueError("Vectors must have the same length")

    return [sum(vector[i] for vector in vectors) for i in range(v_len)]
