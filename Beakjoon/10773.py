import sys
n = int(sys.stdin.readline())
num = []
for i in range(n):
    S = int(sys.stdin.readline())
    if S != 0:
        num.append(S)
    else:
        num.pop()
print(sum(num))