# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[]for _ in range(n)]
        for r, c in edges:
            graph[r].append(c)
            graph[c].append(r)
        
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    ans = dfs(neigh, visited)
                    if ans:
                        return True
            return False
        return dfs(source, set())

        
            
                    

                


            
        
        