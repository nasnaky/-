import sys

num = list(map(int, sys.stdin.readline().split()))

if num[2] - num[1] <= 0:
    print(-1)
    exit(0)
mon = num[2] - num[1]
count = int(num[0] / mon + 1)
print(count)
