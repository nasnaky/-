import sys
import math

A = int(sys.stdin.readline())
A_list = list(map(int, sys.stdin.readline().split()))
B = int(sys.stdin.readline())
B_list = list(map(int, sys.stdin.readline().split()))

A_num = 1
B_num = 1
for i in A_list:
    A_num *= i
for i in B_list:
    B_num *= i

print(str(math.gcd(A_num, B_num))[-9:])
