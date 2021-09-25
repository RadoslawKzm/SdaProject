import pytest
import random
from calculator import Calculator


def test_addition():
    for _ in range(1000):
        test_val_1 = random.uniform(-1000, 1000)
        test_val_2 = random.uniform(-1000, 1000)
        expected_result = test_val_1 + test_val_2

        calc = Calculator()
        retval = calc.add(test_val_1, test_val_2)
        assert expected_result == retval


def test_addition1():
    test_val_1 = 5.5
    test_val_2 = 6.5
    expected_result = test_val_1 + test_val_2

    calc = Calculator()
    retval = calc.add(test_val_1, test_val_2)
    assert expected_result == retval


def test_addition2():
    test_val_1 = "dupa"
    test_val_2 = "dupa2"
    expected_result = test_val_1 + test_val_2

    calc = Calculator()
    with pytest.raises(ValueError):
        retval = calc.add(test_val_1, test_val_2)
        assert expected_result == retval


def test_addition3():
    test_val_1 = (1, 2, 3)
    test_val_2 = (4, 5, 6)
    expected_result = test_val_1 + test_val_2

    calc = Calculator()
    with pytest.raises(ValueError):
        retval = calc.add(test_val_1, test_val_2)
        assert expected_result == retval


def test_addition4():
    test_val_1 = [1, 2, 3]
    test_val_2 = [4, 5, 6]
    expected_result = test_val_1 + test_val_2

    calc = Calculator()
    with pytest.raises(ValueError):
        retval = calc.add(test_val_1, test_val_2)
        assert expected_result == retval


def test_addition5():
    test_val_1 = {1: 1, 2: 2, 3: 3}
    test_val_2 = {4: 4, 5: 5, 6: 6}
    expected_result = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}

    calc = Calculator()
    with pytest.raises(ValueError):
        retval = calc.add(test_val_1, test_val_2)
        assert expected_result == retval


if __name__ == "__main__":
    pytest.main()
