a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите третье число "))
if a >= b >= c:
    print(c, b, a)
if a <= b <= c:
    print(a, b, c)
if a >= c >= b:
    print(b, c, a)
if c >= a >= b:
    print(b, a, c)
if b >= a >= c:
    print(c, a, b)
