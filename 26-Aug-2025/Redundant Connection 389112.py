# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [0] * (len(edges)+1)

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return parent[x]
        
        def union(x, y):
            parentX= find(x)
            parentY= find(y)
            if parentX != parentY:
                rankX = rank[parentX]
                rankY = rank[parentY]
                if rankX > rankY:
                    parent[parentY] = parentX
                elif rankY > rankX:
                    parent[parentX] = parentY
                else:
                    parent[parentY] = parentX
                    rank[parentX] += 1
                return True
        
        for u, v in edges:
            if not union(u,v):
                return [u, v]
            
        