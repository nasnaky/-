import sys

num = int(sys.stdin.readline())
s = []
for i in range(num):
    s.append(sys.stdin.readline().strip())
set_lst = list(set(s))
s.sort()
s.sort(key=len)
for i in s:
    print(i)
