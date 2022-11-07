n = input().split()
lst = []
for i in range(len(n)):
    lst.append(int(n[i]))

def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    print(lst)
change(lst)


