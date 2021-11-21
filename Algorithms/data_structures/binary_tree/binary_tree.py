from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass
class Leaf:
    value: int
    left: Leaf = None
    right: Leaf = None


class BinaryTree:
    def __init__(self, numbers: Sequence[int]):
        # self.leaves: list[Leaf] = [Leaf(value=num) for num in numbers]
        # self.connect()
        # self.leaf = None
        self.leaves = []
        for num in numbers:
            self.insert(num)

    def connect(self):
        for leaf in self.leaves:
            val = leaf.value
            left_val = val * 2 - 1
            right_val = val * 2
            if not (left_val > len(self.leaves) - 1):
                leaf.left = self.leaves[left_val]
            if not (right_val > len(self.leaves) - 1):
                leaf.right = self.leaves[right_val]

    def insert(self, number: int):
        if not self.leaves:
            self.leaves.append(Leaf(number))
            return
        for leaf in self.leaves:
            if not leaf.left:
                leaf.left = Leaf(number)
                break
            if not leaf.right:
                leaf.right = Leaf(number)
                break


if __name__ == '__main__':
    nine = Leaf(value=9)
    eight = Leaf(value=8)
    seven = Leaf(value=7)
    six = Leaf(value=6)
    five = Leaf(value=5)
    four = Leaf(value=4, left=eight, right=nine)
    three = Leaf(value=3, left=six, right=seven)
    two = Leaf(value=2, left=four, right=five)
    one = Leaf(value=1, left=two, right=three)
    tree = BinaryTree(numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    # tree.insert(10)
