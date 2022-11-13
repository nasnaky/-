count = int(input())
L_list = []
for i in range(count):
    L_list.append(int(input()))
L_list.sort()
for i in range(count):
    print(L_list[i])