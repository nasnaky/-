import sys


def sosu(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    return False


cnt = 0
ie = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for iw in range(ie):
    if sosu(nums[iw]):
        cnt += 1

print(cnt)
