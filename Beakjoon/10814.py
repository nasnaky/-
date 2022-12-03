import sys

n = int(sys.stdin.readline())
N_list = []
for i in range(n):
    N_list.append(list(sys.stdin.readline().split()))

N_list.sort(key=lambda x: int(x[0]))
for i in range(n):
    print(" ".join(N_list[i]))
