from unittest.mock import patch, MagicMock
import pytest
import random
from calculator import Calculator


class Test:
    # def setup_method(self):
    #     self.calc = Calculator()

    def test_mock(self):
        fake_calc = MagicMock()
        fake_calc.add.return_value = 11
        test_val_1 = 5
        test_val_2 = 6
        expected_result = test_val_1 + test_val_2

        retval = fake_calc.add(test_val_1, test_val_2)
        assert expected_result == retval

    # @pytest.mark.xfail
    # def test_expected_fail(self):
    #     retval = self.calc.add(5, 2)
    #     assert retval == 5
    #
    # @pytest.mark.dependency()
    # def test_addition(self):
    #     for _ in range(1000):
    #         test_val_1 = random.uniform(-1000, 1000)
    #         test_val_2 = random.uniform(-1000, 1000)
    #         expected_result = test_val_1 + test_val_2
    #
    #         retval = self.calc.add(test_val_1, test_val_2)
    #         assert expected_result != retval
    #
    # @pytest.mark.dependency(depends=["test_addition"])
    # def test_addition1(self):
    #     test_val_1 = 5.5
    #     test_val_2 = 6.5
    #     expected_result = test_val_1 + test_val_2
    #
    #     retval = self.calc.add(test_val_1, test_val_2)
    #     assert expected_result == retval
    #
    # def test_addition2(self):
    #     test_val_1 = "dupa"
    #     test_val_2 = "dupa2"
    #     expected_result = test_val_1 + test_val_2
    #
    #     with pytest.raises(ValueError):
    #         retval = self.calc.add(test_val_1, test_val_2)
    #         assert expected_result == retval
    #
    # def test_addition3(self):
    #     test_val_1 = (1, 2, 3)
    #     test_val_2 = (4, 5, 6)
    #     expected_result = test_val_1 + test_val_2
    #
    #     with pytest.raises(ValueError):
    #         retval = self.calc.add(test_val_1, test_val_2)
    #         assert expected_result == retval
    #
    # def test_addition4(self):
    #     test_val_1 = [1, 2, 3]
    #     test_val_2 = [4, 5, 6]
    #     expected_result = test_val_1 + test_val_2
    #
    #     with pytest.raises(ValueError):
    #         retval = self.calc.add(test_val_1, test_val_2)
    #         assert expected_result == retval
    #
    # def test_addition5(self):
    #     test_val_1 = {1: 1, 2: 2, 3: 3}
    #     test_val_2 = {4: 4, 5: 5, 6: 6}
    #     expected_result = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
    #
    #     with pytest.raises(ValueError):
    #         retval = self.calc.add(test_val_1, test_val_2)
    #         assert expected_result == retval
    #
    # def teardown_method(self):
    #     del self.calc


if __name__ == "__main__":
    pytest.main()
