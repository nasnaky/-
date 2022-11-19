import sys

num = int(sys.stdin.readline())
for i in range(num):
    S1, S2 = map(str, sys.stdin.readline().split())
    s1 = sorted(list(S1))
    s2 = sorted(list(S2))
    if s1 == s2:
        print("%s & %s are anagrams." % (S1, S2))
    else:
        print("%s & %s are NOT anagrams." % (S1, S2))
