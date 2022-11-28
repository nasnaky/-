import sys

num = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(1, num[0]+1):
    if num[0] % i == 0:
        count += 1
        if count == num[1]:
            print(i)
            exit(0)
print(0)
