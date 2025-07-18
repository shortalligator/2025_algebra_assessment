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
    elif operator1 == "/" and operator2 == "-":
        x = (c + b) * a
        equation = f"x/{a} - {b} = {c}"

    return equation, x

def hard_questions():

    operator1 = random.choice(["*", "/"])
    operator2 = random.choice(["+", "-"])

    if operator1 == "*":
        a = random.choice([i for i in range(-10, 11) if i != 0])
        b = random.choice([i for i in range(-10, 11) if i != 0])
        c = random.choice([i for i in range(-10, 11) if i != 0])
        d =  random.choice([i for i in range(-10, 11) if i != 0])
    else:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)

    # a(bx + c) = d
    if operator1 == "*" and operator2 == "+":
        x = (d - c) / b / a
        equation = f"{a}({b}x + {c}) = {d}"
    # a(bx - c) = d
    elif operator1 == "*" and operator2 == "-":
        x = (d + a * c) / (a * b)
        equation = f"{a}({b}x - {c}) = {d}"

    # (bx + c) / a = d
    elif operator1 == "/" and operator2 == "+":
        x = ((d * a) - c) / b
        equation = f"({b}x + {c}) / {a} = {d}"

    # (bx - c) / a = d
    elif operator1 == "/" and operator2 == "-":
        x = ((d * a) + c) / b
        equation = f"({b}x - {c}) / {a} = {d}"

    return equation, x

questions = easy_questions(), medium_questions(), hard_questions()
print(questions)