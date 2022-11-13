import sys
a, b = map(int, sys.stdin.readline().split())
r_a = r_b = 0

r_a = int(a / 100) + (int(a / 10) % 10 * 10) + int(a % 10*100)
r_b = int(b / 100) + (int(b / 10) % 10 * 10) + int(b % 10*100)

if r_a > r_b:
    print(r_a)
elif r_a < r_b:
    print(r_b)