import random


def easy_questions():
    list_of_operators = ["+", "-", "*", "/"]

    operator = random.choice(list_of_operators)
    if operator == "*":
        a = random.choice([i for i in range(-10, 11) if i != 0])
        b = random.choice([i for i in range(-10, 11) if i != 0])
        c = random.choice([i for i in range(-10, 11) if i != 0])
    else:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)

    # x+a = b


    # return equation, x


print(easy_questions())
