import sys

num = int(sys.stdin.readline())
count = 0
while num >= 0:
    if num % 5 == 0:
        count += int(num / 5)
        print(count)
        exit(0)
    num -= 2
    count += 1
print(-1)


