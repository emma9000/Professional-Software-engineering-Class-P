import unittest
from db import create_table

from cost_manager import add_cost, view_costs, calculate_total_cost

class TestCostManager(unittest.TestCase):

    def setUp(self):
        # Clear the Cost table before each test
        costs = view_costs()
        for cost in costs:
            pass  # Here you would normally delete the cost from the database

    def test_calculate_total_cost(self):
        add_cost(100.0, "Groceries")
        add_cost(50.0, "Transport")
        total = calculate_total_cost()
        self.assertEqual(total, 150.0)

if __name__ == "__main__":
    create_table()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)