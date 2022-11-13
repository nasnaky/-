import sys

num = list(map(int, sys.stdin.readline().split()))
num.sort()
str_N = ""
for i in range(len(num)):
    str_N += str(num[i]) + " "
print(str_N)
