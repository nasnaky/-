import sys

num = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))

N_list = list(set(N_list))
N_list.sort()

S = ""
for i in range(len(N_list)):
    S = S + str(N_list[i]) + " "
print(S)
