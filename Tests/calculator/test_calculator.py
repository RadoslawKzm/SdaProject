from calculator import Calculator

def test_addition():
    test_val_1 = 5
    test_val_2 = 6
    expected_result = test_val_1 + test_val_2

    calc = Calculator()
    retval = calc.add(test_val_1, test_val_2)
    assert expected_result == retval