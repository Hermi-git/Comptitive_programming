# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

from collections import defaultdict
nodes, edges = map(int, input().split())
graph = defaultdict(list)
for _ in range(edges):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
edge_list =[]
for u in graph:
    for v, w in graph[u]:
        if u < v:
            edge_list.append((w, u, v))
edge_list.sort()

parent = [i for i in range(nodes + 1)]  
rank = [0] * (nodes + 1) 
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootx, rooty = find(x), find(y)
    rankx, ranky = rank[rootx], rank[rooty]
    if rootx != rooty:
        if rankx > ranky:
            parent[rooty] = rootx
        elif ranky > rankx:
            parent[rootx] = rooty
        else:
            parent[rooty] = rootx
            rankx += 1

mst = []
for edge in edge_list:
    if find(edge[1]) != find(edge[2]):
        mst.append(edge[0])
        union(edge[1], edge[2])
    if len(mst) == nodes -1:
        break
print(sum(mst)) 