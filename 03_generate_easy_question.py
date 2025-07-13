import random
a = random.randint(-10, 10)
b = random.randint(-10, 10)
list_of_operators = ["+", "-", "*", "/"]

operator = random.choice(list_of_operators)


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

print(equation)

