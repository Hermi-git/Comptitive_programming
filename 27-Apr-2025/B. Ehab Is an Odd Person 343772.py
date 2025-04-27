# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
a = list(map(int, input().split()))
a_even = [num for num in a if num%2 == 0]
a_odd = [num for num in a if num%2==1]
if len(a_even) > 0 and len(a_odd) > 0:
    a.sort()
print(*a)