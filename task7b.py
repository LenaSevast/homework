n = input().split()
lst = []

for i in range(len(n)):
    lst.append(int(n[i]))
print(lst)

#создаю новый список из подходящих элементов
new_lst = []
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1] and lst[i] > lst[i+1]:
        new_lst.append(lst[i])
print(new_lst)

#длина нового списка
a = len(new_lst)
print(a)

