stre = input()
a = []
sae = ""
for i in range(26):
    a.append(-1)

for i in range(len(stre)):
    num = ord(stre[i]) - 97
    if a[num] == -1:
        a[num] = i
for i in range(26):
    sae = sae + str(a[i]) + " "
print(sae)
