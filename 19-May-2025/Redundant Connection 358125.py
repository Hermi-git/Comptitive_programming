# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [0] * (len(edges)+1
)
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parentx, parenty = find(x), find(y)
            if parentx == parenty:
                return False
            if rank[parentx] > rank[parenty]:
                parent[parenty] = parentx
            elif rank[parentx] < rank[parenty]:
                parent[parentx] = parenty
            else:
                parent[parenty] = parentx
                rank[parentx] += 1
            return True
            
                
        for x, y in edges:
            if not union(x, y):
                return [x, y]  