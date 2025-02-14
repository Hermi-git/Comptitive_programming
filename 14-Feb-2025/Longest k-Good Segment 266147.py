# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
a_dict = defaultdict(int)
l = 0
longest_K = [1, 1]
for r in range(n):
    a_dict[a[r]] += 1
    while len(a_dict) > k:
        a_dict[a[l]] -= 1
        if a_dict[a[l]] == 0:
            del a_dict[a[l]]
        l += 1
    if r - l > longest_K[1] - longest_K[0]:
        longest_K = [l+1, r+1]
print(*longest_K)
