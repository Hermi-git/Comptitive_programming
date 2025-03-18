# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    curr = 1
    for i in range(n):
        if a[i] == curr:
            curr += 1
        b.append(curr)
        curr += 1
    print(b[-1])
   

  
        