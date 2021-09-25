import time


def timer(func):
    def wrapper(*args, **kwargs):
        tstart = time.time()
        retval = func(*args, **kwargs)
        print(f"Elapsed time = {time.time() - tstart:0.4f}s")

    return wrapper
