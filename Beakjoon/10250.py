import sys

i = int(input())
for i in range(i):
    H, W, N = map(int, sys.stdin.readline().split())
    num1 = int(N / H) + 1
    num100 = N % H
    if num100 == 0:
        num100 = H
        num1 = num1 - 1

    print(num100 * 100 + num1)
