from __future__ import annotations
from typing import Sequence, Any, Union


class Leaf:
    def __init__(self, values: Sequence[Any], next_node: Leaf = None, prev_node: Leaf = None):
        self.values: tuple = tuple(sorted(values))  # Pointer to sorted sequence of any type on hard drive
        self.head: Any = self.values[0]
        self.tail: Any = self.values[-1]
        self.next_node = next_node
        self.prev_node = prev_node

    def __iter__(self):
        self.active_node = self
        self.iterator = self.values.__iter__()
        return self

    def __next__(self):
        try:
            return self.iterator.__next__()
        except StopIteration:
            if not self.active_node.next_node:
                raise StopIteration
            self.active_node = self.active_node.next_node
            self.iterator = self.active_node.values.__iter__()
            return self.iterator.__next__()

    def find(self, searchable):
        if searchable in self.values:
            return searchable
        raise KeyError(f"There is no such key as {searchable} in database")


class IndexTree:
    def __init__(self, *items_to_index: Union[IndexTree, Leaf]):
        self.indexes: dict[tuple, Union[IndexTree, Leaf]] = {}
        self.head = items_to_index[0].head
        self.tail = items_to_index[-1].tail
        for _item in items_to_index:
            self.indexes[(_item.head, _item.tail)] = _item

    def find(self, searchable):
        for key, value in self.indexes.items():
            if key[0] <= searchable <= key[1]:
                return value.find(searchable)
        raise KeyError(f"There is no such key as {searchable} in database")


if __name__ == "__main__":
    l1 = Leaf([1, 2, 3, 4, 5])
    l2 = Leaf([6, 7, 8, 9, 10], prev_node=l1)
    l3 = Leaf([11, 12, 13, 14, 15], prev_node=l2)
    l4 = Leaf([16, 17, 18, 19, 20], prev_node=l3)
    l5 = Leaf([21, 22, 23, 24, 25], prev_node=l4)
    l6 = Leaf([26, 27, 28, 29, 30], prev_node=l5)
    l1.next_node = l2
    l2.next_node = l3
    l3.next_node = l4
    l4.next_node = l5
    l5.next_node = l6
    # for item in l1:
    #     print(item)
    mid_index1 = IndexTree(l1, l2)
    mid_index2 = IndexTree(l3, l4)
    mid_index3 = IndexTree(l5, l6)
    root_index = IndexTree(mid_index1, mid_index2, mid_index3)
    for i in range(1, 31):
        assert root_index.find(i) == i
