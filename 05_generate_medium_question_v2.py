import random


def medium_questions():

    operator1 = random.choice(["*", "/"])
    operator2 = random.choice(["+", "-"])

    if operator1 == "*":
        a = random.choice([i for i in range(-10, 11) if i != 0])
        b = random.choice([i for i in range(-10, 11) if i != 0])
        c = random.choice([i for i in range(-10, 11) if i != 0])
    else:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)

    # ax + b = c
    if operator1 == "*" and operator2 == "+":
        x = (c - b) / a
        equation = f"{a}x + {b} = {c}"
    # ax - b = c
    elif operator1 == "*" and operator2 == "-":
        x = (c + b) / a
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
