# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

node, edge = map(int, input().split())
graph = [[]for _ in range(node+1)]
for _ in range(edge):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
degrees = [0] * (node + 1)
for i in range(1, node + 1):
    degrees[i] = len(graph[i])
cnt_1 = 0
cnt_2 = 0
cnt_center = 0
for i in range(1, len(degrees)):
    if degrees[i] == 1:
        cnt_1 += 1
    elif degrees[i] == 2:
        cnt_2 += 1
    elif degrees[i] == (node-1):
        cnt_center += 1
if node > edge and cnt_1 == 2 and cnt_2 == (node-2):
    print("bus topology") 
elif node == edge and cnt_2 == node:
    print("ring topology")
elif node > edge and cnt_1 == (node-1) and cnt_center == 1:
    print("star topology")
else:
    print("unknown topology")
