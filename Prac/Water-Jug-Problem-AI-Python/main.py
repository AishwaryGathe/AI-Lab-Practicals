# Water Jug Problem 18/04/2023

jug1 = int(input("Enter the Capacity of Jug1 "))
jug2 = int(input("Enter the Capacity of Jug2 "))

x = 0
y = 0


def rule2(x, y):
    x = x
    y = jug2
    return x, y


def rule5(x, y):
    y = y - (jug1 - x)
    x = jug1
    return x, y


def rule7(x, y):
    x = x + y
    y = 0
    return x, y


while y != 2:
    (x, y) = rule2(x, y)
    print(x, y)

    if x + y <= jug1:
        (x, y) = rule7(x, y)
        print(x, y)
        (x, y) = rule2(x, y)
        print(x, y)
    (x, y) = rule5(x, y)
    print(x, y)

    if x == jug1 and y != 2:
        x = 0
        x = y
        y = 0
        print(x, y)
