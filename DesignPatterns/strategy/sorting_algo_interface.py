from __future__ import annotations
import copy
from abc import ABC, abstractmethod
import random

from Algorithms.sortings.buble_sort import bubble_sort
from Algorithms.sortings.insertion_sort import insertion_sort
from Algorithms.sortings.selection_sort import selection_sort


class SortingStrategyABC(ABC):
    name: str

    @staticmethod
    @abstractmethod
    def inplace_sort(obj_to_sort: list[int]) -> None:
        """Implement inplace sorting algorithm"""

    @staticmethod
    @abstractmethod
    def sorted(self, obj_to_sort: list[int]) -> list[int]:
        """Implement sorting algorithm with return value and non changing input"""

    @classmethod
    def subclasses_as_dict(cls) -> dict[str, SortingStrategyABC]:
        return {subclass.name: subclass for subclass in cls.__subclasses__()}


class BubbleSortStrategy(SortingStrategyABC):
    name = "bubble"

    @staticmethod
    def inplace_sort(obj_to_sort: list[int]) -> None:
        bubble_sort(obj_to_sort)

    @staticmethod
    def sorted(self, obj_to_sort: list[int]) -> list[int]:
        """Implement sorting algorithm with return value and non changing input"""
        copied_obj = copy.copy(obj_to_sort)
        bubble_sort(copied_obj)
        return copied_obj


class InsertionSortStrategy(SortingStrategyABC):
    name = "insertion"

    @staticmethod
    def inplace_sort(obj_to_sort: list[int]) -> None:
        insertion_sort(obj_to_sort)

    @staticmethod
    def sorted(self, obj_to_sort: list[int]) -> list[int]:
        """Implement sorting algorithm with return value and non changing input"""
        copied_obj = copy.copy(obj_to_sort)
        insertion_sort(copied_obj)
        return copied_obj


class SelectionSortStrategy(SortingStrategyABC):
    name = "selection"

    @staticmethod
    def inplace_sort(obj_to_sort: list[int]) -> None:
        selection_sort(obj_to_sort)

    @staticmethod
    def sorted(self, obj_to_sort: list[int]) -> list[int]:
        """Implement sorting algorithm with return value and non changing input"""
        copied_obj = copy.copy(obj_to_sort)
        selection_sort(copied_obj)
        return copied_obj


class RandomSortStrategy(SortingStrategyABC):
    name = "random"

    @staticmethod
    def inplace_sort(obj_to_sort: list[int]) -> None:
        random.shuffle(obj_to_sort)

    @staticmethod
    def sorted(self, obj_to_sort: list[int]) -> list[int]:
        """Implement sorting algorithm with return value and non changing input"""
        copied_obj = copy.copy(obj_to_sort)
        random.shuffle(copied_obj)
        return copied_obj
