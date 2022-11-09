a, b = input().split()
a = int(a)
b = int(b)
num = int(input())

b = b + num

while b >= 60:
    a = a + 1
    b = b - 60

if a >= 24:
    a = a - 24

print(a, b)
