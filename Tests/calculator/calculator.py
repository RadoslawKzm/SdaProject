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


class Calculator:
    @staticmethod
    def add(x: float, y: float) -> float:
        if not isinstance(x, float):
            raise ValueError(f"Float is expected. Input {x = } is type of {type(x)}.")
        if not isinstance(y, float):
            raise ValueError(f"Float is expected. Input {y = } is type of {type(y)}.")
        return x + y
