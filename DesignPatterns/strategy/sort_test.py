import strategy
import random


class Test:
    def test_bubble_sort(self):
        test_input = [5, 2, 9, 6, 5, 1, 8, 0, 2, 4, 5]
        test_output = [0, 1, 2, 2, 4, 5, 5, 5, 6, 8, 9]
        assert strategy.sort(sort_type="bubble", obj_to_sort=test_input) == test_output

    def test_selection_sort(self):
        test_input = [5, 2, 9, 6, 5, 1, 8, 0, 2, 4, 5]
        test_output = [0, 1, 2, 2, 4, 5, 5, 5, 6, 8, 9]
        assert strategy.sort(sort_type="selection", obj_to_sort=test_input) == test_output

    def test_insertion_sort(self):
        test_input = [5, 2, 9, 6, 5, 1, 8, 0, 2, 4, 5]
        test_output = [0, 1, 2, 2, 4, 5, 5, 5, 6, 8, 9]
        assert strategy.sort(sort_type="insertion", obj_to_sort=test_input) == test_output

    def test_random_sort(self):
        random.seed(10)
        test_input = [5, 2, 9, 6, 5, 1, 8, 0, 2, 4, 5]
        test_output = [1, 9, 2, 6, 2, 5, 5, 0, 8, 5, 4]
        assert strategy.sort(sort_type="random", obj_to_sort=test_input) == test_output
