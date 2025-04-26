# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            indegree[v] +=1
        nodes =[]
        for i in range(n):
            if indegree[i] == 0:
                nodes.append(i)
        if len(nodes) == 1:
            return nodes[0]
        else:
            return -1

        
        