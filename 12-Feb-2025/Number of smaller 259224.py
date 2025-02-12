# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

p1 = 0
res = []
for p2 in range(m):
    while p1 < n and a[p1] < b[p2]:
        p1 += 1
    res.append(p1)
print(*res)
