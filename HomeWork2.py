"""
Написать программу, считывающую список чисел и выводящую список в обратном порядке.
"""
a = input("Введите список чисел ").split()
lst = []
for i in range(len(a)):
    lst.append(int(a[i]))

lst.reverse()
print(lst)
"""
Написать программу, считывающую список чисел и выводящую:
!Дополнительно: Реализовать функцию для поиска среднего арифметического, принимающую на вход список и возвращающую число:

def mean(my_list):
    # тут код
    return mean_number

a. минимальное число 
б. максимальное число 
в. среднее арифметическое чисел из списка 
г. отсортированный список 
"""

my_list = input("Введите список чисел ").split()
lst = []
for i in range(len(my_list)):
    lst.append(int(my_list[i]))

print("Минимальное число ", min(lst))
print("Максимальное число ", max(lst))

def mean(my_list):
    mean_number = sum(lst) / len(lst)
    print("Среднее арифметическое ", mean_number)
    return mean_number

mean(my_list)

newlst = sorted(lst)
print(newlst)
