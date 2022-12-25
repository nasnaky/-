import sys
n = int(sys.stdin.readline())
for i in range(n):
    num = list(map(int, sys.stdin.readline().split()))
    num.sort()
    print(num[-3])
