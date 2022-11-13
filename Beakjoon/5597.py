import sys

a = []
for i in range(30):
    a.append(0)

for i in range(28):
    num = int(sys.stdin.readline())
    a[num - 1] = 1

for i in range(30):
    if a[i] == 0:
        print(i)
