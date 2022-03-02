import functools
import time


class Logger:
    logs: list = []

    def __init__(self, params: dict):
        self.params: dict = params

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if any((exc_type, exc_val, exc_tb)):
            react = self.params.get(exc_type.__name__, None)
            if not react:
                return False
            react["reaction"](*react["args"], **react["kwargs"])
            msg = {"time": time.asctime(), "status": "exception", "exc": f"{exc_type} {exc_tb} {exc_val}"}
            Logger.log_message(msg)
            return True

    @staticmethod
    def log_it(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            Logger.log_message(
                {"time": time.asctime(), "object": func.__name__, "status": "started", "args": args, "kwargs": kwargs}
            )
            ret_val = func(*args, **kwargs)
            Logger.log_message(
                {"time": time.asctime(), "object": func.__name__, "status": "exited", "return_value": ret_val}
            )
            return ret_val

        return wrapper

    @staticmethod
    def log_message(msg):
        Logger.logs.append(msg)


@Logger.log_it
def dummy1(*args, **kwargs):
    print(f"Inside dummy1 function with {args} and {kwargs}")
    raise KeyError


@Logger.log_it
def dummy2(*args, **kwargs):
    print(f"Inside dummy2 function with {args} and {kwargs}")
    raise AttributeError


@Logger.log_it
def dummy3(*args, **kwargs):
    print(f"Inside dummy3 function with {args} and {kwargs}")
    raise AssertionError


@Logger.log_it
def dummy4(*args, **kwargs):
    print(f"Inside dummy4 function with {args} and {kwargs}")


@Logger.log_it
def dummy5(*args, **kwargs):
    print(f"Inside dummy5 function with {args} and {kwargs}")


if __name__ == "__main__":
    params = {
        "AttributeError": {"reaction": dummy5, "args": (1, 2, 3), "kwargs": {}},
        "KeyError": {"reaction": dummy5, "args": ("dupa",), "kwargs": {}},
        "AssertionError": {"reaction": print, "args": ("not equal",), "kwargs": {}},
    }
    with Logger(params):
        tst = dummy1("Test1", 1, dupa=1, dupa2=1)
    with Logger(params):
        dummy2("Test2", 2, dupa=2, dupa2=2)
    with Logger(params):
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

# class Context:
#     def __init__(self, params: dict):
#         self.params: dict = params
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if any((exc_type, exc_val, exc_tb)):
#             react = self.params.get(exc_type.__name__, None)
#             if not react:
#                 return False
#             react["reaction"](*react["args"], **react["kwargs"])
#             return True
