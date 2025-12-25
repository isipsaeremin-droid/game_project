#!/usr/bin/env python3
"""Game: Greatest Common Divisor."""

import random
import prompt


def gcd(a, b):
    """Calculate Greatest Common Divisor using Euclid's algorithm."""
    while b:
        a, b = b, a % b
    return a


def generate_round():
    """Generate two numbers and their GCD."""
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f'{a} {b}'
    correct_answer = str(gcd(a, b))
    return question, correct_answer


def run_gcd_game():
    """Run the GCD game."""
    print("VD-gcd\n")
    
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    
    print('Find the greatest common divisor of given numbers.')
    
    rounds = 3
    
    for _ in range(rounds):
        question, correct_answer = generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ').strip()
        
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f'Congratulations, {name}!')


def main():
    run_gcd_game()


if __name__ == '__main__':
    main()
