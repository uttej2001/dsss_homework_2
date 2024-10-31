# -*- coding: utf-8 -*-
import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer within a specified range.

    Parameters:
        min_value (int): The minimum boundary for the random integer.
        max_value (int): The maximum boundary for the random integer.

    Returns:
        int: A random integer within the range [min_value, max_value].
    """
    return random.randint(min_value, max_value)

def choose_random_operator():
    """
    Select a random mathematical operator from the list ['+', '-', '*'].

    Returns:
        str: A random operator as a string.
    """
    return random.choice(['+', '-', '*'])

def create_math_problem(num1, num2, operator):
    """
    Generate a math problem and its correct answer based on the operator.

    Parameters:
        num1 (int): The first number.
        num2 (int): The second number.
        operator (str): The mathematical operator ('+', '-', '*').

    Returns:
        tuple: A string of the problem and the correct answer as an integer.
    """
    problem_str = f"{num1} {operator} {num2}"
    # Fixed reversed '+' and '-' operations to ensure correct answers
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    return problem_str, answer

def play_math_quiz():
    """
    Main function for the Math Quiz Game.
    Presents the player with random math questions and evaluates their answers.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Challenge!")
    print("Try your best to solve the math problems correctly.\n")

    for i in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)  # fixed max value to 5 for integer compatibility
        operator = choose_random_operator()

        problem, correct_answer = create_math_problem(num1, num2, operator)
        print(f"\nQuestion {i}: {problem}")

        # Error handling to ensure the user enters a valid integer
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! Well done. You earned a point.")
            score += 1
        else:
            print(f"Oops, that's not correct. The correct answer was {correct_answer}.")

    print(f"\nQuiz Complete! Your final score is {score}/{total_questions}.")
    print("Thank you for playing!")

if __name__ == "__main__":
    play_math_quiz()
