def checkNum(num):
    check = True

    lst = list()
    for i in range(1, len(str(num))):
        num1 = int(str(num)[i])
        num2 = int(str(num)[i - 1])
        lst.append(num1 - num2)

    checkTmp = 0
    for i in range(0, len(lst)):
        if i == 0: checkTmp = lst[i]

        if checkTmp != lst[i]:
            check = False
            break

    return check
a = int(input())

if a < 100:
    print(a)
else:
    cnt = 99
    for i in range(100, a + 1):
        if checkNum(i):
            cnt += 1

    print(cnt)