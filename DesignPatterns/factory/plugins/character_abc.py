from abc import ABC, abstractmethod


class CharacterABC(ABC):
    @abstractmethod
    def move(self) -> None:
        """implement moving function"""

    @abstractmethod
    def make_noise(self) -> None:
        """implement noise funciton"""
