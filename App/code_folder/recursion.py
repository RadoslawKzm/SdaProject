class Node:
    def __init__(self, *, name: str, value: int):
        self.name = name
        self.value = value
        self.nodes = []


if __name__ == '__main__':
    n1 = Node(name="n1", value=1)
    n2 = Node(name="n2", value=2)
    n3 = Node(name="n3", value=3)
    n4 = Node(name="n4", value=4)
    n5 = Node(name="n5", value=5)
