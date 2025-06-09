# Problem: D - Restricted Permutation - https://codeforces.com/gym/607625/problem/D

import heapq
from collections import defaultdict
n, m = map(int, input().split())
graph = defaultdict(list)
in_degree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

heap = []
for i in range(1, n + 1):
    if in_degree[i] == 0:
        heapq.heappush(heap, i)

ans = []
while heap:
    node = heapq.heappop(heap)
    ans.append(node)
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            heapq.heappush(heap, neighbor)

if len(ans) == n:
    print(*ans)
else:
    print(-1)