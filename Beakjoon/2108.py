import sys
from collections import Counter

num = int(sys.stdin.readline())
N_list = []
for _ in range(num):
    N_list.append(int(sys.stdin.readline()))
N_list.sort()
print(round(sum(N_list) / num))
print(N_list[num // 2])
cnt = Counter(N_list).most_common(2)
if len(N_list) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(N_list) - min(N_list))
