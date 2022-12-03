import sys

n = int(sys.stdin.readline())
N_list = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if M_list[i] in N_list:
        print("1")
    else:
        print("0")