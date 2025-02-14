# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = 0
    max_sum = 0
    while l < n:
        cur_max = a[l]
        r = l+1
        while r < n and (a[r] > 0) == (a[l] > 0):
            cur_max = max(cur_max, a[r])
            r += 1
        
        max_sum += cur_max
        l = r
    print(max_sum)