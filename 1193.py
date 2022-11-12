num = int(input())

count = 0
n_count = 0
while n_count < num:
    count = count + 1
    n_count = n_count + count

i = n_count - num
F_num = 0
L_num = 0
if count % 2 == 0:
    F_num = count
    L_num = 1
    for ie in range(i):
        L_num = L_num + 1
        F_num = F_num - 1
else:
    F_num = 1
    L_num = count
    for ie in range(i):
        L_num = L_num - 1
        F_num = F_num + 1

print(str(F_num) + "/" + str(L_num))
