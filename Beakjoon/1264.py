ST = input()
S = ['a', 'e', 'i', 'o', 'u']
while ST != "#":
    ST = ST.lower()
    count = 0
    for i in ST:
        if i in S:
            count += 1
    print(count)
    ST = input()