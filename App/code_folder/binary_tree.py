from __future__ import annotations


class Node:
    def __init__(self, *, name: str, value: int, left: Node, right: Node):
        self.name = name
        self.value = value
        self.left_node: Node = left
        self.right_node: Node = right

    def __repr__(self) -> str:
        return f"{self.name}"
