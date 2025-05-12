# Problem: B - Gelada baboon's Family Trees - https://codeforces.com/gym/607625/problem/B

from collections import defaultdict
n = int(input())
p = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(n):
    graph[i+1].append(p[i])
    graph[p[i]].append(i+1)
visited =set()
def dfs(node):
    visited.add(node)
    for neigh in graph[node]:
        if neigh  not in visited:
            dfs(neigh)
component=0
for i in range(n):
    if i+1 not in visited:
        dfs(i+1)
        component+=1
print(component)



