def read_input():
    n = int(input("Укажите развер вклада "))
    m = int(input("На какой срок делаете вклад "))
    return n, m
proc = 0.1
def calculate(n, m):
    total = n
    for i in range(m):
        total = total + total * 0.1
    print("Вы получите ", total)
n, m = read_input()
calculate(n, m)