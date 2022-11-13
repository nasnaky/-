def check(w):
    n_w = []
    for i in w:
        if i not in n_w:
            n_w.append(i)
        if i != n_w[-1]:
            return False
    return True


num = int(input())
count = 0
for i in range(num):
    w = input()
    if check(w):
        count = count + 1

print(count)
