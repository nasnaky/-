num = []
for i in range(5):
    n = int(input())
    if n < 40:
        n = 40
    num.append(n)
print(sum(num)//5)