a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите третье число "))

if a > b > c:
    print(c, b, a)
if b > a > c:
    print(c, a, b)
if c > a > b:
    print(b, a, c)
if c > b > a:
    print(a, b, c)
if b > c > a:
    print(a, c, b)
if a > c > b:
    print(b, c, a)
