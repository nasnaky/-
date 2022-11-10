import sys

a = list(map(int, sys.stdin.readline().split()))
num1 = []
num2 = []
x = a[0]
y = a[1]
a[0] = 0
a[1] = 0

for i in range(2):
    num1.append(abs(x - a[i*2]))
for i in range(2):
    num2.append(abs(y - a[i*2+1]))

min_x = min(num1)
min_y = min(num2)

if min_x < min_y:
    print(min_x)
elif min_x > min_y:
    print(min_y)
else:
    print(min_x)
