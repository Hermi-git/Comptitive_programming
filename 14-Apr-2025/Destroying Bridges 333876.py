# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    answer = n  
    for x in range(1, n + 1):
        if x * (n - x) <= k:
            answer = x
            break
    print(answer)
