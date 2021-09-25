"""
Should support:
1. Addition
 - only floats input sanitization
2. Subtraction
3. Division
4. Multiplication
5. Powering
6. Factorial
"""
from typing import Union


class Calculator:
    SUPPORTED_TYPES: tuple = (int, float)

    def check_input(self, in_1: Union[int, float], in_2: Union[int, float]):
        if not isinstance(in_1, self.SUPPORTED_TYPES):
            raise ValueError(f"Float is expected. Input {in_1 = } is type of {type(in_1)}.")
        if not isinstance(in_2, self.SUPPORTED_TYPES):
            raise ValueError(f"Float is expected. Input {in_2 = } is type of {type(in_2)}.")

    def add(self, x: float, y: float) -> float:
        self.check_input(x, y)
        return x + y
