import random


def easy_questions():
    list_of_operators = ["+", "-", "*", "/"]

    operator = random.choice(list_of_operators)

    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    x = random.randint(-10, 10)

    # x+a = b
    if operator == "+":
        b = x + a
        equation = f"x + {a} = {b}"

    # x-a = b
    elif operator == "-":
        b = x - a
        equation = f"x - {a} = {b}"

    # xa = b
    elif operator == "*":
        b = x * a
        equation = f"x * {a} = {b}"

    # x/a = b
    else:
        x = a * b
        equation = f"x / {a} = {b}"

    return equation, x


print(easy_questions())
