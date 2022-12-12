import sys

n = int(sys.stdin.readline())
n_list = []
for i in range(n):
    n_list.append(list(map(int, sys.stdin.readline().split())))
n_list.sort()
for i in range(n):
    print(n_list[i][0],n_list[i][1])