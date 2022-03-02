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
        self.leaves = []
        for num in numbers:
            self.insert(num)

    def insert(self, number: int):
        if not self.leaves:
            self.leaves.append(Leaf(number))
            return
        new_leaf = Leaf(number)
        for leaf in self.leaves:
            if not leaf.left:
                leaf.left = new_leaf
                self.leaves.append(new_leaf)
                break
            if not leaf.right:
                leaf.right = new_leaf
                self.leaves.append(new_leaf)
                break

    def reverse_tree(self):
        self._reverse(leaf=self.leaves[0])

    def _reverse(self, leaf: Leaf):
        if leaf.left:
            self._reverse(leaf=leaf.left)
        if leaf.right:
            self._reverse(leaf=leaf.right)
        leaf.left, leaf.right = leaf.right, leaf.left


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
    tree.insert(10)
    tree.reverse_tree()
