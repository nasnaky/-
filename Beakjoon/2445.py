num = int(input())
for i in range(1, num + 1):
    print("*" * i + " "*(num-i)*2 + "*" * i)
for i in range(1, num):
    print("*" * (num-i) + " "*i*2 + "*" * (num-i))

