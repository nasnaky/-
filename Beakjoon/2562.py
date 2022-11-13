import sys

a = []
for i in range(9):
    num = int(sys.stdin.readline())
    a.append(num)
print(max(a))
print(a.index(max(a))+1)
