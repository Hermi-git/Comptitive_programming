# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

from collections import defaultdict
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    # getting input matrix
    matrix = []
    for j in range(n):
        matrix.append(list(map(int, input().split())))
    forward = defaultdict(int)
    backward = defaultdict(int)
    for row in range(n):
        for col in range(m):
            forward[row + col] += matrix[row][col]
            backward[row - col] += matrix[row][col]
    max_sum = 0
    for row in range(n):
        for col in range(m):
            max_sum = max(max_sum, forward[row + col] + backward[row - col] - matrix[row][col])
            
    print(max_sum)
