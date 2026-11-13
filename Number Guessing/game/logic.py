
import random

from config.settings import MIN_NUMBER, MAX_NUMBER


def generate_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def check_guess(guess, secret_number):
    if guess < secret_number:
        return "low"
    elif guess > secret_number:
        return "high"
    else:
        return "correct"


def generate_math_question():

    operators = ["+", "-", "*"]
    operator = random.choice(operators)

    if operator == "+":
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        answer = num1 + num2

    elif operator == "-":
        num1 = random.randint(10, 30)
        num2 = random.randint(1, num1)
        answer = num1 - num2

    else:
        num1 = random.randint(2, 10)
        num2 = random.randint(2, 10)
        answer = num1 * num2

    question = f"{num1} {operator} {num2} = ?"

    return question, answer


def generate_hint(secret_number):

    hints = [
        f"The secret number is {'even' if secret_number % 2 == 0 else 'odd'}.",

        f"The secret number is {'greater than' if secret_number > (MIN_NUMBER + MAX_NUMBER) // 2 else 'less than or equal to'} the middle of the range.",

        f"The secret number is divisible by 5: {'Yes' if secret_number % 5 == 0 else 'No'}."
    ]

    return random.choice(hints)
