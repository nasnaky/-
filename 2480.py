a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a == b == c:
    print(10000 + a * 1000)
elif a ==b:
    print(1000 + a * 100)
elif c == b:
    print(1000 + c * 100)
elif a == c:
    print(1000 + a * 100)
else:
    num = max(a,b,c)
    print(num*100)