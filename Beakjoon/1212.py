import sys

num = sys.stdin.readline()
num10 = int(num, 8)
num2 = format(num10, 'b')
print(num2)
