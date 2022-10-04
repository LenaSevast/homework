n = int(input())
my_list = []
for i in range(n):
    number = int(input())
    my_list.append(number)
print(my_list)
for i in my_list:
    if i % 2 == 0:
        print(i)
