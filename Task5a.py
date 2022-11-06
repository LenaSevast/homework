def read_input():
    a = int(input("Введите первое число "))
    b = int(input("Введите второе число "))
    c = input("Введите знак  действия ")
    return a, b, c

def calculate(a, b, c):
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/" and b != 0:
        print(a / b)
    elif b == 0 and c == "/":
        print("Делить на 0 нельзя")
a, b, c = read_input()
calculate(a, b, c)