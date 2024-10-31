from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:play_math_quiz',  # Main function to run
        ],
    },
    python_requires='>=3.6',
    install_requires=[
        # No external dependencies required for this project
    ],
)
