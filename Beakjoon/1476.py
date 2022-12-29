import sys

E, S, M = map(int, sys.stdin.readline().split())

y = 1
while (y - E) % 15 != 0 or (y - S) % 28 != 0 or (y - M) % 19 != 0:
    y += 1
print(y)
