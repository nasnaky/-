import sys

num = int(sys.stdin.readline())
N_list = [0] * 10001
for i in range(num):
    N = int(sys.stdin.readline())
    N_list[N] = N_list[N] + 1
for i in range(10001):
    if N_list[i] != 0:
        for H in range(N_list[i]):
            print(i)