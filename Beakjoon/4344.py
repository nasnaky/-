import sys

num = int(sys.stdin.readline())
for i in range(num):
    n_list = list(map(int, sys.stdin.readline().split()))
    count = 0
    con = n_list[0]
    del n_list[0]
    avg = sum(n_list) / con
    for i in range(con):
        if n_list[i] > avg:
            count = count + 1
    retun = (count / con) * 100
    print("{:.3f}".format(retun) + "%")
