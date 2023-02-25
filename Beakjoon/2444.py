num = int(input())
for i in range(num-1):
    print(" " * (num - i - 1) + "*" * i + "*" + "*" * i)
for i in range(num):
    print(" " * i + "*" * (num - i - 1) + "*" + "*" * (num - i - 1))