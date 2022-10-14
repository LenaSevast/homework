print("Задачка А")
def read_input():
    a = int(input("Введите первое число "))
    b = int(input("Введите второе число "))
    c = input("Знак действия ")
    return a, b, c


def calculate(a, b, c):
    if c == "+":
        print(a + b)
    elif c == "-":
       print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
       print(a / b)


a, b, c = read_input()

calculate(a, b, c)

print("Задачка Б")
bank_percent = 0.1


def read_inp():
    n = int(input("Введите сумму вклада "))
    m = int(input("На какой срок "))
    return n, m


def colcul(n, m):
    total_money = n
    for i in range(m):
        total_money = total_money + total_money * 0.1
    print(total_money)
n, m = read_inp()
colcul(n, m)
