a = input("Введите номер месяца ")
a = int(a)
if a == 4 or a == 6 or a == 9 or a == 11:
    print("В этом месяце 30 дней")
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print("В этом месяце 31 день")
if a == 2:
    print("ФЕВРАЛЬ")
if a > 12 or a < 1:
    print("Такого месяца не существует")
