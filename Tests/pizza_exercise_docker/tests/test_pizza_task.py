import pytest
from Tests.pizza_exercise_docker.code_folder.pizza_task import Pizza
from math import pi


class Test:

    def setup_method(self):
        self.pizza1 = Pizza(name="Kaprikosa", d_cm=32, price_zl=25, costs_zl=5, toppings=["ser", "szynka", "pieczarki"])
        self.pizza2 = Pizza(name="Margerita", d_cm=40, price_zl=30, costs_zl=10, toppings=["ser"])
        self.pizza3 = Pizza(name="Margerita", d_cm=40, price_zl=30, costs_zl=10, toppings=[])

    def test_how_many_pizzas(self):
        expected_value = 3
        actual_value = Pizza.how_many_pizzas_done
        assert actual_value == expected_value

    def test_overall_gross_income(self):
        expected_value = 85
        actual_value = Pizza.overall_gross_income
        assert actual_value == expected_value

    def test_overall_costs(self):
        expected_value = 25
        actual_value = Pizza.overall_costs
        assert actual_value == expected_value

    def test_net_income(self):
        expected_value = 60
        actual_value = Pizza.calculate_net_income()
        assert actual_value == expected_value

    def test_ratio(self):
        expected_value = pi * (32 / 2) ** 2 / 25
        actual_value = self.pizza1.get_ratio()
        assert actual_value == expected_value

    def test_gt(self):
        expected_value = False
        actual_value = self.pizza1 > self.pizza2
        assert actual_value == expected_value

    def test_ge(self):
        expected_value = False
        actual_value = self.pizza1 >= self.pizza2
        assert actual_value == expected_value

    def test_lt(self):
        expected_value = True
        actual_value = self.pizza1 < self.pizza2
        assert actual_value == expected_value

    def test_le(self):
        expected_value = True
        actual_value = self.pizza1 <= self.pizza2
        assert actual_value == expected_value

    def test_eq(self):
        expected_value = False
        actual_value = self.pizza1 == self.pizza2
        assert actual_value == expected_value

    def test_toppings(self):
        expected_value = ["ser", "szynka", "pieczarki"]
        actual_value = self.pizza1.toppings
        assert actual_value == expected_value

    def test_toppings_empty(self):
        expected_value = []
        actual_value = self.pizza3.toppings
        assert actual_value == expected_value

    def teardown_method(self):
        Pizza.how_many_pizzas_done = 0
        Pizza.overall_gross_income = 0
        Pizza.overall_costs = 0




if __name__ == '__main__':
    pytest.main()