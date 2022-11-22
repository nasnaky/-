import sys

num = sys.stdin.readline()
num = int(num, 2)
num = num * 17
print(format(num, 'b'))
