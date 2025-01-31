# Problem: Sum - https://codeforces.com/contest/1742/problem/A

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    a, b, c = sorted([a, b, c])
    if c == a+b:
        print("YES")
    else:
        print("NO")