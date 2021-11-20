def dummy1(*args, **kwargs):
    print(f"Inside dummy1 function with {args} and {kwargs}")


def dummy2(*args, **kwargs):
    print(f"Inside dummy2 function with {args} and {kwargs}")


def dummy3(*args, **kwargs):
    print(f"Inside dummy3 function with {args} and {kwargs}")


def dummy4(*args, **kwargs):
    print(f"Inside dummy4 function with {args} and {kwargs}")


def dummy5(*args, **kwargs):
    print(f"Inside dummy5 function with {args} and {kwargs}")


if __name__ == '__main__':
    dummy1("Test1", 1, dupa=1, dupa2=1)
    dummy2("Test2", 2, dupa=2, dupa2=2)
    dummy3("Test3", 3, dupa=3, dupa2=3)
    dummy4("Test4", 4, dupa=4, dupa2=4)
    dummy5("Test5", 5, dupa=5, dupa2=5)
