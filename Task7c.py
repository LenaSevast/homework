n = input().split()
lst = []

for i in range(len(n)):
    lst.append(int(n[i]))
print(lst)

c = 0
for i in lst:
    a = lst.count(i)
    if a == 1:
        c +=1
print(c)