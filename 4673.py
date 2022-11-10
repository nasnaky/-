num = set(range(1,10001))
G_num = set()

for i in range(1,10001):
    for j in str(i):
        i = i + int(j)
    G_num.add(i)

s_num = sorted(num - G_num)
for i in s_num:
    print(i)