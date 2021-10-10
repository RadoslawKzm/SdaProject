"""
Write a decorator that will read arguments passed to function and if error occurs will print them to console

error: Function>Dupa was ran with args:xxx and kwargs:xxx
"""


def dummy(x, y, z, *, test1, test2, test3):
    x = 1 / 0
