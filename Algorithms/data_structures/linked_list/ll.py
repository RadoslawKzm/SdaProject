class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


if __name__ == '__main__':
    n1 = Node(value=1, next_node=None)
    n2 = Node(value=2, next_node=n1)
    n3 = Node(value=3, next_node=n2)
    n4 = Node(value=4, next_node=n3)