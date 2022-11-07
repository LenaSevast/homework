n = input().split()
lst = []

for i in range(len(n)):
    lst.append(int(n[i]))
print(lst)

c = 0
seen = []
for i in lst:
    if i not in seen:
        c += 1
        seen.append(i)
print(c)
