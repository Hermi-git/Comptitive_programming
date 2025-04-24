# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        white = 0
        gray = 1
        black = 2
        colors= [0 for _ in range(len(graph))]
        order = []

        def dfs(node):
            if colors[node] == gray:
                return False
            colors[node] = 1
            for neigh in graph[node]:
                if colors[neigh] == black:
                    continue
                if not dfs(neigh):
                    return False
            colors[node] = 2
            order.append(node)
            return True

        for node in range(len(graph)):
            if colors[node] == white:
                dfs(node)
        order.sort()
        return order

        
       
