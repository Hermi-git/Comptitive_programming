# Problem: C - Arya Meets the Night King  - https://codeforces.com/gym/599383/problem/C

s,b=map(int,input().split())
arr=list(map(int,input().split()))
arr2 =[]
for _ in range(b):
    d, g = map(int, input().split())
    arr2.append([d, g])
res = []
for i in range(s):
    ans = 0
    for j in range(b):
        if arr[i] >= arr2[j][0]:
            ans += arr2[j][1]
    res.append(ans)
print(*res)


    