# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        black = -1
        color = [black for _ in range(len(graph))]
        visited = set()
        def dfs(node):
            for neigh in graph[node]:
                if neigh in visited:
                    if color[node] == color[neigh]:
                        return False
                else:
                    if color[neigh] == -1:
                        if color[node] == 0:
                            color[neigh] = 1
                        else:
                            color[neigh] = 0
                        visited.add(neigh)
                        res = dfs(neigh)
                        if not res:
                            return False

            return True

        for node in range(len(graph)):
            if color[node] == -1:
                visited.add(node)
                color[node] = 0
                if not dfs(node):
                    return False
        
        return True 
        

        
                

