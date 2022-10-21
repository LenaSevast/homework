z = '\t'
x = '\n'
for i in range(1, 11):
    print(z, i, end='')
print()
for j in range(1, 11):
    print(j, end='')
    for q in range(1, 11):
        print(z, j*q, end="")
    print()
