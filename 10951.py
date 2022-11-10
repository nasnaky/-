import sys

a, b = map(int, sys.stdin.readline().split())
try:
    while 1:
        print(a + b)
        a, b = map(int, sys.stdin.readline().split())
except Exception:
    exit(0)
