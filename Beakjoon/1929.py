import sys


def check(x):
    for ie in range(2, int(i ** 0.5) + 1):
        if x % ie == 0:
            return False
    return True


num = list(map(int, sys.stdin.readline().split()))
for i in range(num[0], num[1] + 1):
    if i == 1:
        continue
    elif check(i):
        print(i)
