# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

left, right = 0 , 0
result = []
while left < n or right < m:
    if right == m or left < n and a[left]<=b[right]:
        result.append(a[left])
        left += 1
    else:
        result.append(b[right])
        right += 1
print(*result)