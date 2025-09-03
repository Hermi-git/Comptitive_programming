# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

n, m = map(int, input().split())
parent = [i for i in range(n+1)]   
size = [1] * (n+1)              
team_add = [0] * (n+1)                
offset = [0] * (n+1)            

def find(x):
    if parent[x] != x:
        p = parent[x]
        root = find(p)         
        offset[x] += offset[p]       
        parent[x] = root       
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    
    if rootX == rootY:
        return

    if size[rootX] > size[rootY]:
        parent[rootY] = rootX
        offset[rootY] = team_add[rootX] - team_add[rootY]  
        size[rootX] += size[rootY]
    else:
        parent[rootX] = rootY
        offset[rootX] = team_add[rootY] - team_add[rootX] 
        size[rootY] += size[rootX]


for _ in range(m):
    query = input().split()
    
    if query[0] == 'add':
        x = int(query[1])
        v = int(query[2])
        root = find(x)
        team_add[root] += v

    elif query[0] == 'join':
        union(int(query[1]), int(query[2]))

    elif query[0] == 'get':
        x = int(query[1])
        root = find(x)
        xp = team_add[root] - offset[x]
        print(xp)
