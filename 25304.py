num = int(input())
count = int(input())
while count != 0:
    a, b = input().split()
    a = int(a)
    b = int(b)
    num = num - (a*b)
    count = count - 1
if num == 0:
    print("Yes")
else:
    print("No")
