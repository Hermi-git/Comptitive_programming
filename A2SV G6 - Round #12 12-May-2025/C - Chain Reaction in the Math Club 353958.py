# Problem: C - Chain Reaction in the Math Club - https://codeforces.com/gym/606404/problem/C

from collections import defaultdict
students, laces = map(int, input().split())
graph = defaultdict(list)
degree = [0] * (students+1)

for _ in range(laces):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for node in range(1, students + 1):
    degree[node] = len(graph[node])

group = 0
while True:
    leaves= []
    for node in range(1, students+1):
        if degree[node] == 1:
            leaves.append(node)
    if not leaves:
        break
    group += 1
    for leave in leaves:
        degree[leave] = 0
    for leave in leaves:
        for neigh in graph[leave]:
            if degree[neigh] >0:
                degree[neigh] -= 1
print(group)

    


        