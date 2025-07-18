import random


def hard_questions():

    operator1 = random.choice(["*", "/"])
    operator2 = random.choice(["+", "-"])


    a = random.choice([1, 10])
    b = random.choice([i for i in range(-10, 11) if i != 0])
    c = random.choice([i for i in range(-10, 11) if i != 0])
    d =  random.choice([i for i in range(-10, 11) if i != 0])


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


print(hard_questions())
