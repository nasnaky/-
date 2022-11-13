import sys

num = int(sys.stdin.readline())
count = 1
sum1 = ((num % 10) * 10)
sum2 = (num % 10 + int(num / 10)) % 10
sum = sum1 + sum2
while num != sum:
    sum1 = ((sum % 10) * 10)
    sum2 = (sum % 10 + int(sum / 10)) % 10
    sum = sum1 + sum2
    count = count + 1

print(count)
