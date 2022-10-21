a = int(input())
b = int(input())
c = int(input())
if a == b and b == c and a == c:
    print("равносторонний")
if a != b != c:
    print("разносторонний")
if a == b and b != c:
    print("равнобедренный")
if a == c and a != b:
    print("равнобедренный")
if b == c and a != b:
    print("равнобедренный")