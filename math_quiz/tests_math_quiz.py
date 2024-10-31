import unittest
from math_quiz import generate_random_integer, choose_random_operator, create_math_problem

class TestMathQuiz(unittest.TestCase):

    def test_generate_random_integer(self):
        """Test if generated random integers are within the specified range."""
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_random_operator(self):
        """Test if the chosen operator is one of the expected operators."""
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            operator = choose_random_operator()
            self.assertIn(operator, valid_operators)

    def test_create_math_problem(self):
        """Test if math problems and answers are generated correctly."""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 6, '*', '4 * 6', 24)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
