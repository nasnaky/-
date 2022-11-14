import sys

i_num = int(input())
for i in range(i_num):
    num = list(map(int, sys.stdin.readline().split()))

    num.sort()

    if num[3] - num[1] >= 4:
        print("KIN")
        continue
    print(num[1] + num[2] + num[3])

