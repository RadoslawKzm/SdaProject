import functools
import time


class Logger:
    logs: list = []

    @staticmethod
    def log_it(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            Logger.logs.append(
                {"time": time.asctime(), "object": func.__name__, "status": "started", "args": args, "kwargs": kwargs}
            )
            ret_val = func(*args, **kwargs)
            Logger.logs.append(
                {"time": time.asctime(), "object": func.__name__, "status": "exited", "return_value": ret_val}
            )
            return ret_val

        return wrapper


@Logger.log_it
def dummy1(*args, **kwargs):
    print(f"Inside dummy1 function with {args} and {kwargs}")


@Logger.log_it
def dummy2(*args, **kwargs):
    print(f"Inside dummy2 function with {args} and {kwargs}")


@Logger.log_it
def dummy3(*args, **kwargs):
    print(f"Inside dummy3 function with {args} and {kwargs}")


@Logger.log_it
def dummy4(*args, **kwargs):
    print(f"Inside dummy4 function with {args} and {kwargs}")


@Logger.log_it
def dummy5(*args, **kwargs):
    print(f"Inside dummy5 function with {args} and {kwargs}")


if __name__ == "__main__":
    with context([{"exc": AttributeError, "reaction": print, "args": (1, 2, 3)},
                  {"exc": KeyError, "reaction": print, "args": "dupa"},
                  {"exc": AssertionError, "reaction": print, "args": "not equal"}]):
        dummy1("Test1", 1, dupa=1, dupa2=1)
    dummy2("Test2", 2, dupa=2, dupa2=2)
    dummy3("Test3", 3, dupa=3, dupa2=3)
    dummy4("Test4", 4, dupa=4, dupa2=4)
    dummy5("Test5", 5, dupa=5, dupa2=5)

"""



















"""

# def __init__(self, function):
#     self.function = function
#
# def __call__(self, *args, **kwargs):
#     self.logs.append(
#         {
#             "time": time.asctime(),
#             "object": self.function.__name__,
#             "status": "started",
#             "args": args,
#             "kwargs": kwargs,
#         }
#     )
#     ret_val = self.function(*args, **kwargs)
#     self.logs.append(
#         {"time": time.asctime(), "object": self.function.__name__, "status": "exited", "return_value": ret_val}
#     )
#     return ret_val
