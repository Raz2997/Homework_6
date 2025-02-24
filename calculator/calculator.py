import os
from typing import List, Type

class Calculation:
    """Represents a single arithmetic calculation."""
    def __init__(self, operand1: float, operand2: float, operation: str, result: float):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operation = operation
        self.result = result

    def __repr__(self) -> str:
        return f"{self.operand1} {self.operation} {self.operand2} = {self.result}"

class Calculations:
    """Stores a history of calculations."""
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Type[Calculation]) -> None:
        cls.history.append(calculation)
    
    @classmethod
    def get_last_calculation(cls) -> Type[Calculation]:
        return cls.history[-1] if cls.history else None
    
    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()

class Calculator:
    """Performs arithmetic calculations."""
    @staticmethod
    def add(a: float, b: float) -> float:
        result = a + b
        Calculations.add_calculation(Calculation(a, b, '+', result))
        return result
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        result = a - b
        Calculations.add_calculation(Calculation(a, b, '-', result))
        return result
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        result = a * b
        Calculations.add_calculation(Calculation(a, b, '*', result))
        return result
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        Calculations.add_calculation(Calculation(a, b, '/', result))
        return result
