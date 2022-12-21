num = int(input())
for i in range(num - 1):
    print(" " * i + "*" * (num - i - 1) + "*" + "*" * (num - i - 1))
for i in range(num):
    print(" " * (num - i - 1) + "*" * i + "*" + "*" * i)
