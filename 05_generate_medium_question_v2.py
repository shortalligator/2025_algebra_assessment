import random


def medium_questions():

    operator1 = random.choice(["*", "/"])
    operator2 = random.choice(["+", "-"])


    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    x = random.randint(-10, 10)

    # ax + b = c
    if operator1 == "*" and operator2 == "+":
        c = a * x + b
        equation = f"{a}x + {b} = {c}"
    # ax - b = c
    elif operator1 == "*" and operator2 == "-":
        c = a * x - b
        equation = f"{a}x - {b} = {c}"
    # x / a + b = c
    elif operator1 == "/" and operator2 == "+":
        x = (c - b) * a
        equation = f"x/{a} + {b} = {c}"
    # x / a - b = c
    else:
        x = (c + b) * a
        equation = f"x/{a} - {b} = {c}"

    return equation, x

print(medium_questions())
