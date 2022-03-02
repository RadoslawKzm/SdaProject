from __future__ import annotations
from typing import Sequence, Any
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next_node: Node = None


class LinkedList:
    def __init__(self, sequence: Sequence[Any]):
        self.head = None
        if sequence:
            for item in sequence:
                self.head = Node(value=item, next_node=self.head)


def reverse_node(*, head_node: Node, prev_node: Node = None) -> Node:
    if not head_node.next_node:
        head_node.next_node = prev_node
        return head_node
    last_node = reverse_node(head_node=head_node.next_node, prev_node=head_node)
    head_node.next_node = prev_node
    return last_node


def reverse_linked_list(*, link_list: LinkedList) -> None:
    link_list.head = reverse_node(head_node=link_list.head)


if __name__ == '__main__':
    lst = LinkedList(sequence=[1, 2, 3, 4])
    reverse_linked_list(link_list=lst)
