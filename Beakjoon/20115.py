import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
sums = 0.0
num.sort(reverse=True)
for i in range(n):
    if i == 0:
        sums = float(num[i])
    else:
        sums += num[i]/2
if sums % 1.0 == 0:
    print(int(sums))
else:
    print(sums)