# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())

count = 0

for num in range(1, n+1):
    factors = set()
    temp = num
    if temp % 2 == 0:
        factors.add(2)
        while temp % 2 == 0:
            temp //= 2
    
    i = 3
    while i * i <= num:
        while temp % i == 0:
            factors.add(i)
            temp //= i
        i += 2
    
    if temp > 1:
        factors.add(temp)
    
    if len(factors) == 2:
        count += 1

print(count)


