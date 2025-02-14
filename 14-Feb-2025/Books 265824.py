# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
a = list(map(int, input().split()))
l = 0
max_books = 0
cur_books = 0
for r in range(n):
    cur_books += a[r]
    while cur_books > t:
        cur_books -= a[l]
        l += 1
    max_books = max(max_books, r-l+1)
print(max_books)