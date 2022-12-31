import sys

num = int(sys.stdin.readline())
N_list = [1 for _ in range(10**7 + 1)]

s_list = []
for i in range(2, 10 ** 7 + 1):
    if N_list[i] == 1:
        s_list.append(i)
        for j in range(i + i, 10 ** 7 + 1, i):
            N_list[j] = 0

print(s_list[num - 1])
