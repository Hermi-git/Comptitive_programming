# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split()) 
recipes = []
for _ in range(n):
    l, r = map(int, input().split())
    recipes.append([l,r])

prefix_recipes = [0] * 200001
for l, r in recipes:
    prefix_recipes[l] += 1
    if r+1 < len(prefix_recipes):
        prefix_recipes[r+1] -= 1
for i in range(1, len(prefix_recipes)):
    prefix_recipes[i] += prefix_recipes[i-1]
for j in range(len(prefix_recipes)):
    if prefix_recipes[j] >= k:
        prefix_recipes[j] = 1
    else:
        prefix_recipes[j] = 0
for i in range(1, len(prefix_recipes)):
    prefix_recipes[i] += prefix_recipes[i-1]


for _ in range(q):
    a, b = map(int, input().split())
   
    ans = prefix_recipes[b] - prefix_recipes[a-1]
    print(ans)
