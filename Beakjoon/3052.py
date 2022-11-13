import sys

a = []
for i in range(10):
    num = int(sys.stdin.readline())
    a.append(num)

for i in range(10):
    a[i] = a[i] % 42
a = set(a)
a = list(a)
print(len(a))
