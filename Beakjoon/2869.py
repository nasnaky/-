# import sys
#
# num, M, V = map(int, sys.stdin.readline().split())
# D = 0
# while True:
#     D = D + 1
#     if (D*num)-(M*(D-1)) >= V:
#         break
# print(D)

a, b, v = map(int, input().split())
k = (v - b) / (a - b)
print(int(k) if k == int(k) else int(k) + 1)
