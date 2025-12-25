import random

def generate_progression():
    """Генерирует арифметическую прогрессию со скрытым элементом."""
    length = random.randint(5, 10)  # Длина от 5 до 10
    start = random.randint(1, 20)   # Начальное число
    step = random.randint(1, 10)    # Шаг прогрессии
    
    # Создаём прогрессию
    progression = [start + i * step for i in range(length)]
    
    # Выбираем случайную позицию для скрытия
    hidden_index = random.randint(0, length - 1)
    hidden_value = progression[hidden_index]
    
    # Заменяем скрытый элемент на ".."
    progression[hidden_index] = ".."
    
    return progression, hidden_value

def main():
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")
    
    correct_answers = 0
    rounds = 3  # Количество раундов
    
    for _ in range(rounds):
        progression, correct_answer = generate_progression()
        
        # Преобразуем прогрессию в строку для вывода
        progression_str = " ".join(str(x) for x in progression)
        print(f"Question: {progression_str}")
        
        user_answer = input("Your answer: ")
        
        try:
            # Пытаемся преобразовать ответ в число
            user_answer = int(user_answer)
        except ValueError:
            # Если не число, считаем неправильным
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
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
