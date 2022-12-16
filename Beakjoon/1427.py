num = input()
N_list = []
for i in num:
    N_list.append(int(i))
N_list.sort(reverse=True)
print("".join(map(str, N_list)))