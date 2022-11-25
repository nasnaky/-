import sys
num = int(sys.stdin.readline())
N_list = []
for i in range(num):
    N_list.append(int(sys.stdin.readline()))
N_list.sort()
for i in range(num):
    print(N_list[i])