import sys

while True:
    num = list(map(int, sys.stdin.readline().split()))
    if sum(num) == 0:
        exit(0)
    else:
        num.sort()
        if num[0]**2 + num[1]**2 == num[2]**2:
            print("right")
        else:
            print("wrong")