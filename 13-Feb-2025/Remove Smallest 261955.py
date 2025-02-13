# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n-1):
        if a[i+1] -a[i] == 1 or a[i+1] -a[i] == 0:
            count += 1
    if n - count == 1:
        print("YES")
    else:
        print("NO")

            
       
