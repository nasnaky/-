import sys

num = list(map(int, sys.stdin.readline().split()))
S = 0
for i in num:
    S += i ** 2
print(S % 10)
