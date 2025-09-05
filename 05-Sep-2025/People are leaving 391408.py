# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

n, m = map(int, input().split())
parent= [i for i in range(n+2)]
def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return parent[x]

def union(x, y):
    rx = find(x)
    ry = find(y)
    if rx != ry:
        parent[rx] = ry 

for _ in range(m):
    query = input().split()

    if query[0] == "?":
        person = int(query[1])
        root = find(person)
        if root > n:
            print(-1)
        else:
            print(root)
    elif query[0] == "-":
        person = int(query[1])
        union(person, person+1)

