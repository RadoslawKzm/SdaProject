from __future__ import annotations


class Node:
    def __init__(self, *, name: str, value: int, left: Node = None, right: Node = None):
        self.name = name
        self.value = value
        self.left_node: Node = left
        self.right_node: Node = right

    def __repr__(self) -> str:
        return f"{self.name}"


def reverse_tree(node: Node):
    if node.left_node:
        reverse_tree(node.left_node)
    if node.right_node:
        reverse_tree(node.right_node)
    node.left_node, node.right_node = node.right_node, node.left_node


if __name__ == "__main__":
    n4 = Node(name="n4", value=4)
    n5 = Node(name="n5", value=5)
    n2 = Node(name="n2", value=2, left=n4, right=n5)
    n6 = Node(name="n6", value=6)
    n3 = Node(name="n3", value=3, right=n6)
    n1 = Node(name="n1", value=1, left=n2, right=n3)
    reverse_tree(n1)
