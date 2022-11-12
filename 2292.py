import sys

num = int(sys.stdin.readline())
i = 1
numd = 1
if num == i:
    print(i)
    exit(0)
while True:
    numd = numd + (i * 6)
    if num <= numd:
        print(i+1)
        exit(0)
    i = i + 1
