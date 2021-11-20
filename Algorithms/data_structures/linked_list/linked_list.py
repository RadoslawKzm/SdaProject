from __future__ import annotations
from typing import Sequence, Any
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next_node: Node = None


class LinkedList:
    def __init__(self, sequence: Sequence[Any]):
        self.node = None
        if sequence:
            for item in sequence:
                self.node = Node(value=item, next_node=self.node)


if __name__ == '__main__':
    lst = LinkedList(sequence=[1, 2, 3, 4])
