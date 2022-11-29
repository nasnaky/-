import sys

min_num = int(sys.stdin.readline())
max_num = int(sys.stdin.readline())

sum_num = []

for i in range(min_num, max_num + 1):
    if i == 1:
        pass
    elif i == 2:
        sum_num.append(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i - 1:
                sum_num.append(i)
if sum(sum_num) == 0:
    print(-1)
    exit(0)

print(sum(sum_num))
print(min(sum_num))
