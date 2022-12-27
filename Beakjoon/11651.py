import sys

n = int(sys.stdin.readline())
n_list = []
for i in range(n):
    num = list(map(int, sys.stdin.readline().split()))
    t = num[1]
    num[1] = num[0]
    num[0] = t
    n_list.append(num)
n_list.sort()
for i in range(n):
    print(n_list[i][1],n_list[i][0])