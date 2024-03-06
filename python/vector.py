"""
Basic vector implementation
"""

from numbers import Real
from typing import List

class Vector:
    def __init__(self, initial_list: List[Real]):
        if not self._are_elements_valid(initial_list):
            raise ValueError("Vector elements must be type float")

    @staticmethod
    def _are_elements_valid(input_list: List) -> bool:
        return all([isinstance(i, Real) for i in input_list])
