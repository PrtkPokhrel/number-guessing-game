
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
