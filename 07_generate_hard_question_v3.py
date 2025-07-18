import random


def hard_questions():
    operator1 = "*"
    operator2 = random.choice(["+", "-"])

    a = random.randint(-10, 10)
    b = random.randint(-20, 20)
    c = random.randint(-20, 20)
    x = random.randint(-20, 20)

    # a(bx + c) = d
    if operator1 == "*" and operator2 == "+":
        d = a * (b * x + c)
        equation = f"{a}({b}x + {c}) = {d}"

    # a(bx - c) = d
    else:
        d = a * (b * x - c)
        equation = f"{a}({b}x - {c}) = {d}"

    return equation, x


print(hard_questions())
