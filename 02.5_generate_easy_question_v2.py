import random

def easy_questions():

    list_of_operators = ["+", "-", "*", "/"]

    operator = random.choice(list_of_operators)
    if operator == "*":
        a = random.choice([i for i in range(-10, 11) if i != 0])
        b = random.choice([i for i in range(-10, 11) if i != 0])
    else:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)


    # x+a = b
    if operator == "+":
        x = b - a
        equation = f"x + {a} = {b}"

    # x-a = b
    elif operator == "-":
        x = b + a
        equation = f"x - {a} = {b}"

    # xa = b
    elif operator == "*":
        x = b / a
        equation = f"x * {a} = {b}"

    # x/a = b
    else:
        x = b * a
        equation = f"x / {a} = {b}"

    return equation, x

print(easy_questions())