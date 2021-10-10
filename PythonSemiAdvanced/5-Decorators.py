"""
Write a decorator that will read arguments passed to function and if error occurs will print them to console

error: Function>Dupa was ran with args:xxx and kwargs:xxx
"""
import traceback


def disable_at_night(func):

    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as exc:
            print(f"Error: {type(exc)}, Function {func.__name__}, ran with args:{args}, kwargs:{kwargs}")
            print(f"Traceback: {traceback.format_exc()}")

    return wrapper


@disable_at_night
def dummy(x, y, z, *, test1, test2, test3):
    x = 1 / 0


# disable_at_night(dummy)(1,2,3,test1=1, test2=2, test3=3)

output = dummy(1, 2, 3, test1=1, test2=2, test3=3)
print("pass")
