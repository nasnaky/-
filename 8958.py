import sys

ae = int(sys.stdin.readline())
for i in range(ae):
    stre = sys.stdin.readline()
    count = 0
    num = 0

    for i in range(len(stre)):
        if stre[i] == "O":
            count = count + 1
            num = num + count
        elif stre[i] == "X":
            count = 0
    print(num)


