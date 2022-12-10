num = int(input())
for i in range(num):
    if i == 0:
        print(" " * (num - 1) + "*")
    elif i == num - 1:
        print("*" * (num * 2 - 1))
    else:
        print(" " * (num - i - 1) + "*" + " " * ((i - 1) * 2 + 1) + "*")
