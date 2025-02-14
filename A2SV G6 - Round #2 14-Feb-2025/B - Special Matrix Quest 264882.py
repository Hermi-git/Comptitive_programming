# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
good_sum = 0
for i in range(n):
    for j in range(n):
        if i == j or i  == n-1-j or i == n//2 or j == n//2:
            good_sum += matrix[i][j]

print(good_sum)