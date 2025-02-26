# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

if sum(a) != sum(b):
    print(-1)
    exit()

p1 = p2 = 0
size = 0
while p1 < n and p2 < m:
    if a[p1] == b[p2]:
        p1 += 1
        p2 += 1
        size += 1
    while p1 < n-1 and a[p1] < b[p2]:
        a[p1+1] += a[p1]
        p1 += 1
    while p2 < m-1 and a[p1] > b[p2]:
        b[p2+1] += b[p2]
        p2 += 1
print(size)


