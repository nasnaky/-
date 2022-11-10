import sys

cont = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
num = int(sys.stdin.readline())

count = 0
for i in range(cont):
    if n_list[i] == num:
        count = count + 1
print(count)
