import random
import unittest
from math_quiz import rand_num, rand_choice, math_ops


class TestMathGame(unittest.TestCase):

    def test_rand_num(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random.randint(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_rand_choice(self):
        # TODO
        for _ in range(100):
            result = rand_choice()
            self.assertIn(result, ['+', '-', '*'], f"Unexpected operation: {result}")

    def test_math_ops(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (4, 3, '-', '4 - 3', 1),
                (5, 5, '*', '5 * 5', 25),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                result = math_ops(num1, num2, operator)
                expected_result = (expected_problem, expected_answer)
                self.assertEqual(result, expected_result, f"Failed for {num1} {operator} {num2}")

if __name__ == "__main__":
    unittest.main()
