# Problem: B - The Lord of Medianfell - https://codeforces.com/gym/599383/problem/B

from math import ceil
t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    mid = ceil(n/2)
    range = n-mid+1
    ans = s//range
    print(ans)