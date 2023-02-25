from itertools import combinations
import sys

n_list = []
for i in range(9):
    n_list.append(int(sys.stdin.readline()))
for i in combinations(n_list, 7):
    if sum(i) == 100:
        i = list(i)
        i.sort()
        for ie in i:
            print(ie)
        exit(0)
