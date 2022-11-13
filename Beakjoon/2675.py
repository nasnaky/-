ae = int(input())
for h in range(ae):
    num, strs = input().split()
    num = int(num)
    stre = ""
    for i in strs:
        stre = stre + i*num
    print(stre)
