# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import Counter
t= int(input())
for _ in range(t):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    l = 0
    sub = a[:d]
    a_dict = Counter(sub)
    min_sub = len(a_dict)
    for r in range(d, n):
        a_dict[a[r]] += 1

        a_dict[a[l]] -= 1
        if a_dict[a[l]] == 0:
            del a_dict[a[l]]
        l += 1

        min_sub = min(min_sub, len(a_dict))
    print(min_sub if min_sub else -1)

    