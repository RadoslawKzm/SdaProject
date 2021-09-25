class Node:
    def __init__(self, *, name: str, value: int):
        self.name = name
        self.value = value
        self.nodes = []

    def __repr__(self) -> str:
        return f"{self.name}"


def recursive_algorithm(first_node: Node):
    """left to right walkthrough"""
    print(first_node.name)
    if not first_node.nodes:
        return
    for node in first_node.nodes:
        recursive_algorithm(node)
        print("pass")


if __name__ == "__main__":
    n1 = Node(name="n1", value=1)
    n2 = Node(name="n2", value=2)
    n3 = Node(name="n3", value=3)
    n4 = Node(name="n4", value=4)
    n5 = Node(name="n5", value=5)
    n1.nodes.extend([n2, n3])
    n2.nodes.extend([n4, n5])
    recursive_algorithm(n1)
