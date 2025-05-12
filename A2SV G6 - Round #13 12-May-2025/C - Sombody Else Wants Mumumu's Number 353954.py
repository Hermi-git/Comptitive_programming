# Problem: C - Sombody Else Wants Mumumu's Number - https://codeforces.com/gym/607625/problem/C

from collections import Counter
t = int(input())
for _ in range(t):
    n= int(input())
    a = list(map(int, input().split()))
    a_count = Counter(a)
    max_value = max(a_count.values())
    if max_value <= n//2:
        print(n%2)
    else:
        print((2 * max_value) - n)