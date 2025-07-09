# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict
import heapq

n = int(input())
names = [input().strip() for _ in range(n)]
graph = defaultdict(list)
indegree = {chr(i + ord('a')): 0 for i in range(26)}

for i in range(n-1):
    if names[i].startswith(names[i+1]) and len(names[i]) > len(names[i+1]):
        print("Impossible")
        exit()
    else:
        for j in range(len(names[i])):
            if names[i][j] != names[i+1][j]:
                graph[names[i][j]].append(names[i+1][j])
                indegree[names[i+1][j]] += 1
                break
q = []
order = []  
for i in range(26):
    ch = chr(i + ord('a'))
    if indegree[ch] == 0:
        heapq.heappush(q, ch)
while q:
    letter =  heapq.heappop(q)
    order.append(letter)
    for neigh in graph[letter]:
        indegree[neigh] -= 1
        if indegree[neigh] == 0:
            heapq.heappush(q, neigh)
if len(order) == 26:
    print("".join(order))
else:
    print("Impossible")
        

