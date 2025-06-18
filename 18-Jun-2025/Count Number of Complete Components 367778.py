# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[]for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(node, connected_nodes):
            visited.add(node)
            connected_nodes.append(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh, connected_nodes)
        
        complete_nodes =0
        for node in range(n):
            if node not in visited:
                connected_nodes = []
                dfs(node, connected_nodes)
                
                total_edges= 0
                for node in connected_nodes:
                    total_edges += len(graph[node])
                total_edges //= 2

                m = len(connected_nodes)
                if total_edges == m*(m-1)//2:
                    complete_nodes += 1
        return complete_nodes
        