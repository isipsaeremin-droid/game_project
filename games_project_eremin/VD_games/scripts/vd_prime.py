import random
import math

def is_prime(number):
    """Проверяет, является ли число простым."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    # Проверяем делители до квадратного корня
    limit = int(math.sqrt(number)) + 1
    for divisor in range(3, limit, 2):
        if number % divisor == 0:
            return False
    return True

def generate_question():
    """Генерирует вопрос для игры."""
    # С вероятностью 50% выбираем простое или составное число
    if random.choice([True, False]):
        # Генерируем простое число
        while True:
            num = random.randint(2, 50)
            if is_prime(num):
                return num, "yes"
    else:
        # Генерируем составное число
        while True:
            num = random.randint(2, 50)
            if not is_prime(num) and num != 1:
                return num, "no"

def main():
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    
    correct_answers = 0
    rounds = 3  # Количество раундов
    
    for _ in range(rounds):
        number, correct_answer = generate_question()
        
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()
        
        # Проверяем ответ
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    # Если все ответы правильные
    if correct_answers == rounds:
        print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
