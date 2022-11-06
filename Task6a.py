n = int(input("Введите колличество строк "))
string = ""
for i in range(n):
    string += input("Введите строку ")
    string += " "
print(string)
x = string.count(" ")
print(x)

