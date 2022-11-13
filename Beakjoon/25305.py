import sys

C = list(map(int, sys.stdin.readline().split()))
num = list(map(int, sys.stdin.readline().split()))
num.sort()

print(num)
print(num[-C[1]])
