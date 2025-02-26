# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
a = list(map(int, input().split()))
a.sort()
minimum = a[(n-1)//2]
print(minimum)