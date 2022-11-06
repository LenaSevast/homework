n = int(input("Введите колличество элементов в списке - "))
my_list = []
for i in range (n):
    number = int(input("Введите элемент "))
    my_list.append(number)
print(my_list)
new_list = []
for i in my_list:
    if i % 2 == 0:
        new_list.append(i)
print(new_list)