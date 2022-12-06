num = []
for i in range(3):
    num.append(int(input()))
if sum(num) != 180:
    print("Error")
    exit(0)
else:
    num = list(set(num))
    if len(num) == 1:
        print("Equilateral")
        exit(0)
    elif len(num) == 2:
        print("Isosceles")
        exit(0)
    elif len(num) == 3:
        print("Scalene")
        exit(0)