import sys
num = [0] * 10
S = 1
for i in range(3):
    S *= int(sys.stdin.readline())
for i in str(S):
    N = int(i)
    num[N] += 1
for i in num:
    print(i)