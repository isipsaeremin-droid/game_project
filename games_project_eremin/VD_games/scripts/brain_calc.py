#!/usr/bin/env python3
"""Game: Calculator."""

import random
import operator
import prompt


def generate_round():
    """Generate a math expression and its answer."""
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    operations = [
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul)
    ]
    op_symbol, op_func = random.choice(operations)
    
    question = f'{a} {op_symbol} {b}'
    correct_answer = op_func(a, b)
    
    return question, str(correct_answer)


def run_calc_game():
    """Run the calculator game."""
    print("VD-calc\n")
    
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    
    print('What is the result of the expression?')
    
    rounds = 3
    
    for i in range(rounds):
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
    run_calc_game()


if __name__ == '__main__':
    main()
