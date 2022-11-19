ms = input()
n = int(input())
li = sorted([input() for i in range(n)])
p = i = 0
for ie in range(n):
    L = ms.count("L") + li[ie].count("L")
    O = ms.count("O") + li[ie].count("O")
    V = ms.count("V") + li[ie].count("V")
    E = ms.count("E") + li[ie].count("E")
    a = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    if p < a:
        p = a
        i = ie
print(li[i])
