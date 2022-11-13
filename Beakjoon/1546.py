import sys

num = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
max_num = max(n_list)
avg_list = []
for i in range(num):
    avg_list.append((n_list[i] / max_num) * 100)
print(sum(avg_list) / num)
