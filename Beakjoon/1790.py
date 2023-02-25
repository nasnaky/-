import sys

num = list(map(int, sys.stdin.readline().split()))
cnt = 1
count = 9
now = 0

while num[1] > cnt * count:
    num[1] -= (cnt * count)
    now += count
    cnt += 1
    count *= 10
now = (now + 1) + (num[1] - 1) // cnt

if now > num[0]:
    print(-1)
else:
    print(str(now)[(num[1] - 1) % cnt])
