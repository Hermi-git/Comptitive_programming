# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = [i for i in range(4 * n * n)]
        rank = [0] * (4 * n * n)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[py] > rank[px]:
                parent[px] = py
            else:
                parent[py] = px
                rank[px] += 1

        for i in range(n):
            for j in range(len(grid[i])):
                t0 = (i * n + j) * 4 + 0 
                t1 = (i * n + j) * 4 + 1  
                t2 = (i * n + j) * 4 + 2  
                t3 = (i * n + j) * 4 + 3 

                #connect triangle inside cell 

                cell = grid[i][j]
                if cell == ' ':
                    union(t0, t1)
                    union(t1, t2)
                    union(t2, t3)
                elif cell == '/':
                    union(t0, t3)
                    union(t1, t2)
                elif cell == '\\':
                    union(t0, t1)
                    union(t2, t3)

                # connect to bottom neighbor if exists
                if i + 1 < n:
                    t2 = (i * n + j) * 4 + 2
                    t0_below = ((i+1) * n + j) * 4 + 0
                    union(t2, t0_below)

                # connect to right neighbor if exists
                if j + 1 < n:
                    t1 = (i * n + j) * 4 + 1
                    t3_right = (i * n + (j+1)) * 4 + 3
                    union(t1, t3_right)

        roots = set(find(x) for x in range(4 * n * n))
        return len(roots)



