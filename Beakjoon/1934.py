import sys
import math

f = int(sys.stdin.readline())
for i in range(f):
    num = list(map(int, sys.stdin.readline().split()))
    min_num = min(num)
    print(math.lcm(num[0], num[1]))
