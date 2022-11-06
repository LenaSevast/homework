n = int(input("Введите колличество элементов в списке - "))
my_list = []
for i in range (n):
    number = int(input("Введите элемент "))
    my_list.append(number)
print(my_list)
new_list = []
for i in my_list:
    num = i ** 2
    new_list.append(num)
print(new_list)
