import sys

a = list(map(int, sys.stdin.readline().split()))
hol = []
su = 1

for i in range(3):
    if a[i] % 2 == 1:
        hol.append(a[i])

if not hol:
    for i in range(3):
        su = su * a[i]
else:
    for i in range(len(hol)):
        su = su * hol[i]
print(su)
