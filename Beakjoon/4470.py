num = int(input())
S = []
for i in range(num):
    S.append(input())
for i in range(num):
    print(str(i+1)+". "+S[i])