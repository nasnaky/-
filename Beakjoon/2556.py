import sys

num = []
for i in range(9):
    num.append(list(map(int, sys.stdin.readline().split())))
for i in range(9):
    for j in range(9):
        if num[i][j] == max(map(max, num)):
            print(max(map(max, num)))
            print(i+1, j+1)
            exit(0)
