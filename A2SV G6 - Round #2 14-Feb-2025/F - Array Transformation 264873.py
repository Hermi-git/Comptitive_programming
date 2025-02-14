# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    elm_count = Counter()
    freq_count = Counter()
    for i in range(n):
        elm_count[a[i]] += 1
        freq_count[elm_count[a[i]]] += 1
    res = []
    for freq, elm in freq_count.items():
        ans = n - (freq* elm)
        res.append(ans)
    min_res = min(res)
    print(min_res)


    