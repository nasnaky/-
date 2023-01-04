import sys

num = list(map(int, sys.stdin.readline().split()))


def 제곱(num0, num1):
    if num1 == 0:
        return 1
    x = 제곱(num0, num1 // 2) % num[2]
    if num1 % 2 == 0:
        return x * x
    else:
        return x * x * num0


print(제곱(num[0], num[1]) % num[2])
